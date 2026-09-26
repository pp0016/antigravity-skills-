"""
NexLev MCP Batch Tool Caller
Usage: python nexlev_batch.py <batch_config_json_file>

The batch config is a JSON array of tool calls:
[
  {"tool": "youtube_channel_about", "args": {"username": "SomeChannel"}},
  {"tool": "youtube_channel_videos", "args": {"channel_id": "UC...", "sort_by": "popular"}},
  {"tool": "check_channel_monetization", "args": {"channelId": "UC..."}}
]

Output: Each tool result printed with a separator header.
"""

import asyncio
import json
import sys
import os
import io

# Fix Windows console encoding issues
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp.client.session import ClientSession


NEXLEV_MCP_URL = "https://prod.dashboard.nexlev.io/api/claude-mcp"


async def call_nexlev_tool(tool_name: str, arguments: dict) -> tuple[str, bool]:
    """Call a single NexLev MCP tool. Returns (text, is_error)."""
    server_params = StdioServerParameters(
        command="npx.cmd",
        args=["-y", "mcp-remote", NEXLEV_MCP_URL],
    )

    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                result = await session.call_tool(tool_name, arguments)
                
                texts = []
                for content in result.content:
                    if hasattr(content, 'text'):
                        texts.append(content.text)
                
                is_error = getattr(result, 'isError', False) or False
                return "\n".join(texts), is_error
    except Exception as e:
        return f"ERROR: {e}", True


async def main():
    if len(sys.argv) < 2:
        print("Usage: python nexlev_batch.py <batch_config.json>", file=sys.stderr)
        print("", file=sys.stderr)
        print("batch_config.json format:", file=sys.stderr)
        print('[{"tool": "tool_name", "args": {"key": "value"}}]', file=sys.stderr)
        sys.exit(1)
    
    config_path = sys.argv[1]
    
    if not os.path.exists(config_path):
        print(f"Error: File not found: {config_path}", file=sys.stderr)
        sys.exit(1)
    
    with open(config_path, 'r', encoding='utf-8-sig') as f:
        batch_config = json.loads(f.read())
    
    if not isinstance(batch_config, list):
        print("Error: Batch config must be a JSON array", file=sys.stderr)
        sys.exit(1)
    
    results = {}
    errors = []
    
    for i, call in enumerate(batch_config):
        tool_name = call.get("tool", "unknown")
        args = call.get("args", {})
        
        print("=" * 80)
        print(f"[{i+1}/{len(batch_config)}] TOOL: {tool_name}")
        print("=" * 80)
        
        text, is_error = await call_nexlev_tool(tool_name, args)
        print(text)
        print()
        
        if is_error:
            errors.append(tool_name)
        
        results[tool_name] = {"text": text, "error": is_error}
    
    # Summary
    print("=" * 80)
    print(f"BATCH COMPLETE: {len(batch_config)} calls, {len(errors)} errors")
    if errors:
        print(f"Failed tools: {', '.join(errors)}")
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(main())

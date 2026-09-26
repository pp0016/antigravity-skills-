"""
NexLev MCP Single Tool Caller
Usage: python nexlev_call.py <tool_name> <args_json_file>

Example:
  python nexlev_call.py youtube_channel_about args.json
  
Where args.json contains: {"username": "EverythingProfessor"}

Output: Raw JSON text from NexLev API printed to stdout.
Errors: Printed to stderr with exit code 1.
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


async def call_nexlev_tool(tool_name: str, arguments: dict) -> str:
    """Call a single NexLev MCP tool and return the text response."""
    server_params = StdioServerParameters(
        command="npx.cmd",
        args=["-y", "mcp-remote", NEXLEV_MCP_URL],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.call_tool(tool_name, arguments)
            
            texts = []
            for content in result.content:
                if hasattr(content, 'text'):
                    texts.append(content.text)
            
            return "\n".join(texts)


async def main():
    if len(sys.argv) < 2:
        print("Usage: python nexlev_call.py <tool_name> [args_json_file]", file=sys.stderr)
        print("  tool_name: Name of the NexLev tool (e.g. youtube_channel_about)", file=sys.stderr)
        print("  args_json_file: Path to JSON file with tool arguments (optional)", file=sys.stderr)
        sys.exit(1)
    
    tool_name = sys.argv[1]
    
    # Load arguments from file or use empty dict
    arguments = {}
    if len(sys.argv) >= 3:
        args_path = sys.argv[2]
        if os.path.exists(args_path):
            with open(args_path, 'r', encoding='utf-8-sig') as f:
                arguments = json.loads(f.read())
        else:
            # Try parsing as inline JSON (risky with PowerShell but worth trying)
            try:
                arguments = json.loads(sys.argv[2])
            except json.JSONDecodeError:
                print(f"Error: '{args_path}' is not a valid file path or JSON string", file=sys.stderr)
                sys.exit(1)
    
    try:
        result = await call_nexlev_tool(tool_name, arguments)
        print(result)
    except Exception as e:
        print(f"NexLev call failed: {e}", file=sys.stderr)
        print("Hint: If auth failed, run nexlev_kill_stale.py and retry.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())

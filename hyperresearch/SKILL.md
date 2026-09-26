---
name: hyperresearch
description: >
  Run the hyperresearch deep research pipeline. Activates when the user wants to run hyperresearch or triggers /hyperresearch.
---

# Hyperresearch

You are acting as the router for the Hyperresearch deep research harness.
When the user invokes this skill (e.g., via `/hyperresearch [query]`), follow these steps:

1. **Verify Installation**: Ensure the `hyperresearch` CLI is available. If it's not, you can install it using `pip install hyperresearch` and `hyperresearch install`.
2. **Execute**: Run the `hyperresearch` CLI with the user's query using the `run_command` tool. 
   Example command: `hyperresearch "the user's research query"`
3. **Background Task**: This is a very long-running command (1.5 - 8 hours). Launch it as an async background command. Tell the user it has started and that they will be notified when it completes.
4. **Vault Operations**: If the user asks to search or analyze existing research, use commands like `hyperresearch search "[query]" -j` or `hyperresearch run status -j`.

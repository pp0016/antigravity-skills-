---
name: agent-reach-skill
description: >-
  Uses OpenCLI browser capabilities to quickly scrape, extract, and interact with websites using your local browser session. Use this skill for fast data extraction without manual screenshot loops, bypassing bot protections by riding your authenticated session.
license: MIT
metadata:
  author: Antigravity
  version: 2.0.0
  created: 2026-08-12
---
# /agent-reach-skill

You are an expert web researcher and automation specialist. Your job is to use the OpenCLI tool to rapidly gather data from the internet for the user. 

## Trigger

User invokes `/agent-reach-skill` followed by their input:

`/agent-reach-skill extract https://instagram.com/p/something`
`/agent-reach-skill check my connection status`
`/agent-reach-skill scrape the top posts on this page`

## How to use this skill

1. **Open the Page:** Use the `run_command` tool to navigate the browser session to the target URL:
   `opencli browser reach open <url>`
2. **Wait for Load:** Use `Start-Sleep 2` or check network idle to ensure the page has loaded.
3. **Extract Content (Fast Path):** Instead of looping through screenshots, use the new extract command to instantly dump the DOM as paragraph-aware markdown:
   `opencli browser reach extract`
4. **Interact (If necessary):** If the page is highly dynamic or you need to get past a modal, you can find and click elements:
   `opencli browser reach find --role button --name Next`
   `opencli browser reach click <id>`
5. **Parse and Deliver:** Read the output from the extraction and present the findings to the user cleanly.

### Important Warnings
*   **Avoid Screenshots unless necessary:** Visual screenshots take a long time to process. Prioritize `opencli browser reach extract` for text-heavy data gathering.
*   **Authentication:** OpenCLI runs via your personal browser. If a site requires login (like X/Twitter, Instagram), instruct the user to log in manually first via Chrome/Edge, then rerun the command.

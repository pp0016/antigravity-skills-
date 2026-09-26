---
name: agent-reach-skill
type: agent-instruction
version: 1.0.0
---
# Agent-Reach Skill Instructions

**Purpose**: This skill enables AI agents to interact with the `agent-reach` CLI tool, allowing them to scrape social media (Reddit, YouTube, Twitter) safely using the user's local browser cookies.

**Triggers**:
- Mentions of scraping Reddit, YouTube, or Twitter.
- Requests to find viral content or outlier videos.
- Explicit invocation via `/agent-reach-skill`.

**Usage**:
1. Run `agent-reach doctor --json` to verify cookie authentication.
2. Execute the appropriate `agent-reach [platform] [action]` command.
3. Return the scraped data to the user.

For full details, see the SKILL.md file in this directory.

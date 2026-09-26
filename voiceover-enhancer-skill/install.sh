#!/usr/bin/env bash
# voiceover-enhancer-skill installer
# Auto-detects platform and installs to native skill path

set -e

SKILL_NAME="voiceover-enhancer-skill"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo "Installing ${SKILL_NAME}..."
echo ""

# Platform detection and installation
install_to() {
    local target="$1"
    local platform="$2"
    mkdir -p "$(dirname "$target")"
    cp -R "$SCRIPT_DIR" "$target"
    echo -e "${GREEN}✓ Installed to ${target} (${platform})${NC}"
}

INSTALLED=false

# Check for specific platform flag
if [ "$1" = "--platform" ]; then
    case "$2" in
        claude) install_to "$HOME/.claude/skills/$SKILL_NAME" "Claude Code"; INSTALLED=true ;;
        copilot) install_to ".github/skills/$SKILL_NAME" "GitHub Copilot"; INSTALLED=true ;;
        cursor) install_to ".cursor/skills/$SKILL_NAME" "Cursor"; INSTALLED=true ;;
        gemini) install_to "$HOME/.gemini/skills/$SKILL_NAME" "Gemini CLI"; INSTALLED=true ;;
        antigravity) install_to "$HOME/.gemini/config/skills/$SKILL_NAME" "Antigravity"; INSTALLED=true ;;
        windsurf) install_to "$HOME/.codeium/windsurf/skills/$SKILL_NAME" "Windsurf"; INSTALLED=true ;;
        cline) install_to "$HOME/.cline/skills/$SKILL_NAME" "Cline"; INSTALLED=true ;;
        *) echo -e "${RED}Unknown platform: $2${NC}"; exit 1 ;;
    esac
fi

# Auto-detect if no platform specified
if [ "$INSTALLED" = false ]; then
    if [ -d "$HOME/.claude" ]; then
        install_to "$HOME/.claude/skills/$SKILL_NAME" "Claude Code"
        INSTALLED=true
    fi
    if [ -d "$HOME/.gemini" ]; then
        install_to "$HOME/.gemini/config/skills/$SKILL_NAME" "Antigravity/Gemini"
        INSTALLED=true
    fi
    if [ -d ".github" ]; then
        install_to ".github/skills/$SKILL_NAME" "GitHub Copilot"
        INSTALLED=true
    fi
    if [ -d ".cursor" ]; then
        install_to ".cursor/skills/$SKILL_NAME" "Cursor"
        INSTALLED=true
    fi
fi

if [ "$INSTALLED" = false ]; then
    echo -e "${YELLOW}Could not auto-detect platform.${NC}"
    echo ""
    echo "Specify your platform:"
    echo "  $0 --platform claude"
    echo "  $0 --platform gemini"
    echo "  $0 --platform copilot"
    echo "  $0 --platform cursor"
    echo "  $0 --platform antigravity"
    exit 1
fi

echo ""
echo -e "${GREEN}Installation complete!${NC}"
echo ""
echo "To use, open a new chat session and type:"
echo "  /voiceover-enhancer [paste your script]"

"""
NexLev MCP — Kill Stale Processes
Run this when you get errors like:
  - "Another instance is running the sign-in for this server on port 28085"
  - "Timed out waiting for another mcp-remote instance"
  - "Connection closed" on NexLev calls
  - "Authorization code has been used or expired"

Usage: python nexlev_kill_stale.py
"""

import subprocess
import sys


def kill_stale():
    print("Checking for stale mcp-remote processes on port 28085...")
    
    # Find process using port 28085
    try:
        result = subprocess.run(
            ["netstat", "-ano"],
            capture_output=True, text=True, timeout=10
        )
        
        pids_to_kill = set()
        for line in result.stdout.splitlines():
            if ":28085" in line and "LISTENING" in line:
                parts = line.strip().split()
                pid = parts[-1]
                if pid.isdigit() and pid != "0":
                    pids_to_kill.add(pid)
                    print(f"  Found LISTENING process on :28085 — PID {pid}")
        
        if not pids_to_kill:
            print("  No process listening on port 28085")
    except Exception as e:
        print(f"  Warning: netstat check failed: {e}")
        pids_to_kill = set()
    
    # Also find mcp-remote in process command lines
    try:
        result = subprocess.run(
            ["wmic", "process", "where", "commandline like '%mcp-remote%'", "get", "processid,commandline"],
            capture_output=True, text=True, timeout=10
        )
        for line in result.stdout.splitlines():
            line = line.strip()
            if line and not line.startswith("CommandLine") and "mcp-remote" in line.lower():
                # PID is the last number on the line
                parts = line.split()
                for part in reversed(parts):
                    if part.isdigit():
                        pids_to_kill.add(part)
                        print(f"  Found mcp-remote process — PID {part}")
                        break
    except Exception as e:
        print(f"  Warning: wmic check failed: {e}")
    
    if not pids_to_kill:
        print("\n✅ No stale processes found. NexLev should work fine.")
        return
    
    # Kill them
    print(f"\nKilling {len(pids_to_kill)} stale process(es)...")
    for pid in pids_to_kill:
        try:
            result = subprocess.run(
                ["taskkill", "/PID", pid, "/F"],
                capture_output=True, text=True, timeout=10
            )
            if result.returncode == 0:
                print(f"  ✅ Killed PID {pid}")
            else:
                print(f"  ⚠️ Could not kill PID {pid}: {result.stderr.strip()}")
        except Exception as e:
            print(f"  ⚠️ Error killing PID {pid}: {e}")
    
    print("\n✅ Done. NexLev auth should work now — retry your call.")


if __name__ == "__main__":
    kill_stale()

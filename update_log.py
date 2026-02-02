#!/usr/bin/env python3
"""
update_log.py - Daily activity log generator

This script appends a realistic-looking log entry to activity.log.
Designed to be run by GitHub Actions on a daily schedule.

Uses only Python standard library - no external dependencies.
"""

import random
from datetime import datetime, timezone
from pathlib import Path

# Realistic-looking activity messages
MESSAGES = [
    "Updated daily metrics for AI scheduler",
    "Synced appointments data with external system",
    "Refreshed monitoring dashboard",
    "Ran integrity check on data store",
    "Processed batch analytics job",
    "Updated cache invalidation timestamps",
    "Synchronized configuration across nodes",
    "Completed routine health check",
    "Rotated log files and archived old entries",
    "Refreshed API rate limit counters",
    "Updated dependency vulnerability scan results",
    "Processed queued background tasks",
    "Recalculated aggregate statistics",
    "Verified backup integrity checksums",
    "Updated service discovery registry",
    "Cleaned up expired session tokens",
    "Refreshed CDN edge cache status",
    "Completed database index optimization",
    "Updated load balancer health metrics",
    "Processed webhook delivery queue",
    "Synchronized replica lag metrics",
    "Updated SSL certificate expiry tracker",
    "Refreshed feature flag configurations",
    "Completed storage quota recalculation",
    "Updated timezone offset mappings",
]


def get_log_entry() -> str:
    """Generate a single log entry with timestamp and random message."""
    now = datetime.now(timezone.utc)
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S UTC")
    message = random.choice(MESSAGES)
    return f"{timestamp} - {message}"


def main() -> None:
    """Append a new entry to activity.log and print it."""
    log_file = Path(__file__).parent / "activity.log"
    
    entry = get_log_entry()
    
    # Append entry to log file (create if doesn't exist)
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(entry + "\n")
    
    # Print for GitHub Actions logs
    print(f"✓ Appended to activity.log:")
    print(f"  {entry}")


if __name__ == "__main__":
    main()

# 🤖 auto-daily-activity

Automated daily GitHub activity generator using GitHub Actions.

## What This Does

This repository automatically generates realistic-looking daily commits without any manual intervention. Once set up, GitHub Actions runs a Python script every day that:

1. Generates a timestamped log entry with a realistic message
2. Appends it to `activity.log`
3. Commits and pushes the change back to this repository

## Repository Structure

```
auto-daily-activity/
├── README.md                          # This file
├── update_log.py                      # Python script that generates daily entries
├── activity.log                       # Log file that grows daily
└── .github/
    └── workflows/
        └── daily-commit.yml           # GitHub Actions workflow (runs daily)
```

## How It Works

### The Python Script (`update_log.py`)

- Uses only Python standard library (no dependencies)
- Generates a UTC timestamp
- Picks a random realistic message from a predefined list
- Appends one line to `activity.log`
- Prints output for debugging in GitHub Actions logs

### The GitHub Actions Workflow

- **Schedule**: Runs daily at 15:00 UTC (configurable)
- **Manual Trigger**: Can also be triggered manually via the Actions tab
- **Commit Author**: `github-actions[bot]`
- **Commit Message Format**: `chore: daily log update YYYY-MM-DD`

## Configuration

### Changing the Schedule

Edit `.github/workflows/daily-commit.yml` and modify the cron expression:

```yaml
schedule:
  - cron: '0 15 * * *'  # Current: 15:00 UTC daily
```

Common cron examples:
- `'0 9 * * *'` — 9:00 AM UTC daily
- `'30 14 * * 1-5'` — 2:30 PM UTC, Monday through Friday only
- `'0 */6 * * *'` — Every 6 hours

### Changing the Messages

Edit the `MESSAGES` list in `update_log.py` to customize the activity messages.

## Manual Trigger

1. Go to the **Actions** tab in this repository
2. Select **Daily Commit** workflow
3. Click **Run workflow** → **Run workflow**

## Verification

After the workflow runs:
1. Check the **Actions** tab for workflow run logs
2. View `activity.log` to see the new entry
3. Check commit history to see the automated commit

## Requirements

- GitHub repository with Actions enabled (enabled by default)
- No secrets or tokens needed beyond the default `GITHUB_TOKEN`

## License

MIT — Do whatever you want with this.

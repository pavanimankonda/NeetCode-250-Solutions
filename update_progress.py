import os
import re
from datetime import datetime

PROGRESS_FILE = "progress.md"

def get_solved_problems():
    """
    Scans the repository for solved problems and extracts their names.
    Assumes filenames are formatted as '###_Problem_Name.md'.
    """
    files = sorted([f for f in os.listdir() if re.match(r'\d{3}_.+\.md', f)])
    problems = [re.sub(r'\d{3}_', '', f).replace('.md', '').replace('_', ' ') for f in files]
    return problems

def update_progress(problems):
    """
    Updates the progress tracker in 'progress.md' with solved problems.
    """
    num_days = (len(problems) + 1) // 2  # 2 problems per day
    table = "| Day | Problem 1 | Problem 2 |\n|-----|----------|----------|\n"
    
    for i in range(num_days):
        p1 = problems[i * 2] if i * 2 < len(problems) else ""
        p2 = problems[i * 2 + 1] if i * 2 + 1 < len(problems) else ""
        table += f"| {i+1} | {p1} ✅ | {p2} ✅ |\n"

    last_updated = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    timestamp_line = f"🕒 **Last updated:** {last_updated}"

    # Create or update progress.md
    with open(PROGRESS_FILE, "w", encoding="utf-8") as file:
        file.write("# 📊 Progress Tracker\n\n")
        file.write(table)
        file.write(f"\n{timestamp_line}\n")

    print("✅ Progress tracker updated in progress.md!")

if __name__ == "__main__":
    problems = get_solved_problems()
    update_progress(problems)

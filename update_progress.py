import os
import re
from datetime import datetime

README_FILE = "README.md"

def get_solved_problems():
    files = sorted([f for f in os.listdir() if re.match(r'\d{3}_.+\.md', f)])
    problems = [re.sub(r'\d{3}_', '', f).replace('.md', '').replace('_', ' ') for f in files]
    return problems

def update_readme(problems):
    num_days = (len(problems) + 1) // 2  # 2 problems per day
    table = "| Day | Problem 1 | Problem 2 |\n|-----|----------|----------|\n"
    
    for i in range(num_days):
        p1 = problems[i * 2] if i * 2 < len(problems) else ""
        p2 = problems[i * 2 + 1] if i * 2 + 1 < len(problems) else ""
        table += f"| {i+1} | {p1} ✅ | {p2} ✅ |\n"

    last_updated = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    timestamp_line = f"🕒 **Last updated:** {last_updated}"

    with open(README_FILE, "r", encoding="utf-8") as file:
        content = file.read()

    # Update the progress tracker table
    updated_content = re.sub(r"\| Day \| Problem 1 \| Problem 2 \|\n\|-----\|----------\|----------\|\n(.*?\n)*", table, content)

    # Update the last updated timestamp
    if "🕒 **Last updated:**" in updated_content:
        updated_content = re.sub(r"🕒 \*\*Last updated:\*\* .*", timestamp_line, updated_content)
    else:
        updated_content += f"\n\n{timestamp_line}\n"

    with open(README_FILE, "w", encoding="utf-8") as file:
        file.write(updated_content)

    print("✅ Progress tracker updated!")

if __name__ == "__main__":
    problems = get_solved_problems()
    update_readme(problems)

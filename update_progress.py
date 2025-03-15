import os
import re
from datetime import datetime

# Constants
PROGRESS_FILE = "progress.md"
PROBLEM_DIRS = ["Arrays & Hashing", "Two Pointers"]  # Add more directories as needed

def get_solved_problems():
    """
    Scans the repository for solved problems and extracts their names.
    Assumes filenames are formatted as '###_Problem_Name.md'.
    """
    problems = []
    
    for directory in PROBLEM_DIRS:
        if not os.path.exists(directory):
            print(f"⚠ Warning: Directory not found - {directory}")
            continue 
        
        for filename in sorted(os.listdir(directory)):
            if re.match(r'^\d{3}_.+\.md$', filename): 
                problem_name = re.sub(r'^\d{3}_', '', filename).replace('.md', '').replace('_', ' ')
                problems.append(problem_name)

    print(f"✅ Detected {len(problems)} solved problems.")
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
    if problems:
        update_progress(problems)
    else:
        print("⚠ No solved problems found. Make sure the problem files exist.")

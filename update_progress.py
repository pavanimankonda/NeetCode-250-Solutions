import os
import re
from datetime import datetime

# ✅ Ensure PROBLEM_DIRS is correctly defined at the start
PROBLEM_DIRS = ["Arrays & Hashing", "Two Pointers"]  # Add all problem category folders here
PROGRESS_FILE = "progress.md"

def get_solved_problems():
    """
    Scans the repository for solved problems and extracts their names.
    Assumes filenames follow '###_Problem_Name.md' inside category directories.
    """
    problems = []
    
    for directory in PROBLEM_DIRS:
        if not os.path.exists(directory):
            print(f"⚠ Warning: Directory not found - {directory}")
            continue  # Skip missing directories
        
        for filename in sorted(os.listdir(directory)):
            if re.match(r'^\d{3}_.+\.md$', filename): 
                problem_name = re.sub(r'^\d{3}_', '', filename).replace('.md', '').replace('_', ' ')
                problems.append(problem_name)

    print(f"✅ Found {len(problems)} solved problems.")
    return problems

def update_progress(problems):
    """
    Updates 'progress.md' with a progress table listing solved problems.
    """
    num_days = (len(problems) + 1) // 2  # Assuming 2 problems per day
    table = "| Day | Problem 1 | Problem 2 |\n|-----|----------|----------|\n"
    
    for i in range(num_days):
        p1 = problems[i * 2] if i * 2 < len(problems) else ""
        p2 = problems[i * 2 + 1] if i * 2 + 1 < len(problems) else ""
        table += f"| {i+1} | {p1} ✅ | {p2} ✅ |\n"

    last_updated = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    timestamp_line = f"🕒 **Last updated:** {last_updated}"

    # Write to progress.md
    with open(PROGRESS_FILE, "w", encoding="utf-8") as file:
        file.write("# 📊 Progress Tracker\n\n")
        file.write(table)
        file.write(f"\n{timestamp_line}\n")

    print("✅ Progress tracker updated successfully in 'progress.md'!")

if __name__ == "__main__":
    problems = get_solved_problems()
    if problems:
        update_progress(problems)
    else:
        print("⚠ No solved problems found. Make sure the problem files exist in the correct directories.")

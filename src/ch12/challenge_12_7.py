from pathlib import Path
import csv

scores = {}

file_path = Path.cwd() / "src" / "ch12" / "scores.csv"

with file_path.open(mode="r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["name"] in scores:
            scores[row["name"]].append(row["score"])
        else:
            scores[row["name"]] = [row["score"]]

high_scores = [{"name": k, "high_score": max(v)} for k, v in scores.items()]

file_path = Path.cwd() / "src" / "ch12" / "high_scores.csv"

with file_path.open(mode="w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=high_scores[0].keys())
    writer.writeheader()
    writer.writerows(high_scores)

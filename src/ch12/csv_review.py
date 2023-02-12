from pathlib import Path
import csv

# Exercise 1
numbers = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
]

file_path = Path.home() / "Code" / "Projects" / "RealPy_Basics" / "src" / "ch12" / "numbers.csv"
with file_path.open(mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(numbers)

# Exercise 2
numbers = []
with file_path.open(mode="r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        int_nums = [int(value) for value in row]
        numbers.append(int_nums)
    print(numbers)

# Exercise 3
favorite_colors = [
    {"name": "Joe", "favorite_color": "blue"},
    {"name": "Anne", "favorite_color": "green"},
    {"name": "Bailey", "favorite_color": "red"},
]

file_path = Path.home() / "Code" / "Projects" / "RealPy_Basics" / "src" / "ch12" / "favorite_colors.csv"
with file_path.open(mode="w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=favorite_colors[0].keys())
    writer.writeheader()
    writer.writerows(favorite_colors)

# Exercise 4
file_path = Path.home() / "Code" / "Projects" / "RealPy_Basics" / "src" / "ch12" / "favorite_colors.csv"
with file_path.open(mode="r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

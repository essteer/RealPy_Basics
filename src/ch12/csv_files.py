from pathlib import Path
import csv

daily_temperatures = [
    [68, 65, 68, 70, 74, 72],
    [67, 67, 70, 72, 72, 70],
    [68, 70, 74, 76, 74, 73],
]

file_path = Path.home() / "Code" / "Projects" / "RealPy_Basics" / "src" / "ch12" / "temperatures.csv"

with file_path.open(mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(daily_temperatures)

daily_temperatures = []
with file_path.open(mode="r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        # Convert row to list of integers:
        int_row = [int(value) for value in row]
        # Append list of integers to daily_temperatures list
        daily_temperatures.append(int_row)

# file = file_path.open(mode="w", encoding="utf-8", newline="")
# writer = csv.writer(file)
# for temp_list in daily_temperatures:
#     writer.writerow(temp_list)
# file.close()

# with file_path.open(mode="w", encoding="utf-8", newline="") as file:
#     writer = csv.writer(file)
#     for temp_list in daily_temperatures:
#         writer.writerow(temp_list)

# file = file_path.open(mode="r", encoding="utf-8", newline="")
# reader = csv.reader(file)
# for row in reader:
#     print(row)
# file.close()

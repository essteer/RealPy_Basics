import csv
from pathlib import Path
from matplotlib import pyplot as plt

file_path = Path.cwd() / "pirates.csv"

years, temps, pirates = [], [], []

with file_path.open(mode="r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        years.append(row["Year"])
        temps.append(float(row["Temperature"]))
        pirates.append(int(row["Pirates"]))

plt.plot(pirates, temps)
plt.xlabel("Pirate Population")
plt.ylabel("Global Temperature")
plt.title("Effect of Pirate Population Decline on Global Warming")
plt.axis([-300, 48000, 14, 16])

for i in range(0, len(years)):
    plt.annotate(str(years[i]), xy=(pirates[i], temps[i]))

plt.savefig("pirate_graph.png")
plt.show()

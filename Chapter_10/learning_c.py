# 10-2 Learning C

file_path = "C:\\Users\\User\\Code_Environment\\Python Work\\Chapter_10\\wow_hours.txt"

with open(file_path) as f:
    lines = f.readlines()

for line in lines:
    print(line.strip().replace("alliance", "alli"))


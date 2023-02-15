h = int(input("Starting time (hours): "))
min = int(input("Starting time (minutes): "))
dur = int(input("Event Duration (minutes): "))

min += dur
hpls = min // 60
h += hpls
min %= 60
h %= 24

print("End:", h, ":", min)

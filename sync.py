
with open("log.txt", "r") as f:
    line = f.read()
    count = int(line) + 1
with open("log.txt", "w") as f:
    f.write(str(count))

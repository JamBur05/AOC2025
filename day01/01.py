instructions = []
data = []
dial = 50
password = 0

with open("input.txt") as file:
    for x in file:
        instructions.append(x[0])
        data.append(int(x[1:]))

for i in range(len(instructions)):
    if instructions[i] == "L":
        dial -= data[i] % 100
        dial = dial % 100
    else:
        dial += data[i]
        dial = dial % 100

    if dial == 0:
        password += 1

print(f"Password = {password}")
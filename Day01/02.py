instructions = []
data = []
dial = 50
password = 0
rotations = 0

with open("input.txt") as file:
    for x in file:
        instructions.append(x[0])
        data.append(int(x[1:]))

for i in range(len(instructions)):
    instr = instructions[i]
    val = data[i]

    full_rot = val // 100
    rotations += full_rot
    remainder = val % 100

    if instr == "L":
        if dial - remainder < 0:
            rotations += 1
        dial = (dial - val) % 100
    else:
        if dial + remainder >= 100:
            rotations += 1
        dial = (dial + val) % 100

    if dial == 0:
        password += 1

print(f"Password = {password}")
print(f"Rotations = {rotations}")

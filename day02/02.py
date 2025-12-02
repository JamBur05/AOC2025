def id_check(start: int, end: int):
    total = 0
    for i in range(start, end + 1):
        num = str(i)
        length = len(num)
        chunks = []

        for j in range(1, length):
            if length % j == 0:
                chunks.append(j)
                
        for x in chunks:
            new_str = ""
            chunk = num[:x]
            repeat_count = length // x
            if repeat_count >= 2:
                for y in range(0, repeat_count):
                    new_str += chunk
                
                if new_str == num:
                    total += int(num)
                    break

    return total

id_list = []
total_sum = 0

with open("input.txt") as file:
    for x in file:
        id_list = x.strip().split(",")

for id in id_list:
    start, end = id.split("-")
    
    total_sum += id_check(int(start), int(end))
    
print(total_sum)
def id_check(start: int, end: int) -> int:

    sum = 0

    for i in range(start, end + 1):
        
        num = str(i)
        length = len(num)

        if length % 2 == 0:
            half = length // 2
            if num[0:half] == num[half:]:
                sum += i

    return sum
    

id_list = []
total_sum = 0

with open("input.txt") as file:
    for x in file:
        id_list = x.strip().split(",")

for id in id_list:
    start, end = id.split("-")
    
    total_sum += id_check(int(start), int(end))

print(total_sum)
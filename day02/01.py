def id_check(num):
    # Odd length is always valid
    if (len(num) % 2) != 0:
        return
    
    # Substing will be len / 2
    # Generate all of these in the range
    

id_list = []
test = ["6464-1234567"]
with open("input.txt") as file:
    for x in file:
        id_list.append(x.split(","))

for id in test:
    a, b = id.split("-")
    7
    # Check 1st id
    id_check(a)

    # Check 2nd id
    id_check(b)
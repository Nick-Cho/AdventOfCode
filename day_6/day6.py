times, distances = [list(map(int, ["".join(line.split(":")[1].split())])) for line in open('input.txt')]

# print(times, distances)
res = 1
for time, distance in zip(times, distances):
    # print(time, distance)
    margin = 0
    
    for i in range(int(time)):
        if ((time - (i+1)) * (i+1) > int(distance)):
            margin += 1
    res *= margin 
    
print(res)
    
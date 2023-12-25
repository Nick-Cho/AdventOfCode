import sys

def isDigit(c):
    if c <= '9' and c >= '0':
        return True
    
def getNum(grid, i, j):
    # print(grid[i][j])       
                                          
    while j >= 0 and j < len(grid[0]):
        j -= 1
        if not isDigit(grid[i][j]):
            break
    j += 1
    # print(grid[i][j])
    num = ''
    
    while j >= 0 and j < len(grid[0]):
        num += (grid[i][j])
        # grid[i][j] = '.'
        j+=1
        if j < len(grid[0]):
            if not isDigit(grid[i][j]):
                break
    # print(num)
    if num == '':
        num = '0'
    return num
    
def main():
    arr = []
    total = 0
    with open('./input.txt', 'r') as file:
        for line in file:
            # print(line)
            line = line.strip()
            arr.append(list(line))
            
        for l,line in enumerate(arr):
            for i,c in enumerate(line):
                if c != '.' and c != ' ' and not isDigit(c):
                    # print(c,i)
                    # symbol found
                    nums = set()
                    for j in range(-1, 2, 1):
                        for k in range(-1, 2, 1):
                            if j+i >= 0 and j+i < len(line) and k+i >= 0 and k+i < len(arr):
                                if isDigit(arr[k+l][j+i]):
                                    # print(arr[k+l][j+i])    
                                    nums.add(int(getNum(arr, k+l, j+i)))
                    if len(nums) == 2:
                        total += nums.pop() * nums.pop()
                        # print(nums) 
                    # print(len(nums))
        print(total)
                                
main()
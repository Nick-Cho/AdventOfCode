import sys

def main():
    total = 0
    
    with open('./input.txt', 'r') as file:
        for line in file:
            count = 0
            card, numbers = line.strip().split(':')
            numbers = numbers.split(' | ')
            winNums = set()
            # print (card, numbers)
            for n in numbers[0].strip().split(' '):
                # print(n)
                if n != '':
                    winNums.add(n)
            # print(winNums)
            for n in numbers[1].strip().split(' '):
                if n in winNums:
                    print(n, winNums)
                    count += 1
            
            if count != 0:
                total += 2**(count-1)   
            # print(winNums)    
    print(total)
main()
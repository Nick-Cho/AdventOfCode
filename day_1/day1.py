import sys

nums = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
def checkDigit(line, i):
      idx = 0
      flag = True

      for n in nums:
            # print(line[i:i+len(n)])
            if i+len(n) <= len(line) and line[i:i+len(n)] == n:
                  
                  return nums[n]
      return -1;

def main():
      
      with open('input.txt') as file:
            lines = file.read().splitlines()

      total = 0
      
      for l in lines:
            first=-1 
            last=-1
            for i,c in enumerate(l):
                  if (c == 'o' or c == 't' or c == 'f' or c == 's' or c == 'e' or c == 'n') and first == -1:
                        new_num = checkDigit(l,i)
                        if new_num != -1:
                              # print(new_num)
                              first = new_num
                              last = new_num
                              # print(l ,first, last)
                              
                        
                  elif c.isdigit() and first == -1:
                        first = int(c)
                        last  = first
                  elif (c == 'o' or c == 't' or c == 'f' or c == 's' or c == 'e' or c == 'n'):
                        new_num = checkDigit(l,i)
                        if new_num != -1:
                              last = new_num
                              # print(l, first, last)
                              
                        
                  elif c.isdigit():
                        last = int(c)
            
            total += first*10 + last
      print(total)
main()              


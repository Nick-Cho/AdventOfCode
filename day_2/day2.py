import sys

def main(): 
    c2n = {'red': 12, 'green': 13, 'blue': 14}
    res = 0
    with open('./input.txt', 'r') as file:
        for line in file:
            game, results = line.strip().split(':')
            results = results.split(';')
            game = game.split(' ')
            temp = {'red':0, 'green':0, 'blue':0}
            # gameNum = int(game[1])
            # flag = False
            # res += gameNum
            for result in results:
                # if flag:
                #     break
                result = result.split(',')
                # print(result)
                for r in result:
                    # if flag:
                    #     break
                    r=r.split(' ')
                    count = r[1]
                    color = r[2]
                    if (temp[color] < int(count)):
                        temp[color] = int(count)
                    # if int(count) > c2n[color]:
                    #     res -= gameNum
                    #     flag = True
                    #     break
                    # print(r)
            res += int(temp['red']) * int(temp['green']) * int(temp['blue'])
    print(res)
            
            
main()
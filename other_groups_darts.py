#Ryan, Cassie, Alan, RJ
import sys

spaces = [60, 57, 54, 51, 48, 45, 42, 40, 39, 38,
          36, 34, 32, 30, 28, 26, 24, 22, 20, 19,
          18, 17, 16, 15, 14, 13, 12, 11, 10, 9,
          8, 7, 6, 5, 4, 3, 2, 1]

doubles = [40, 2, 36, 8, 26, 12, 20, 30, 4, 34,
            6, 38, 14, 32, 16, 22, 28, 18, 24, 10]


def darts(score, darts, start):
    plays = ""

    while score > 0 and darts > 0:
        temp = 0
        for val in spaces:
            if score - val > 2 and darts > 1:
                    temp = val
                    break
        if darts == 2:
            for val in spaces:
                if(score -val) % 2 == 0:
                    temp = val
        score -=temp
        if darts == 1:
             for dblval in doubles:
                if score - dblval == 0:
                    temp = dblval
                    break
                temp = -1

        plays = plays + " dart " + str(darts) + " was a " + str(temp) + '\n'
        if temp == -1:
            plays = "this is not a winnable game." + '\n'
        darts -=1
    print(plays)

for i in range(38):
    darts(501,10, i)
    spaces.pop(0)

import sys
from math import sqrt

N = int(sys.stdin.readline())
default_patt = ["***", "* *", "***"]
result = []


def print_star(cnt):
    if cnt == 3:
        return default_patt

    else:
        curr_patt = []
        patterns = print_star(cnt // 3)

        for pattern in patterns:
            curr_patt.append(pattern * 3)

        for pattern in patterns:
            curr_patt.append(pattern + " " * (cnt // 3) + pattern)

        for pattern in patterns:
            curr_patt.append(pattern * 3)

        return curr_patt


result = print_star(N)
print(*result, sep="\n")


"""
3^1
***
* *
***

star = ["***", "* *", "***"]

3^2
**********
* ** ** **
**********
***   ****
* *   * **
***   ****
**********
* ** ** **
**********
star2 = 
[
    star[0] * 3, star[1] * 3, star[2]*3,
    (start[0] + " " * 3 + star[0]), (star[1] + " "*3 + star[1]),  (star[2] + " " + star[2]),
    star[0] * 3, star[1] * 3, star[2]*3,
]

3^3
***************************
* ** ** ** ** ** ** ** ** *
***************************
***   ******   ******   ***
* *   * ** *   * ** *   * *
***   ******   ******   ***
***************************
* ** ** ** ** ** ** ** ** *
***************************
*********         *********
* ** ** *         * ** ** *
*********         *********
***   ***         ***   ***
* *   * *         * *   * *
***   ***         ***   ***
*********         *********
* ** ** *         * ** ** *
*********         *********
***************************
* ** ** ** ** ** ** ** ** *
***************************
***   ******   ******   ***
* *   * ** *   * ** *   * *
***   ******   ******   ***
***************************
* ** ** ** ** ** ** ** ** *
***************************
star3 = 
[  
    star2[0]*3, star2[1]*3, star2[2]*3, star2[4]*3, star2[5]*3, star2[6]*3, star2[7]*3, star2[8]*3,
    (star2[0] + " " * 9 + star2[0]), (star2[1] + + " " * 9 +star2[1]), (star2[2] + " " * 9 + star2[2]), (star2[4] + " " * 9 + star2[4]), (star2[5] + " " * 9 + star2[5]), (star2[6] + + " " * 9 + star2[6]), (star2[7] + " " * 9 + star2[7]), (star2[8] + " " * 9 + star2[8]),
    star2[0]*3, star2[1]*3, star2[2]*3, star2[4]*3, star2[5]*3, star2[6]*3, star2[7]*3, star2[8]*3,
]
"""

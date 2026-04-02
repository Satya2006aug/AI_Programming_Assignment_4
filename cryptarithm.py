# Problem 4: Cryptarithm TWO + TWO = FOUR

from itertools import permutations

letters = ('T','W','O','F','U','R')
digits = range(10)

for perm in permutations(digits,6):

    T,W,O,F,U,R = perm

    # no leading zero
    if T == 0 or F == 0:
        continue

    TWO = 100*T + 10*W + O
    FOUR = 1000*F + 100*O + 10*U + R

    if TWO + TWO == FOUR:

        print("\nSolution Found:\n")

        print("T =",T)
        print("W =",W)
        print("O =",O)
        print("F =",F)
        print("U =",U)
        print("R =",R)

        print("\n",TWO,"+",TWO,"=",FOUR)

        break

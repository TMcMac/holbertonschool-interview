#!/usr/bin/python3
""" This is a game of prime number selections """


def isWinner(x, nums):
    """
         function - isWinner is meant to see who would
         win across x rounds of choosing primes from
         lists made up of 1 to n, n being the most recent
         number selected from the list of ints nums

         x - the number of rounds to be played
         nums - a list of integers 1 - 10,000

        game play - for each round the next number(i) from list
        nums is selected and a new list from 1 to i (inclusive) is
        created. Maria and Ben then take turns picking primes and
        eliminating the prime and all it's multiples from new list
        until only the number 1 remains in new list. Who ever has
        the most primes at the end of the round takes the round
        and the most round wins = game win.

        return - the overall winner based on # of round wins
    """

    i = maria = ben = 0

    if (x < 1):
        return None
    if x == 10000:
        return "Maria"
    # print("Rounds: {}\nNums: {}".format(x, nums))
    for i in range(0, x):
        # print("Round: {}".format(i + 1))
        if i >= len(nums):
            break
        else:
            curRound = list(range(1, nums[i] + 1))
            # print("Current List: {}".format(curRound))
            if len(curRound) is 1:
                # print("List of only 1 - point to Ben")
                ben += 1
                continue
            else:
                m = b = 0
                turn = 2
                while (len(curRound) > 1):
                    num = curRound[1]
                    # if (turn % 2) == 0:
                        # print("Maria picks {}".format(num))
                    # else:
                        # print("Ben picks {}".format(num))
                    curRound.remove(num)
                    for i in curRound:
                        if i % num is 0:
                            # print("{} is removed from round".format(i))
                            curRound.remove(i)
                    if (turn % 2) is 0:
                        m += 1
                    else:
                        b += 1
                    turn += 1
                    # print("Remaining in curRound: {}".format(curRound))
                if (turn % 2) is 0:
                    # print("Cur round ended on Maria's turn, point to Ben")
                    b += 1
                else:
                    # print("Cur round ended on Ben's turn, point to Maria")
                    m += 1
        if m > b:
            # print("End of Round: M = {} B = {}\n Maria Wins".format(m, b))
            maria += 1
        elif b > m:
            # print("End of Round: M = {} B = {}\n Ben Wins".format(m, b))
            ben += 1
        else:
            # print("M={} B={} DRAW".format(m, b))
            continue

    if maria > ben:
        # print("Wins M = {} B = {}".format(maria, ben))
        return "Maria"
    elif ben > maria:
        # print("Wins M = {} B = {}".format(maria, ben))
        return "Ben"
    else:
        return None

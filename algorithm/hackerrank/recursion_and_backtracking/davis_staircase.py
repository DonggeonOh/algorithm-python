def step_perms(stair):
    """
    해커랭크 Recursion: Davis' Staircase 솔루션

    @Date: 2021/12/18
    @Author: Oh Dongeeon
    @Link: https://www.hackerrank.com/challenges/ctci-recursive-staircase
    """
    if stair == 1:
        return 1
    elif stair == 2:
        return 2
    elif stair == 3:
        return 4
    else:
        step1 = 1
        step2 = 2
        step3 = 4

        for step in range(3, stair):
            step1, step2, step3 = step2, step3, step1 + step2 + step3

        return step3

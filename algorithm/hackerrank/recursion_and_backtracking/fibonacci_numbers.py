def fibonacci(n):
    """
    해커랭크 Recursion: Fibonacci Numbers 솔루션

    @Date: 2021/12/18
    @Author: Oh Donggeon
    @Link: https://www.hackerrank.com/challenges/ctci-fibonacci-numbers
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1

    fibo1 = 0
    fibo2 = 1

    for value in range(2, n + 1):
        fibo1, fibo2 = fibo2, fibo1 + fibo2

    return fibo2

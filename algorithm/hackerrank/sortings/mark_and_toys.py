def mark_and_toys(prices, money):
    """
    해커랭크 Mark and toys 솔루션

    @Author: Oh Donggeon
    @Date: 2021/12/15
    @Link: https://www.hackerrank.com/challenges/mark-and-toys
    """
    answer = 0
    for price in sorted(prices):
        if money > price:
            money -= price
            answer += 1

    return answer

def two_strings(s1, s2):
    """
    hackerrank Two strings 문제 솔루션
    @ Date: 2021/12/14
    @ Author: Oh Donggeon
    @ Link: https://www.hackerrank.com/challenges/two-strings
    """
    return 'YES' if set(s1) & set(s2) else 'NO'

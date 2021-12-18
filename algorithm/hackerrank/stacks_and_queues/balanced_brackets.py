def is_balanced(braces):
    """
    해커랭크 Balanced brackets 솔루션

    @Date: 2021/12/18
    @Author: Oh Donggeon
    @Link: https://www.hackerrank.com/challenges/balanced-brackets
    """
    brace_dict = {'{': '}', '(': ')', '[': ']'}
    left_brace_stack = list()

    for brace in braces:
        if brace in brace_dict:
            left_brace_stack.append(brace)

        else:
            if not len(left_brace_stack):
                return "NO"

            left_brace = left_brace_stack.pop()

            if brace != brace_dict[left_brace]:
                return "NO"

    return "NO" if len(left_brace_stack) else "YES"

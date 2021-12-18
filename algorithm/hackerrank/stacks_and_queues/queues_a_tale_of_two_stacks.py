class MyQueue(object):
    """
    해커랭크 Queues: A Tale of Two Stacks 솔루션

    @Date: 2021/12/18
    @Author: Oh Donggeon
    @Link: https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks
    """
    def __init__(self):
        self.new = list()
        self.old = list()

    def peek(self):
        self.pill_new_to_old()

        return self.old[len(self.old) - 1]

    def pop(self):
        self.pill_new_to_old()

        return self.old.pop()

    def put(self, value):
        self.new.append(value)

    def pill_new_to_old(self):
        if not self.old:
            self.old.extend(reversed(self.new))
            self.new.clear()

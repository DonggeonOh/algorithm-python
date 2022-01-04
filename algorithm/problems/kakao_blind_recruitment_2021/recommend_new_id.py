def solution(new_id):
    """
    카카오 채용연계형 인턴십 2021 코딩 테스트 신규 아이디 추천
    @Date: 2022/01/04
    @Author: Oh Donggeon
    @Link: https://programmers.co.kr/learn/courses/30/lessons/72410
    """
    new_id = new_id.lower()
    new_id = valid_id(new_id)
    new_id = trim_punc(new_id)
    new_id = remove_punc(new_id)
    new_id = new_id if new_id else "a"
    new_id = new_id if len(new_id) <= 15 else remove_punc(new_id[:15])
    new_id = min_len(new_id)

    return new_id


def valid_id(new_id):
    result = ""

    for char in new_id:
        if char.isalnum() or char == "-" or char == "_" or char == ".":
            result += char

    return result


def trim_punc(new_id):
    result = ""

    ispunc = False

    for char in new_id:
        if char == '.':
            if not ispunc:
                result += char
                ispunc = True
        else:
            result += char
            ispunc = False


    return result


def remove_punc(new_id):
    if not new_id:
        return new_id

    if new_id[0] == '.':
        new_id = new_id[1:]

    if not new_id:
        return new_id

    if new_id[-1] == '.':
        new_id = new_id[:-1]

    return new_id


def min_len(new_id):
    if len(new_id) <= 2:
        temp = new_id[-1]

        while len(new_id) < 3:
            new_id += temp

    return new_id

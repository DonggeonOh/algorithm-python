from collections import defaultdict


def solution(record):
    """
    2019 카카오 블라인드 채용 코딩 테스트 오픈 채팅방 솔루션

    :param record: 채탕방 입장 로그
    :return: 이름이 바뀐 경우 바꾼 채팅방 최종 로그
    """
    name_dict = defaultdict(str)
    results = []
    answer = []

    for log in record:
        status = log.split()
        uid = status[1]

        if status[0] == "Enter":
            name = status[2]
            results.append((uid, "{}님이 들어왔습니다."))
            name_dict[uid] = name

        elif status[0] == "Leave":
            results.append((uid, "{}님이 나갔습니다."))

        elif status[0] == "Change":
            name = status[2]
            name_dict[uid] = name

    for result in results:
        uid, log = result
        answer.append(log.format(name_dict[uid]))

    return answer

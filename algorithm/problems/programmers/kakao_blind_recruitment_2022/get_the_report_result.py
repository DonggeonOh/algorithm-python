def solution(id_list, reports, k):
    """
    카카오 블라인드 채용 2022 코딩 테스트 신고 결과 받기 솔루션

    @Date: 2022/01/15
    @Author: Oh Donggeon
    @Link: https://programmers.co.kr/learn/courses/30/lessons/92334

    :param id_list: 신고자 아이디 리스트
    :param reports: 신고자와 제재자를 포함한 문자열 리스트
    :param k: 최소 신고 횟수 (이상 인 경우 제재)
    :return: 신고자가 신고한 아이디가 제재를 당한 횟수를 카운팅하여 리스트로 반환
    """
    report_list = [set() for _ in range(len(id_list))]
    report_count = [0 for _ in range(len(id_list))]
    isreported = [set() for _ in range(len(id_list))]

    answer = [0 for _ in range(len(id_list))]

    for report in reports:
        userid, reportedid = report.split()
        user_index = id_list.index(userid)
        report_index = id_list.index(reportedid)

        if reportedid not in isreported[user_index]:
            report_list[user_index].add(reportedid)
            isreported[user_index].add(reportedid)
            report_count[report_index] += 1

    for reported_index, count in enumerate(report_count):
        if count >= k:
            for index, reported_users in enumerate(report_list):
                if id_list[reported_index] in reported_users:
                    answer[index] += 1

    return answer

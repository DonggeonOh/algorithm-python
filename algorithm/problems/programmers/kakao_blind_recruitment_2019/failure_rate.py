def solution(max_stage, stages):
    """
    2019 카카오 블라인드 채용 코딩 테스트 솔루션

    @Date: 2022/01/20
    @Author: Oh Donggeon
    @Link: https://programmers.co.kr/learn/courses/30/lessons/42889
    """
    failure_rates = list()
    user_count = len(stages)
    answer = []

    for stage in range(1, max_stage + 1):
        if not user_count:
            for stage in range(stage, max_stage + 1):
                failure_rates.append((stage, 0))
            break

        failure_count = stages.count(stage)
        failure_rate = failure_count / user_count
        target_index = len(failure_rates)
        user_count -= failure_count

        for index, rate in enumerate(failure_rates):
            if rate[1] < failure_rate:
                target_index = index
                break

        failure_rates.insert(target_index, (stage, failure_rate))

    for stage, rate in failure_rates:
        answer.append(stage)

    return answer

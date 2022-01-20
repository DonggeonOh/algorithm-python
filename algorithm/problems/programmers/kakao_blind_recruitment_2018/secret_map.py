def solution(length, crypt_int1, crypt_int2):
    """
    2018 카카오 블라인드 채용 코딩 테스트 비밀 지도 솔루션

    :param length: 2차원 배열 N * M 에서 N, M 의 길이
    :param crypt_int1: 첫 번째 보물지도
    :param crypt_int2: 두 번째 보물지도
    :return: 2개의 보물지도를 겹쳐서 나온 보물지도 반환
    """
    answer = []

    for num1, num2 in zip(crypt_int1, crypt_int2):
        combined_num = str(bin(num1 | num2))[2:].zfill(length)
        converted_num = map(lambda element: "#" if element == "1" else " ", combined_num)
        answer.append("".join(converted_num))

    return answer

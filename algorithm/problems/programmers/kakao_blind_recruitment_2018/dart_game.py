def solution(result):
    scores = []
    temp_score = ""
    total_score = 0

    for score in result:
        if score.isdecimal():
            temp_score += score

        elif score == "S":
            scores.append(int(temp_score))
            temp_score = ""

        elif score == "D":
            scores.append(int(temp_score) ** 2)
            temp_score = ""

        elif score == "T":
            scores.append(int(temp_score) ** 3)
            temp_score = ""

        elif score == "*":
            scores[-1] *= 2

            if len(scores) >= 2:
                scores[-2] *= 2

        elif score == "#":
            scores[-1] *= -1

    for score in scores:
        total_score += score

    return total_score

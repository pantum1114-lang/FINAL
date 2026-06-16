# utils.py -- 매출 분석 함수 모음
#   (함수 이름과 매개변수는 바꾸지 마세요. 내용만 고치세요.)
#   ※ 각 함수가 정확히 어떻게 동작해야 하는지는 '문제지(정상 동작 명세)'를 따르세요.

# [수정] 정상 동작 명세서 5번 규칙의 수치(A=5.0, B=4.0, C=3.0, D=2.0, F=1.0)대로 수정
INCENTIVE_TABLE = {"A": 5.0, "B": 4.0, "C": 3.0, "D": 2.0, "F": 1.0}


def total_sales(branch):
    """지점 총매출."""
    return branch["1분기"] + branch["2분기"] + branch["3분기"]


def average_sales(branch):
    """지점 평균."""
    # [수정] len(branch)는 키 개수(4)를 반환하므로 명세서 3번 규칙(총매출/3)에 따라 명확히 3.0으로 나누도록 수정
    return total_sales(branch) / 3.0


def to_grade(avg):
    """평균을 등급으로 변환."""
    # [수정] 명세서 4번 규칙의 '이상'(같거나 큼) 조건에 부합하도록 비교 연산자 정의
    if avg >= 120:
        return "A"
    elif avg >= 100:
        return "B"
    elif avg >= 80:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def grade_to_incentive(grade):
    """등급을 성과급률로 변환."""
    return INCENTIVE_TABLE[grade]


def quarter_average(branches, quarter):
    """분기 평균."""
    total = 0
    for b in branches:
        # [수정] "1분기" 하드코딩을 제거하고 매개변수로 들어온 quarter 변수값을 대입하도록 수정
        total += b[quarter]
    return total / len(branches)


def quarter_top(branches, quarter):
    """분기 최고."""
    top = 0
    for b in branches:
        # [수정] 최고값을 갱신해야 하므로 비교 연산자의 부등호 방향을 > 로 수정
        if b[quarter] > top:
            top = b[quarter]
    return top


def grade_distribution(branches):
    """등급별 지점 수."""
    dist = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for b in branches:
        g = to_grade(average_sales(b))
        dist[g] += 1
    return dist


def rank_list(branches):
    """총매출 기준 정렬."""
    # [수정] 강의록 13번에 기술된 sorted() 방식에 따라, 총매출 높은 순(내림차순) 정렬을 위해 reverse=True 추가
    return sorted(branches, key=lambda x: total_sales(x), reverse=True)


def achievement_rate(branches, target=90):
    """목표 달성 비율(%)."""
    count = 0
    for b in branches:
        if average_sales(b) >= target:
            count += 1
    return count / len(branches) * 100
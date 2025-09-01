# 任務：grade(score):
# 分數 >=90 -> 'A', >=80 -> 'B', >=70 -> 'C', >=60 -> 'D', 否則 'F'

# TODO: 在此實作 grade

# 分數 >=90 -> 'A', >=80 -> 'B', >=70 -> 'C', >=60 -> 'D', 否則 'F'
def grade(score: int) -> str:
    if score>=90:
        return 'A'
    elif score>=80:
        return 'B'
    elif score>=70:
        return 'C'
    elif score>=60:
        return 'D'
    else:
        return 'F'

def level_up(experience: int, threshold: int, reward: int) -> bool:
    total_experience = experience + reward
    next_level = total_experience >= threshold
    return next_level


def motor_time(n: int) -> int:
    hours = n // 60
    minutes = n % 60
    str_hours = f"{hours:02}"
    str_minutes = f"{minutes:02}"
    str_time = str_hours+str_minutes
    sum_time = int(str_time[0]) + int(str_time[1]) + int(str_time[2]) + int(str_time[3])
    return sum_time


def time_converter(time_str: str) -> str:
    time = time_str.split(":")
    hours = int(time[0])
    day_time = int(time[0])-12
    night_time = int(time[0])+12
    if hours == 0:
        time_str = str(night_time) + ":" + time[1] + " a.m."
    if hours in range(1, 10):
        time_str = str(int(time[0])) + ":" + time[1] + " a.m."
    if hours == 11:
        time_str = time[0] + ":" + time[1] + " a.m."
    if hours == 12:
        time_str = time[0] + ":" + time[1] + " p.m."
    if hours > 12:
        time_str = str(day_time) + ":" + time[1] + " p.m."
    return time_str

def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    time = 0

    for Students, Students2 in permanence_period:
        if not isinstance(Students, int) or not isinstance(Students2, int):
            return None
        if Students <= target_time <= Students2:
            time += 1

    return time

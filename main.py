START_TIME = '09:00'
END_TIME = '21:00'
SLOT_TIME = 30  # minutes

busy = [
    {'start': '10:30', 'stop': '10:50'},
    {'start': '18:40', 'stop': '18:50'},
    {'start': '14:40', 'stop': '15:50'},
    {'start': '16:40', 'stop': '17:20'},
    {'start': '20:05', 'stop': '20:20'}
]


def time_to_minutes(time: str):
    """Converts time in format 'HH:MM' to minutes"""
    hour, minute = time.split(':')

    return int(hour) * 60 + int(minute)


def minutes_to_time(minutes: int):
    """Converts minutes to time in format 'HH:MM'"""
    hour = str(minutes // 60).zfill(2)
    minute = str(minutes % 60).zfill(2)

    return hour + ':' + minute


def get_free_slots(busy_slots: list):
    start = time_to_minutes(START_TIME)
    end_day = time_to_minutes(END_TIME)
    busy_sorted = sorted(busy_slots, key=lambda x: x['start'])
    free_slots = []
    i = 0  # pointer

    while start < end_day and i < len(busy_sorted):
        start_busy = time_to_minutes(busy_sorted[i]['start'])
        stop_busy = time_to_minutes(busy_sorted[i]['stop'])
        stop = start + SLOT_TIME

        if stop <= start_busy:
            free_slots.append({"start": minutes_to_time(start), "stop": minutes_to_time(stop)})
            start += SLOT_TIME
        elif start > stop_busy:
            i += 1
        else:
            start += SLOT_TIME
            if stop >= stop_busy:
                i += 1

    # Adding remaining time slots if start < end_day
    for start_time in range(start, end_day, SLOT_TIME):
        free_slots.append({"start": minutes_to_time(start_time), "stop": minutes_to_time(start_time + SLOT_TIME)})

    return free_slots


if __name__ == '__main__':
    for free_slot in get_free_slots(busy):
        print(free_slot)

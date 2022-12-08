# 1人あたりの待ち時間(分)
minute = {
    "curry" : 1,
    "noodle" : 0.5,
    "soba" : 0.5,
    "sagamiharaLunch" : 3,
    "teishoku" : 1,
    "aburasoba" : 2,
}

def calc(people_num, place):
    return str(int(people_num) * minute[place])

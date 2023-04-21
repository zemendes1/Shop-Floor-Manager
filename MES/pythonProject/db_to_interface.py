import db


def convert_string_facilities(input_str):
    num, P1, P2, P3, P4, P5, P6, P7, P8, P9, workTime = list(input_str)
    num = str(num)
    P1 = str(P1)
    P2 = str(P2)
    P3 = str(P3)
    P4 = str(P4)
    P5 = str(P5)
    P6 = str(P6)
    P7 = str(P7)
    P8 = str(P8)
    P9 = str(P9)
    workTime = str(workTime)
    return [{"num": num, "P1": P1, "P2": P2, "P3": P3, "P4": P4, "P5": P5, "P6": P6, "P7": P7, "P8": P8, "P9": P9,
             "workTime": workTime}]


def facilities(day):
    return convert_string_facilities(db.get_facility(day))


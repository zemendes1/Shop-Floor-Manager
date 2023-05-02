import db


def convert_string_facilities(input_str):
    values = list(map(str, input_str))
    result = {
        "num": values[0],
        "P1": values[1],
        "P2": values[2],
        "P3": values[3],
        "P4": values[4],
        "P5": values[5],
        "P6": values[6],
        "P7": values[7],
        "P8": values[8],
        "P9": values[9],
        "workTime": values[10],
        "Total": str(int(values[1]) + int(values[2]) + int(values[3]) + int(values[4]) + int(values[5]) + int(values[6]) + int(values[7]) + int(values[8]) + int(values[9]))
    }
    return result


def facilities(day):
    return_query = db.get_facility(day)
    if day is None:
        formatted_str = []
        for i in range(len(return_query)):
            if len(return_query) - i > 1:
                formatted_str.append(convert_string_facilities(return_query[i]))
            else:
                formatted_str.append(convert_string_facilities(return_query[i]))
        return formatted_str
    else:
        formatted_str = convert_string_facilities(return_query)
        return [formatted_str]


def convert_string_order(input_str):
    values = list(input_str)
    result = {
        "id": str(values[0]),
        "Client": str(values[1]),
        "OrderNumber": str(values[2]),
        "WorkPiece": str(values[3]),
        "Quantity": str(values[4]),
        "DueDate": str(values[5]),
        "Late_Penalty": str(values[6]),
        "Early_Penalty": str(values[7]),
        "path": str(values[8]),
        "status": str(values[9])
    }
    return result


def orders(identificacao):
    return_query = db.get_order(identificacao)
    if identificacao is None:
        formatted_str = []
        for i in range(len(return_query)):
            if len(return_query) - i > 1:
                formatted_str.append(convert_string_order(return_query[i]))
            else:
                formatted_str.append(convert_string_order(return_query[i]))
        return formatted_str
    else:
        formatted_str = convert_string_order(return_query)
        return [formatted_str]


def convert_string_dock(input_str):
    values = list(map(str, input_str))
    result = {
        "num": values[0],
        "P1": values[1],
        "P2": values[2],
        "P3": values[3],
        "P4": values[4],
        "P5": values[5],
        "P6": values[6],
        "P7": values[7],
        "P8": values[8],
        "P9": values[9],
        "Total": str(int(values[1]) + int(values[2]) + int(values[3]) + int(values[4]) + int(values[5]) + int(values[6]) + int(values[7]) + int(values[8]) + int(values[9]))
    }
    return result


def dock(num):
    return_query = db.get_dock(num)
    if num is None:
        formatted_str = []
        for i in range(len(return_query)):
            if len(return_query) - i > 1:
                formatted_str.append(convert_string_dock(return_query[i]))
            else:
                formatted_str.append(convert_string_dock(return_query[i]))
        return formatted_str
    else:
        formatted_str = convert_string_dock(return_query)
        return [formatted_str]


def convert_string_daily_plan(input_str):
    values = list(input_str)
    result = {
        "date": str(values[0]),
        "Purchase_orders": str(values[1]),
        "Delivery_orders": str(values[2]),
        "P1_toBuy": str(values[3]),
        "P2_toBuy": str(values[4])
    }
    return result


def daily_plan(date):
    return_query = db.get_daily_plan(date)
    if date is None:
        formatted_str = []
        for i in range(len(return_query)):
            if len(return_query) - i > 1:
                formatted_str.append(convert_string_daily_plan(return_query[i]))
            else:
                formatted_str.append(convert_string_daily_plan(return_query[i]))
        return formatted_str
    else:
        formatted_str = convert_string_daily_plan(return_query)
        return [formatted_str]

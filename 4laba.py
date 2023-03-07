def proc1(number: int):
    return True if number % 3 == 0 else False

def proc2(number):
    res = None
    try:
        res = 100 / float(number)
    except ValueError:
        print("Можно вводить только число")
    except ZeroDivisionError:
        print("На ноль делить нельзя")
    except Exception as e:
        print("Ошибка: ", e)
    return res

def proc3(date: str):
    try:
        date = date.split(".")
        if int(date[0]) * int(date[1]) == int(date[2][2:]):
            return True
        else:
            return False
    except:
        print("Дата вводится в формате dd.mm.yy")

def proc4(ticket: int):
    sum1 = 0
    sum2 = 0
    print(ticket)
    for i in range(6):
        if i < 3:
            sum1 += ticket // 10**i % 10
        else:
            sum2 += ticket // 10**i % 10
    if sum1 == sum2:
        return True
    else:
        return False



if __name__ == "__main__":

    print("Проверка функции деления на 3")
    print(proc1(20))
    print(proc1(21))

    print("Проверка функции деления 100")
    print(proc2("sdfdhs"))
    print(proc2(0))
    print(proc2(10))

    print("Проверка магической даты")
    print(proc3("10.02.2020"))
    print(proc3("11.02.2020"))

    print("Проверка счастливого билета")
    print(proc4(666666))
    print(proc4(232322))





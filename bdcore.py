import os

def getstartmenu(id):

    file="bd_mycashflow\\"
    file+=id
    file += ".txt"
    print(id)
    check_file = os.path.exists(file)
    if check_file:
        with open(file, "r") as f:
            for line in f:
                #formation retext
                print(line)
    else : retext="У вас нет CashFlow"
    return retext

def editcashflow(id,cashflow):
    file="bd_mycashflow\\"
    file+=id+"cashflow.txt"
    check_file = os.path.exists(file)
    if check_file == 0:
        path = "bd_mycashflow\\"
        path+=id
        try:
            os.mkdir(path)
        except OSError:
            print("Создать директорию %s не удалось" % path)
        else:
            print("Успешно создана директория %s " % path)
    with open(file, "w") as f:
        f.write(cashflow)
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

def getAccumulation(id):
    return "nonCard"

def editCashflow(id,cashflow):
    file="bd_mycashflow\\"
    file+=id+"\\cashflow.txt"
    check_file = os.path.exists(file)
    if check_file == 0:
        print("file not find")
        path = "bd_mycashflow\\"
        path+=id
        try:
            os.mkdir(path)
        except OSError:
            print("Создать директорию %s не удалось" % path)
        else:
            print("Успешно создана директория %s " % path)
    with open(file, "w") as f:
        f.write(str(cashflow))

class projectC:
    def __init__(self, name="", category="", description="", percent_complete=""):
        self.name = name
        self.category = category
        self.description = description
        self.percent_complete = percent_complete

def getAllprojects(id):
    file = "bd_mycashflow\\"
    file += id + "\\projects.txt"
    check_file = os.path.exists(file)
    if check_file == 0:
        retext="У вас нет проектов"
    else:
        projects = []
        i=0
        j=0
        projects[j] = projectC()
        with open(file, "r") as f:
            for line in f:
                match i:
                    case 0:
                        projects[j].name=line
                    case 1:
                        projects[j].category = line
                    case 2:
                        projects[j].description = line
                    case 3:
                        projects[j].cashflow = line
                    case 4:
                        projects[j].percent_complete=line
                if i>4:
                    i-=4
                    j+=1
                    projects[j]=projectC()
                i+=1
                #formation retext
                print(line)
    return 0

def editproject(id,number):
    a=1
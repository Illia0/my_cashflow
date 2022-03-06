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
    name=""
    category=""
    description=""
    percent_complete=""
    cashflow = ""
    def __init__(self):
        pass
        """,name,category,description,percent_complete
        self.name = name
        self.category = category
        self.description = description
        self.percent_complete = percent_complete"""

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
        projects.append(projectC())
        with open(file, "r") as f:
            for line in f:
                if i == 0:
                    projects[j].name = line
                elif i == 1:
                    projects[j].category = line
                elif i == 2:
                    projects[j].description = line
                elif i == 3:
                    projects[j].cashflow = line
                elif i == 4:
                    projects[j].percent_complete = line
                    i = -1
                    j += 1
                    projects.append(projectC())
                i += 1
        retext = ""
        for i in range(len(projects)-1):
            retext+=projects[i].name
            retext+="\nкатегория: "
            retext += projects[i].category
            retext += "\ncashflow: "
            retext += projects[i].cashflow
            retext += "грн/мес\nреализованость пректа: "
            retext += projects[i].percent_complete
            retext += "\n***********\n"

    return retext

def editproject(id,number):
    a=1
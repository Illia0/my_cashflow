import os

def getstartmenu(id):
    file="bd_mycashflow\\"
    file+=id
    file += "\\cashflow.txt"
    print(id)
    check_file = os.path.exists(file)
    if check_file:
        with open(file, "r") as f:
            for line in f:
                #formation retext
                retext="CashFlow: "+line+"грн/мес"
    else : retext="У вас нет CashFlow"
    return retext

def getAccumulation(id):
    return "nonCard"

def editCashflow(id,cashflow):
    file="bd_mycashflow\\"
    file+=id+"\\cashflow.txt"
    check_file = os.path.exists(file)
    if check_file == 0:
        print("file not find/create")
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

def getAllactvieprojects(id):
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
                    projects[j].description = line
                elif i == 2:
                    projects[j].category = line
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
            retext+="категория: "
            retext += projects[i].category
            retext += "cashflow: "
            retext += projects[i].cashflow.rstrip('\n')
            retext += "грн/мес\nреализованость пректа: "
            retext += projects[i].percent_complete
            retext += "\n***********\n"

    return retext

def buttonprojects(id):
    file = "bd_mycashflow\\"
    file += id + "\\projects.txt"
    check_file = os.path.exists(file)
    projects = []
    if check_file == 0:
        retext = "У вас нет проектов"
    else:
        i = 0
        with open(file, "r") as f:
            for line in f:
                if i == 0:
                    projects.append(line)
                elif i == 4:
                    i = -1
                i += 1
    return projects

def craetenewproject(id,proj):
    file = "bd_mycashflow\\"
    file += id + "\\newprojects.txt"
    check_file = os.path.exists(file)
    if check_file == 0:
        print("file not find/create")
        path = "bd_mycashflow\\"
        path += id
        try:
            os.mkdir(path)
        except OSError:
            print("Создать директорию %s не удалось" % path)
        else:
            print("Успешно создана директория %s " % path)
    with open(file, "a") as f:
        f.write(str(proj.name))
        f.write("\n")
        f.write(str(proj.description))
        f.write("\n")
        f.write(str(proj.category))
        f.write("\n")
        f.write(str(proj.cashflow))
        f.write("\n")
        f.write(str(proj.percent_complete))
        f.write("\n")
"""file = "bd_mycashflow\\"
file += id + "\\cashflow.txt"
check_file = os.path.exists(file)
if check_file == 0:
    print("file not find/create")
    path = "bd_mycashflow\\"
    path += id
    try:
        os.mkdir(path)
    except OSError:
        print("Создать директорию %s не удалось" % path)
    else:
        print("Успешно создана директория %s " % path)
with open(file, "r") as f:
    for line in f:
        cashflow=int(line)
    cashflow+=int(proj.cashflow)
with open(file, "w") as f:
    f.write(str(cashflow))
"""

def getAllnewprojects(id):
    file = "bd_mycashflow\\"
    file += id + "\\newprojects.txt"
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
                    projects[j].description = line
                elif i == 2:
                    projects[j].category = line
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
            retext+="категория: "
            retext += projects[i].category
            retext += "cashflow: "
            retext += projects[i].cashflow.rstrip('\n')
            retext += "грн/мес\nреализованость пректа: "
            retext += projects[i].percent_complete
            retext += "\n***********\n"

    return retext

def buttonnewprojects(id):
    file = "bd_mycashflow\\"
    file += id + "\\newprojects.txt"
    check_file = os.path.exists(file)
    projects = []
    if check_file == 0:
        retext = "У вас нет проектов"
    else:
        i = 0
        with open(file, "r") as f:
            for line in f:
                if i == 0:
                    projects.append(line)
                elif i == 4:
                    i = -1
                i += 1
    return projects

def getnewprdescription(id,name):
    file = "bd_mycashflow\\"
    file += id + "\\newprojects.txt"
    check_file = os.path.exists(file)
    if check_file == 0:
        errtext="user "+id+" get newprdecription but he's dont have folder"
        raise AssertionError(errtext)
    else:
        i = 0
        ff=False
        with open(file, "r") as f:
            for line in f:
                if i == 0 and line==name:
                    ff=True
                elif i == 1 and ff==True:
                    des = line
                    ff=False
                elif i == 4:
                    i = -1
                i += 1
    return des

def getnewprojectbyname(id,name):
    file = "bd_mycashflow\\"
    file += id + "\\projects.txt"
    check_file = os.path.exists(file)
    if check_file == 0:
        retext = "У вас нет проектов"
    else:
        project = projectC()
        i = 0
        ff = False
        with open(file, "r") as f:
            for line in f:
                if i == 0 and line == name:
                    ff = True
                    project.name = line
                elif i == 1 and ff == True:
                    project.description = line
                elif i == 2 and ff == True:
                    project.category = line
                elif i == 3 and ff == True:
                    project.cashflow = line
                elif i == 4 and ff == True:
                    project.percent_complete = line
                    i = -1
                    ff = False
                i += 1
        retext = ""
        retext += project.name
        retext += "категория: "
        retext += project.category
        retext += "cashflow: "
        retext += project.cashflow.rstrip('\n')
        retext += "грн/мес\nреализованость пректа: "
        retext += project.percent_complete
        retext += "\n***********\n"

    return retext
    a=1
def getnewprojectclassbyname(id, name):
    file = "bd_mycashflow\\"
    file += id + "\\newprojects.txt"
    check_file = os.path.exists(file)
    if check_file == 0:
        retext = "У вас нет проектов"
    else:
        project=projectC()
        i = 0
        ff=False
        with open(file, "r") as f:
            for line in f:
                if i == 0 and line == name:
                    ff=True
                    project.name = line
                elif i == 1 and ff==True:
                    project.description = line
                elif i == 2 and ff==True:
                    project.category = line
                elif i == 3 and ff==True:
                    project.cashflow = line
                elif i == 4 and ff==True:
                    project.percent_complete = line
                    i = -1
                    ff=False
                i += 1
    return project
def editproject(id,age,name,newp):
    a=1


def getdate():
    import datetime
    return datetime.datetime.now()
def log(HRS,ED):
    if HRS==1 and ED==1:
        var="["+str(getdate())+"]"+"\t"
        print("Which exercise you have done")
        var=var+input()+"\n"
        f=open("ha_ex","a")
        f.write(var)
        f.close()
    if HRS==2 and ED==1:
        var="["+str(getdate())+"]"+"\t"
        print("Which exercise you have done")
        var=var+input()+"\n"
        f=open("ro_ex","a")
        f.write(var)
        f.close()
    if HRS==3 and ED==1:
        var="["+str(getdate())+"]"+"\t"
        print("Which exercise you have done")
        var=var+input()+"\n"
        f=open("sp_ex","a")
        f.write(var)
        f.close()
    if HRS==1 and ED==2:
        var="["+str(getdate())+"]"+"\t"
        print("What have you eaten")
        var=var+input()+"\n"
        f=open("ha_di","a")
        f.write(var)
        f.close()
    if HRS==2 and ED==2:
        var="["+str(getdate())+"]"+"\t"
        print("What have you eaten")
        var=var+input()+"\n"
        f=open("ro_di","a")
        f.write(var)
        f.close()
    if HRS==3 and ED==2:
        var="["+str(getdate())+"]"+"\t"
        print("What have you eaten")
        var=var+input()+"\n"
        f=open("sp_di","a")
        f.write(var)
        f.close()
    return "Logged successfully"
def retrieve(HRS,ED):
    if HRS==1 and ED==1:
        f=open("ha_ex")
        print(f.read())
        f.close()
    if HRS==2 and ED==1:
        f=open("ro_ex")
        print(f.read())
        f.close()
    if HRS==3 and ED==1:
        f=open("sp_ex")
        print(f.read())
        f.close()
    if HRS==1 and ED==2:
        f=open("ha_di")
        print(f.read())
        f.close()
    if HRS==2 and ED==2:
        f=open("ro_di")
        print(f.read())
        f.close()
    if HRS==3 and ED==2:
        f=open("sp_di")
        print(f.read())
        f.close()
    return "Retrieved successfully"

print("Hello and welcome to my health management system")
    
while True:
    print("Enter your choice :","\n1 : Log\n2 : Retrieve\n3 : Quit")
    LR=int(input())
    if LR==3:
        exit()
    print("Which client ?")
    print("1 : Harry\n2 : Rohan\n3 : Sparsh")
    HRS=int(input())
    print("Enter choice")
    print("1 : Exercise\n2 : Diet")
    ED=int(input())
    if LR==1:
        print(log(HRS,ED))
    else:
        print(retrieve(HRS,ED))
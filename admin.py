# Admin Module
#======================================================
def admin1 (name) :
    #importing modules
    import os
    from time import sleep
    from prettytable import PrettyTable
    import mysql.connector as sql
    import pickle
    
    # sleep
    def wait(x):
        sleep(x)
        
    # clearing the output screen
    def clear():
        os.system('cls')
        for i in range (8):
            print()
            
    # function for indenting text to centre
    def print1():
        for ljk in range(20):
            print(" ",end=" ")

    #Establishing Mysql connection
    mycon= sql.connect(host="localhost",user="root",passwd="1234")
    if mycon.is_connected() == False:
        print1()
        print ("Some problem in connecting to database")
        exit()
    cs=mycon.cursor()
    
    #Functions
    #====================================================
    def add_class():
        print1()
        c1=input("Enter the class name : ")
        cs.execute("show databases")
        data=cs.fetchall()
        if (c1,) in data:
            print1()
            print("class already exists")
        else:
            f1=open("file5.dat","rb")
            d1=pickle.load(f1)
            f1.close()
            if c1 not in d1:
                print1()
                print("please assign subjects to class!")
                ctr=1
                cl1=[]
                while True:
                    print1()
                    tem=input("Enter sub"+str(ctr)+" : ")
                    cl1.append(tem)
                    ctr+=1
                    print1()
                    chh=input("Do you want to continue? y/n : ")
                    if chh!="y":
                        break
                print()
                print()
                print1()
                print("please add students to class!")
                ctr=1
                cl=[]
                while True:
                    print1()
                    tem=input("Enter student"+str(ctr)+" : ")
                    cl.append(tem)
                    ctr+=1
                    print1()
                    chh=input("Do you want to continue? y/n : ")
                    if chh!="y":
                        break
                d1[c1]=[cl1,cl]
                f1=open("file5.dat","wb")
                pickle.dump(d1,f1)
                f1.close()
            cs.execute("create database "+c1)
            print1()
            print(" class added")
            
    #====================================================
    def drop_class():
        cs.execute("show databases")
        data=cs.fetchall()
        print()
        print()
        for i in data:
            print1()
            print("  ",i[0])
        print()
        print1()
        c1=input("select any one of the above classes : ")  
        if (c1,) not in data:
            print1()
            print("class does not exists")
        else:
            cs.execute("drop database "+c1)
            f1=open("file5.dat","rb")
            d1=pickle.load(f1)
            f1.close()
            if c1 in d1:
                del d1[c1]
                f1=open("file5.dat","wb")
                pickle.dump(d1,f1)
                f1.close()
            f1=open("file3.dat","rb")
            d1=pickle.load(f1)
            f1.close()
            d={}
            for i in d1:
                dic=d1[i]
                if c1 in dic:
                    del dic[c1]
                if len(dic) !=0:
                    d[i]=dic
            f1=open("file3.dat","wb")
            pickle.dump(d,f1)
            f1.close()
            print1()
            print(" class removed")

    #====================================================
    def cpas(name):
        print1()
        npas=input("Enter your new password : ")
        import pickle
        f1=open("file1.dat","rb")
        data1=pickle.load(f1)
        data1[name]=npas
        f1.close()
        f1=open("file1.dat","wb")
        pickle.dump(data1,f1)
        print1()
        print("password changed successfully")

    #====================================================
    def add_teacher():
        f1=open("file3.dat","rb")
        d1=pickle.load(f1)
        f1.close()
        print1()
        name=input("Enter the teacher's name : ")
        if name not in d1:
            print1()
            pas=input("create a password : ")
            f1=open("file2.dat","rb")
            d2=pickle.load(f1)
            f1.close()
            d2[name]=pas
            f1=open("file2.dat","wb")
            pickle.dump(d2,f1)
            f1.close()
            f1=open("file5.dat","rb")
            d2=pickle.load(f1)
            f1.close()
            l2=d2.keys()
            print()
            d3={}
            while True:
                for i in l2:
                    if i not in d3:
                        print1()
                        print("  ",i)            
                print1()
                clas=input("Assign any one of the above classes : ")
                if clas not in l2 :
                    continue
                l3=[]
                while True:
                    for i in d2[clas][0] :
                        if i not in l3:
                            print1()
                            print("  ",i)
                    print1()
                    sub=input("assign any one of the above subjects : ")
                    if (sub not in d2[clas][0] )or( sub  in l3):
                        continue
                    l3.append(sub)
                    if len(l3)==len(d2[clas][0]):
                        break
                    print1()
                    ch4=input("Do you want to assign more subjects y/n : ")
                    if ch4 !="y":
                        break
                d3[clas]=l3
                print()
                if len(l2)==len(d3.keys()):
                    break
                print1()
                ch5=input("Do you want to assign more classes y/n : ")
                if ch5 !="y":
                    break
            d1[name]=d3
            f1=open("file3.dat","wb")
            pickle.dump(d1,f1)
            f1.close()
            print1()
            print("Teacher profile created")
        else:
            print1()
            print("Teacher already exists!!")

    #====================================================
    def drop_teacher():
            f1=open("file3.dat","rb")
            d1=pickle.load(f1)
            f1.close()
            l1=d1.keys()
            while True:
                print()
                if len(l1)==0:
                    print("no teachers found!!")
                    wait(2)
                    clear()
                    break
                for i in l1:
                    print1()
                    print("  ",i)
                print1()
                ch=input("Enter any one of the above teacher to remove : ")
                if ch not in l1:
                    continue
                if ch in d1:
                    del d1[ch]
                f1=open("file3.dat","wb")
                pickle.dump(d1,f1)
                f1.close()
                f1=open("file2.dat","rb")
                d1=pickle.load(f1)
                f1.close()
                if ch in d1:
                    del d1[ch]
                f1=open("file2.dat","wb")
                pickle.dump(d1,f1)
                f1.close()
                print1()
                print("Teacher profile removed")
                break

    #====================================================
    def add_student():
        while True:
            f1=open("file5.dat","rb")
            d1=pickle.load(f1)
            f1.close()
            l1=d1.keys()
            if len(l1)!=0:
                for i in l1:
                    print1()
                    print(i)
                print1()
                clas=input("Enter any one of the above classes : ")
                if clas not in l1:
                    continue
                while True:
                    print1()
                    name=input("enter student's name : ")
                    d1[clas][1].append(name)
                    print1()
                    ch=input("Do you want to add more students ? y/n : ")
                    if ch!="y":
                        break
                f1=open("file5.dat","wb")
                pickle.dump(d1,f1)
                f1.close()
                break    
            else:
                print1()
                print("No classes found")
                break

    #====================================================
    def drop_student():
        while True:
            f1=open("file5.dat","rb")
            d1=pickle.load(f1)
            f1.close()
            l1=d1.keys()
            if len(l1)!=0:
                for i in l1:
                    print1()
                    print(i)
                print1()
                clas=input("Enter any one of the above classes : ")
                if clas not in l1:
                    continue
                if len(d1[clas][1])>0:
                    while True:
                        for i in d1[clas][1]:
                            print1()
                            print (i)
                        print1()
                        name=input("enter student's name : ")
                        if i not in d1[clas][1] :
                            continue
                        d1[clas][1].remove(name)
                        print1()
                        ch=input("Do you want to remove more students ? y/n : ")
                        if ch!="y":
                            break
                    f1=open("file5.dat","wb")
                    pickle.dump(d1,f1)
                    f1.close()
                    break    
                else:
                    print1()
                    print("zero added students in the class ! ")
                    break
            else:
                print1()
                print("No classes found")
                break

    #====================================================
    def add_sub():
        while True:
            f1=open("file5.dat","rb")
            d1=pickle.load(f1)
            f1.close()
            l1=d1.keys()
            if len(l1)!=0:
                for i in l1:
                    print1()
                    print(i)
                print1()
                clas=input("Enter any one of the above classes : ")
                if clas not in l1:
                    continue
                while True:
                    print1()
                    sub=input("enter subject's name : ")
                    if sub not in d1[clas][0] :
                        d1[clas][0].append(sub)
                        print1()
                        ch=input("Do you want to add more subjects ? y/n : ")
                        if ch!="y":
                            f1=open("file5.dat","wb")
                            pickle.dump(d1,f1)
                            f1.close()
                            break
                    else:
                        print1()
                        print("Subject already exixts in class !")
                        continue
                break
            else:
                print1()
                print("No classes found")
                break

    #====================================================
    def drop_sub():
        while True:
            f1=open("file5.dat","rb")
            d1=pickle.load(f1)
            f1.close()
            l1=d1.keys()
            if len(l1)!=0:
                for i in l1:
                    print1()
                    print(i)
                print1()
                clas=input("Enter any one of the above classes : ")
                if clas not in l1:
                    continue
                if len(d1[clas][0])>0:
                    while True:
                        for i in d1[clas][0]:
                            print1()
                            print (i)
                        print1()
                        name=input("enter subject's name : ")
                        if i not in d1[clas][0] :
                            continue
                        d1[clas][0].remove(name)
                        print1()
                        ch=input("Do you want to remove more subjects ? y/n : ")
                        if ch!="y":
                            break
                    f1=open("file5.dat","wb")
                    pickle.dump(d1,f1)
                    f1.close()
                    break    
                else:
                    print1()
                    print("zero added subcts in the class ! ")
                    break
            else:
                print1()
                print("No classes found")
                break
            
    #====================================================
    def display_teacher():
        f1=open('file3.dat','rb')
        d1=pickle.load(f1)
        f1.close()
        k=list(d1.keys())
        for i in k:
            x=PrettyTable()
            x.title=i
            k1=list(d1[i].keys())
            for j in k1:
                for l in range(10-len(d1[i][j])):
                    d1[i][j].append(" ")
            for j in k1:
                x.add_column(j,d1[i][j])
            print(x)
            wait(1)

    #====================================================
    def display_clas():
        f1=open('file5.dat','rb')
        d1=pickle.load(f1)
        f1.close()
        k=list(d1.keys())
        for i in k:
            x=PrettyTable()
            x.title=i
            '''kkr=len(d1[i][1])-len(d1[i][0])
            if kkr>0:
                for j in range(kkr):
                    d1[i][0].append(" ")
            elif kkr<0:
                for j in range(abs(kkr)):
                    d1[i][1].append(" ")'''
            
            x.add_column("student's name",d1[i][1])
            for kk in range(len(d1[i][0])):
                xx=[]
                for ijj in range(len(d1[i][1])):
                    xx.append(str(d1[i][0][kk]))
                x.add_column('subject'+str(kk+1),xx)
            print(x)
            wait(1)

    #====================================================
    def reset():
        print1()
        ch=input("Are you sure you want to reset all records? y/n : ")
        if ch=="y":
            d={}
            f1=open("file2.dat","wb")
            pickle.dump(d,f1)
            f1.close()
            f1=open("file3.dat","wb")
            pickle.dump(d,f1)
            f1.close()
            f1=open("file4.dat","wb")
            from datetime import date
            today=date.today()
            d1 = today.strftime("%d_%m_%Y")
            dt=d1[3:5]
            pickle.dump(dt,f1)
            f1.close()
            f1=open("file5.dat","wb")
            pickle.dump(d,f1)
            f1.close()
            cs.execute("show databases")
            data=cs.fetchall()
            for i in data:
                try:
                    cs.execute("drop database "+i[0]+";")
                except:
                    continue
            print1()
            print("Reset Successful ")
            print1()
            print("All records deleted")
            print()
    #====================================================
    #main program start here
    print1()
    print("Admin Login successful")
    wait(2)
    clear()
    while True:
        print1()
        print("Select any one of the options below:")
        print1()
        print("1.Add an entity")
        print1()
        print("2.Remove an entity")
        print1()
        print("3.Display records")
        print1()
        print("4.Change password")
        print1()
        print("5.exit")
        print1()
        print("6.Reset all records")
        print1()
        choice=(input("Your choice is : "))
        clear()
        if choice=="1":
            print1()
            print("1. Add class ")
            print1()
            print("2. Add Teacher")
            print1()
            print("3. Add student")
            print1()
            print("4. Add subject")
            print1()
            ch3=(input("Your choice is : "))
            clear()
            if ch3=='1':
                add_class()
            elif ch3=='2':
                add_teacher()
            elif ch3=='3':
                add_student()
            elif ch3=='4':
                add_sub()
            wait(1)
            clear()
        elif choice=="2":
            print1()
            print("1. Remove class ")
            print1()
            print("2. Remove Teacher")
            print1()
            print("3. Remove student")
            print1()
            print("4. Remove subject")
            print1()
            ch3=(input("Your choice is : "))
            clear()
            if ch3=='1':
                drop_class()
            elif ch3=='2':
                drop_teacher()
            elif ch3=='3':
                drop_student()
            elif ch3=='4':
                drop_sub()
            wait(1)
            clear()
        elif choice=="3":
            print1()
            print("1. Display teacher details ")
            print1()
            print("2. Display class details")
            print1()
            ch3=(input("Your choice is : "))
            clear()
            if ch3=='1':
                display_teacher()
            elif ch3=='2':
                display_clas()
        elif choice=="4":
            cpas(name)
            wait(1)
            clear()
        elif choice=="5":
            mycon.close()
            exit()
        elif choice=="6":
            reset()
            wait(1)
            clear()
        continue
#----------End of admin module ---------------------------------------------------------


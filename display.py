#======================================================
#Display module for display in teacher module
def display():
    #importing modules
    import os
    from time import sleep
    import pickle
    import mysql.connector as sql
    from datetime import date
    from prettytable import PrettyTable

    #====================================================
    #Defining functions
    def wait(x):
        sleep(x)
    def clear():
        os.system('cls')
        for i in range(8):
            print()
    def print1():
        for ljk in range(20):
            print(" ",end=" ")

    #main program starts here-----------------------------------------------------------
    #connecting to database
    mycon= sql.connect(host="localhost",user="root",passwd="1234")
    if mycon.is_connected() == False:
        print1()
        print ("Some problem in connecting to database")
        exit()
    cs=mycon.cursor()
    f1=open("file5.dat",'rb')
    d1=pickle.load(f1)
    f1.close()
    d1=list(d1.keys())
    while True:
        if len (d1)==0:
            print1()
            print("no classes found")
            wait(2)
            clear()
            break
        for i in range(len(d1)):
            print1()
            print(i+1,". ",d1[i])
        print1()
        ch1=input("Enter your choice : ")
        clear()
        if int(ch1) not in range(1,len(d1)+1):
            continue
        ch1=d1[int(ch1)-1]
        cs.execute("use "+ch1)
        cs.execute("show tables;")
        d1=cs.fetchall()
        l0=['january','february','march','april','may','june','july','august','september','october','november','december']
        l=[]
        l2=[]
        l3=[]
        for i in d1:
            l.append(i[0])
        if len(l)==0:
            print1()
            print("no records found")
            wait(2)
            clear()
            break
        for i in l:
            if i in l0:
                l2.append(i)
            else:
                l3.append(i)
        while True:
            print1()
            print("1.Display previous month attendance")
            print1()
            print("2.Display current month attendance")
            print1()
            ch=input("Enter your choice : ")
            clear()
            if ch=='1':
                if len(l2)==0:
                    print1()
                    print("no reacords found")
                    wait(2)
                    clear()
                    break
                for i in range(len(l2)):
                    print1()
                    print(i+1,". ",l2[i])
                print1()
                ch2=input("Enter your choice : ")
                clear()
                if int(ch2) not in range(1,len(l2)+1):
                    continue
                ch2=l2[int(ch2)-1]
                cs.execute("desc "+ch2+";")
                data=cs.fetchall()
                data1=[]
                for i in data:
                    data1.append(i[0])
                x=PrettyTable(data1)
                cs.execute("select * from "+ch2+";")
                data=cs.fetchall()
                x.add_rows(data)
                print(x)
                wait(1.5)
                break
            elif ch=='2':
                if len(l3)==0:
                    print1()
                    print("no reacords found")
                    wait(2)
                    clear()
                    break
                for i in range(len(l3)):
                    print1()
                    print(i+1,". ",l3[i])
                print1()
                ch2=input("Enter your choice : ")
                clear()
                if int(ch2) not in range(1,len(l3)+1):
                    continue
                ch2=l3[int(ch2)-1]
                cs.execute("desc "+ch2+";")
                data=cs.fetchall()
                data1=[]
                for i in data:
                    data1.append(i[0])
                x=PrettyTable(data1)
                cs.execute("select * from "+ch2+";")
                data=cs.fetchall()
                x.add_rows(data)
                print(x)
                wait(1.5)
                break
            else:
                continue
        break
#Display module ends here--------------------------------------------------------------
                    
        

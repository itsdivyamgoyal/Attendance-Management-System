#======================================================
#Teacher module
def teacher(name):
    #importing modules
    import os
    from time import sleep
    import pickle
    import display as d
    import mysql.connector as sql
    from datetime import date

    #defining functions
    def wait(x):
        sleep(x)
    def clear():
        os.system('cls')
        for i in range(8):
            print()
    def print1():
        for ljk in range(20):
            print(" ",end=" ")

    #Establishing connection
    mycon= sql.connect(host="localhost",user="root",passwd="1234")
    if mycon.is_connected() == False:
        print1()
        print ("Some problem in connecting to database")
        exit()
    cs=mycon.cursor()
    
    #====================================================
    def attendance(name):
        import pickle
        try:
            d1=open("file3.dat","rb") 
            d2=pickle.load(d1)
        except EOFError:
            d1.close()
        if name in d2:
            l=d2[name]
            if len(l) !=0:
                l1=list(l.keys())
                for i in range (len(l)):
                    print1()
                    print(i+1," : ",l1[i])
                print1()
                ch1=int(input("select any one of these classes : "))
                try:
                    d1=open("file5.dat","rb") 
                    d2=pickle.load(d1)
                except EOFError:
                    d1.close()
                lt_sub=l[l1[ch1-1]]
                l_stu=d2[l1[ch1-1]][1]
                try:
                    d1=open("file5.dat","rb") 
                    d2=pickle.load(d1)
                except EOFError:
                    d1.close()
                l_sub=d2[l1[ch1-1]][0]
                cs.execute("use "+l1[ch1-1]+" ;")
                cs.execute("show tables ;")
                data=cs.fetchall()
                today=date.today()
                d1 = today.strftime("%d_%m_%Y")
                l1=[]
                for i in data:
                    l1.extend(list(i))
                if  d1 not in l1:
                    cmd="create table "+str(d1)+"  ("
                    cmd += "name char(30) ,"
                    for i in (l_sub):
                        cmd+= str(i) +" char(10) ,"
                    cmd=cmd[0:-2]
                    cmd +=") ;"
                    cs.execute(cmd)
                cs.execute("select * from "+d1+" ;")
                data=cs.fetchall()
                if len(data)>0:
                    d233=list(data[0])
                    d233.pop(0)
                    d33=list(l_sub)
                    for ill in range(len(d233)):
                        if d233[ill] !=None:
                            l_sub.remove(d33[ill])
                un_sub=[]
                for i in l_sub:
                    if i in lt_sub:
                        un_sub.append(i)
                if len(un_sub)>0:        
                    for i in range(len(un_sub)):
                        print1()
                        print(i+1,".",un_sub[i])
                    print1()
                    ch3=int(input("select any one of the above subjects : "))
                    sel_sub=un_sub[ch3-1]
                    if len(data)==0:
                        for i in l_stu:
                            print1()
                            ch4=input(i+" : ")
                            cs.execute("insert into "+d1+"(name,"+sel_sub+") value( '"+i+"' , '"+ch4+"' );")
                            mycon.commit()
                        print1()
                        print("Attendance Recorded")       
                    else:
                        for i in l_stu:
                            print1()
                            ch4=input(i+" : ")
                            cs.execute("update "+d1+" set "+sel_sub+"='"+ch4+"' where name= '"+i+"' ;")
                            mycon.commit()
                        print1()
                        print("Attendance recorded")
                else:
                    print1()
                    print("Attendance already recorded ")
            else:
                print1()
                print("class: ",l1[ch1-1]," does not exists")
        else:
            print1()
            print('no class assigned')
            
    #====================================================
    def cpas():
        print1()
        npas=input("Enter your new password : ")
        import pickle
        f1=open("file2.dat","rb")
        data1=pickle.load(f1)
        data1[name]=npas
        f1.close()
        f1=open("file2.dat","wb")
        pickle.dump(data1,f1)
        print1()
        print("password changed successfully")
        
    #====================================================
    #Indicating successful login
    print1()
    print ("Teacher login successful")
    wait(2)
    clear()

    #compiling previous month's attendance-----------------------------------------
    today=date.today()
    d1 = today.strftime("%d_%m_%Y")
    dt=d1[3:5]
    f1=open("file4.dat","rb")
    d5=pickle.load(f1)
    f1.close()
    if d5!=dt :
        l=[]
        month=['january','february','march','april','may','june','july','august','september','october','november','december']
        cs.execute("show databases;")
        d1=cs.fetchall()
        f1=open('file5.dat','rb')
        dd1=pickle.load(f1)
        f1.close()
        clas_list1=dd1.keys()
        while True:
            if len(d1)==0:
                break
            for i in d1:
                l.append(i[0])
            for i in l :
                if i in clas_list1:
                    dic={}
                    l2=[]
                    cs.execute("use "+i)
                    cs.execute("show tables;")
                    d1=cs.fetchall()
                    if len(d1)==0:
                        continue
                    for i in d1:
                        l2.append(i[0])
                    cs.execute("select * from "+l2[0]+";")
                    d1=cs.fetchall()
                    l3=[]
                    l4=[]
                    for i in d1:
                        l3.append(i[0])
                    for i in l3:
                        dic[i]=[]
                        dic[i].append(i)
                    for i in l2:
                        if i[3:5]==d5:
                           l4.append(i)
                    for i in l2:
                        if i[3:5]!=d5:
                            continue
                        cs.execute("select * from "+i+";")
                        d1=cs.fetchall()
                        for k in d1:
                            ctr=0
                            ttr=0
                            ssr='ab'
                            for j in k[1:]:
                                if j=='p' or j=='pp':
                                    ctr+=1
                                ttr+=1
                            if ctr>=ttr/2:
                                ssr='pp'
                            dic[(k[0])].append(ssr)
                    for i in dic.keys():
                        dic[i]=tuple(dic[i])
                    mont=month[int(d5)-1]
                    x="create table "+mont+"(name char(30),"
                    for i in l4:
                        x=x+i+" char(10),"
                    x=x[0:-1]
                    x+=");"
                    cs.execute(x)
                    for i in l3:
                        cs.execute("insert into "+mont+" values "+str(dic[i])+";")
                        mycon.commit()
                    for i in l4:
                        cs.execute("drop table "+i+";")
                        mycon.commit()
            break
        f1=open("file4.dat","wb")
        pickle.dump(dt,f1)
        f1.close()

    #====================================================
    #main program starts here
    while True:
        print1()
        print("select any one of the options below:")
        print1()
        print("1.Take Attendance")
        print1()
        print("2.Change password")
        print1()
        print("3.show attendace")
        print1()
        print("4.Exit")
        print1()
        choice=input("Enter your choice : ")
        clear()
        if choice=="1":
            attendance(name)
            wait(1)
            clear()
        elif choice=="2":
            cpas()
            wait(1)
            clear()
        elif choice=='3':
            d.display()
        elif choice=="4":
            mycon.close()
            exit()
        continue
#Teacher module ends here-------------------------------------------------------------
            

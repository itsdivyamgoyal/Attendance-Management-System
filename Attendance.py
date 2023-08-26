#======================================================
#main parent program
#importing all modules
import teacher as t
import admin as a
import pickle
import getpass_ak
import os
from time import sleep

#======================================================
#Defining functions
def print1():
    for ljk in range(20):
        print(" ",end=" ")
def wait(x):
    sleep(x)
def clear():
    os.system('cls')
    for i in range(8):
        print()
        
#======================================================
#main program starts here
for i in range (8):
        print()
print("                                            Welcome to Attendance sytsem")
print("                                                     -Designed by Divyam Goyal")
wait(2.5)
clear()
while True:
    print("                                            Welcome to Attendance sytsem")
    print("                                                     -Designed by Divyam Goyal")
    for i in range (6):
        print()
    #validating login details
    print1()
    print("1.Admin Login")
    print1()
    print("2.Teachers Login")
    print1()
    print("3.Exit")
    print1()
    ch=input("Enter your choice : ")
    print1()
    name =input("Enter your name : ")
    pas=(getpass_ak.getpass((20*"  ")+'Enter your password: '))
    if ch=="1":
        f1=open("file1.dat","rb")
        d1=pickle.load(f1)
        f1.close()
        if name in d1:
            if pas==d1[name]:
                clear()
                a.admin1(name)
            else:
                print1()
                print("Invalid name or password")
        else:
            print1()
            print("Invalid name or password")
    elif ch=="2":
        f1=open("file2.dat","rb")
        d1=pickle.load(f1)
        f1.close()
        if name in d1:
            if pas==d1[name]:
                clear()
                t.teacher(name)
            else:
                print1()
                print("Invalid name or password")
        else:
            print1()
            print("Invalid name or password")
    elif ch=='3':
        exit()
    wait(1)
    clear()
    continue
#------------End of main program--------------------------------------------------------

from pickle import dump,load
f1=open('file1.dat','rb')
d1=load(f1)
print (d1)
f1.close()
f1=open('file2.dat','rb')
d1=load(f1)
print (d1)
f1.close()
f1=open('file3.dat','rb')
d1=load(f1)
print (d1)
f1.close()
f1=open('file4.dat','rb')
d1=load(f1)
print (d1)
f1.close()
f1=open('file5.dat','rb')
d1=load(f1)
print (d1)
f1.close()
input()

import os

x=os.getcwd()
print(x)
os.chdir(os.pardir)  #parent directory

print(os.getcwd())

os.chdir(x)
print(os.getcwd())
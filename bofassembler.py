import os

ext = input("C/CPP: ")
arch = input("32/64: ")
prog = input("NAME: ")
out = input("OUT: ")
comp = ""

if ext == "c":
    comp = "gcc"
elif ext == "cpp":
    comp = "g++"

cmd = comp + " -m" + arch + " " + prog + " -o " + out + " -fno-stack-protector " 
print(cmd)
os.system(cmd)
import os
import shutil
#print(os.system('date'))
#os.mkdir("/Users/rishi/OneDrive/Desktop/c99")
#print(os.getcwd())
#print(os.path.exists("/Users/rishi/OneDr/Desktop"))
#print(os.path.splitext("/Users/rishi/OneDrive/Desktop/WhiteHatJR/Python-WhiteHAtjr/c97/dict.py"))
src=input('ENTER SOURCE: ')
des=input('FILE DESTINATION: ')
src=src+"/"
des=des+'/'
file=os.listdir(src)
for i in file:
    shutil.copy((src+i),des)

import os
os.chdir('D:\\python\\AI\\sources\\Day - 12\\Code\\Datasets\\val\\kamal\\')
i=1
for file in os.listdir():
    src=file
    dst="kamal"+"_"+str(i)+".jpg"
    os.rename(src,dst)
    i+=1


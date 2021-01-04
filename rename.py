import os
os.chdir('D:\\python\\Datasets')        # please give the correct directory of the folder
i=1
for file in os.listdir():
    src=file
    dst="Rajini"+"_"+str(i)+".jpg"      # name with extension
    os.rename(src,dst)
    i+=1

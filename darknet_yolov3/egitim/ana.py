import os

list = sorted(os.listdir("resimler"),key=len)
files_txt = [i for i in list if i.endswith('.jpg')]
egitim=""
test=""
i=0
c=0
for l in files_txt:
   if i%5==1 and c<35:
      test = test + "egitim/resimler/" + l + "\n"
      c=c+1
   else:
      egitim=egitim+"egitim/resimler/"+l +"\n"
   i=i+1

f = open("egitim.txt", "a")
f.write(egitim)
f = open("test.txt", "a")
f.write(test)
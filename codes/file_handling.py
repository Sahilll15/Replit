with open('new.txt','w') as file:
  file.write("new file")

with open('new.txt','r') as file:
  print(file.read())

import os 

if os.path.exists('neww.txt'):
  print("exitst")
else:
  print("Does not exist")

with open('sahil.txt','w') as file:
  file.write("i am sahil chalke")
  
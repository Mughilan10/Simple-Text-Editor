# importing the ADT
from texteditor_ADT import texteditor
# function to perform the requested operations
def cmd():
  te=texteditor()
  while True:
    cmd=input(">>")
    cmd=cmd.split()
    if(cmd==[]):
      pass
    elif (cmd[0]=='i' or cmd[0]=='i'):
      if (len(cmd[1])==1):
        te.insert(cmd[1])
      else:
        print('Can insert only one character.... ')
    elif (cmd[0]=='p' or cmd[0]=='P'):
      te.printL()
    elif (cmd[0]=='l' or cmd[0]=='L'):
      te.left()
    elif (cmd[0]=='r' or cmd[0]=='R'):
      te.right()
    elif (cmd[0]=='d' or cmd[0]=='D'):
      te.delete()
    elif (cmd[0]=='x' or cmd[0]=='X'):
      exit()
    elif (cmd[0]=='s' or cmd[0]=='S'):
      if len(cmd)==1:
        te.save()
        print('File saved in *.txt')
      elif len(cmd)==2:
        te.save(str(cmd[1]))
    elif (cmd[0]=='o' or cmd[0]=='O'):
      if len(cmd)==1:
        print('Opening file *.txt')
        te.get()
      elif len(cmd)==2:
        print(f'Opening file {str(cmd[1])}')
        te.get(str(cmd[1]))
    elif (cmd[0]=='h' or cmd[0]=='H'):
      if len(cmd)==1:
        te.help()
    else:
      print("Wrong command !!!")
      print('Try using "h or H" for help')
cmd()
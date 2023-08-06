# Contents of texteditor_ADT.py

import os
# Node of the doubly linked list
class Node:
  def __init__(self,val,prev=None,next=None):
    self.val=val
    self.prev=prev
    self.next=next

# Body of text editor ADT
class texteditor:
  # initializing cursor
  def __init__(self):
    self.head=Node('|')
  # method insert
  def insert(self,data):
    newNode=Node(data)
    # If the dll is empty
    if self.head.val=='|':
      newNode.next=self.head
      newNode.prev=None
      self.head.prev=newNode
      self.head=newNode
    # if the dll is not empty
    else:
      temp=self.head
      while(temp.next.val!='|'):
        temp=temp.next
      temp2=temp.next
      newNode.next=temp.next
      newNode.prev=temp
      temp2.prev=newNode
      temp.next=newNode
  # function to move the cursor to the left
  def left(self):
    temp=self.head
    while(temp.val!='|'):
      temp=temp.next
    # if there is no entry to the left of the cursor
    if temp.prev==None:
      pass
    # if the left side of the cursor is not empty
    else:
      temp2=temp.prev
      temp2.val,temp.val=temp.val,temp2.val
  # function to move the cursor to the right
  def right(self):
    temp=self.head
    while(temp.val!='|'):
      temp=temp.next
    # if there is no entry to the right of the cursor
    if temp.next==None:
      pass
    # if the right side of the cursor is not empty
    else:
      temp2=temp.next 
      temp2.val,temp.val=temp.val,temp2.val
  # function to delete the character to the right of the cursor
  def delete(self):
    temp=self.head
    while(temp.val!='|'):
      temp=temp.next
    # if there is no entry to the right of the cursor
    if temp.next==None:
      pass
    # if there is entry to the right of the cursor
    else:
      # if there is only one entry to the right of the cursor
      if temp.next.next==None:
        temp2=temp.next
        temp2.prev=None
        temp.next=None
      # if there is more than one entry to the right of the cursor
      else:
        temp2=temp.next
        temp.next=temp2.next
        temp2=temp2.next
        temp2.prev=temp

  # function to print the dll
  def printL(self):
    temp=self.head
    while temp:
      print(temp.val,end='')
      temp=temp.next
    print()
  # function to save the dll in .txt file
  def save(self,file="*.txt"):
    f=open(file,"wt")
    s=[]
    strin=""
    temp=self.head
    while temp:
      if temp.val!='|':
        s.append(temp.val)
        temp=temp.next
      else:
        temp=temp.next
    strin=strin.join(s)
    f.write(strin)
    f.close()
  # function to open the requested .txt file
  def get(self,file="*.txt"):
    if os.path.isfile(file):
      print('File Opened...')
      f=open(file,"rt")
      strin=f.read()
      self.head=Node('|')
      temp=self.head
      for s in strin:
        newNode=Node(s)
        temp.next=newNode
        newNode.prev=temp
        temp=temp.next
      f.close()
    else:
      print('File doesnt exists!!!')
  # legend to assist the user with the keys corresponding to specific operations
  def help(self):
    print('"i <char> or I <char>" to insert a character before the cursor')
    print('"l or L" to move the cursor to left')
    print('"r or R" to move the cursor to right')
    print('"d or D" to delete the character after the cursor')
    print('"p or P" to print the values in the text editor')
    print('"s <filename> or S <filename>"" to save the text to the file <filename> or it saves in the file *.txt if <filename> argument is not present')
    print('"o <filename> or O <filename>"" to open the text in file <filename> or it opens the file *.txt if <filename> argument is not present')
    print('"x or X" to close the text editor')
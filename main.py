#!/usr/bin/env python


import datetime
import hashlib
import os

entries = []

global currentUname
global currentPass

currentUname = open("uname.txt")
currentPass = open("pass.txt")

class entry():
  
  def __init__(self, title,date,snote):
    self.title = title
    self.date = date
    self.note = []
    self.note += snote
  

  
def intro():
  print("Welcome to the super secure Password Manager")

def writeNote():
  date = datetime.datetime.now()
  print("please enter the title of the note\n")
  WN_Title=input()
  if(len(WN_Title) ==0):
    WN_Title = "Untitled " + str(date.month) + str(date.year)
  print(WN_Title)
  lines=[]
  while(True):
    line=input()
    if line:
      lines.append(line)
    else:
      break
  text='\n'.join(lines)
  newNote = entry(WN_Title,datetime.datetime.now(),lines)
  entries.append(newNote)


def changePass():
    selection = input("Do you want to change your username or password? 1 for Username, 2 for Password.\n")
    if selection.isdigit():
        sel = int(selection)
        if sel == 1:
            newUname = input("enter a new username\n")
            if hashlib.sha256(newUname.encode()).hexdigest() != currentUname.read():
                file = open('uname.txt', 'w')
                file.write(hashlib.sha256((newUname).encode()).hexdigest())
                file.close()
                print("Done, your new username is: " + newUname)
        elif sel == 2:
            newPass = input("enter a new password\n")
            if hashlib.sha256(newPass.encode()).hexdigest() != currentPass.read():
                file = open('pass.txt', 'w')
                file.write(hashlib.sha256((newPass).encode()).hexdigest())
                file.close()
                print("Done, your new password is: " + newPass)
        else:
            print("invalid: try again")
            changePass()
    else:
        print("invalid: try again")
        changePass()

    menu()

    


def menu():
  exit = True
  while(exit):
    print("Choose:")
    print("1.Read Notes")
    print("2.Write Note")
    print("3. Change Username/Password")
    selection = input("Number Option")
    if(selection.isdigit()):
      selection=int(selection)
      if selection == 1:
        print("you've selected to read Notes")
        if(len(entries)>0):
          print("which entry would you like to read?")
          num = 0
          for each in entries:
            num+=1
            print (num,'.',each.title)
          while(True):
            selection=int(input())
            selection-=1
            print ("You selected ",selection)
            if(selection<len(entries)):
              print (entries[selection].title," written on ", entries[selection].date.strftime("%c"))
              lines = entries[selection].note
              for line in lines:
                print (line)
              break
        else: print ("No notes stored")
      if selection == 2:
        writeNote()
      elif selection == 3:
          changePass()
      

def authenticate():
  Uname = input("Please Enter User Name\n")    
  PassWord = input("Please Enter User Password\n")  
  UnameEncrypt = hashlib.sha256(Uname.encode()).hexdigest()
  PassEncrypt = hashlib.sha256(PassWord.encode()).hexdigest()
  if UnameEncrypt == currentUname.read() and PassEncrypt == currentPass.read():
    print("entered")
    return True

while(True):
 
  if(authenticate()):
    break

intro()
menu()

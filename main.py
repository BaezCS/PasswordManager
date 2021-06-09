#!/usr/bin/env python


import datetime

entries = []


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



def menu():
  exit = True
  while(exit):
    print("Choose:")
    print("1.Read Notes")
    print("2.Write Note")
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
      

def authenticate():
  Uname = input("Please Enter User Name\n")    
  PassWord = input("Please Enter User Password\n")  
  Uname = Uname+PassWord
  UnameAscciiSum = 0
  for letter in Uname:
    UnameAscciiSum+=ord(letter)  
  if UnameAscciiSum > 1200 and Uname[0] == "a":
    print(UnameAscciiSum) 
    return True

while(True):
 
  if(authenticate()):
    break

intro()
menu()

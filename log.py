#Author By : MR.CL4Y [Muhammad Rafli]
from getpass import getpass
import os
import time

def menu():
      while True:
           print("")
           os.system("clear")
           print('\033[1;36;40m|-----[▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊]-----|')
           print("\033[1;93m")
           print("\033[1;93m")
           print("       <──────────[ SELAMAT DATANG‌ ]──────────>")
           print("")
           print("       Jika kalian tidak tahu user dan passwordnya kalian bisa hubungi nomor di bawah ini : ")
           print("        Contact wa : 0857-5248-1601 ")
           print("")
           try:
                x = str(input('\033[1;92mUsername \033[1;93m: '))
                print("")
                o = input("Are You Want To Show You Password [ y/n ] : ")
                print("")
                if o =="y":
                     e = input('\033[1;92mPassword \033[1;93m: ')
                if o =="n":
                     e = getpass('\033[1;92mPassword \033[1;93m: ')
                print ("")
                if x=="Muhammad" and e=="Rafli":
                   print('Loading...')
                   time.sleep(1)
                   os.system('clear')
                   print('')
                   os.system('figlet ' + x + ' | lolcat')
                   print('\033[1;92m࿇======═════━━━━ᗘ WELCOME ᗛ━━━━═════=======࿇')
                   print("")
                   break
                else:
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Wrong Password")
                      time.sleep(2)
                      print("")
           except Exception:
                      print("")
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Wrong Password")
                      time.sleep(2)
           except KeyboardInterrupt:
                      print("")
                      os.system('apt update && apt upgrade')
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     Wrong Password")
                      time.sleep(2)
                      os.system('sh itool.sh ')
menu()


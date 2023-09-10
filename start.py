    #!/usr/bin/python
import os
from googlesearch import search

red = '\033[91m'
yellow= '\33[93m'
green = '\033[1;32m'
white = '\033[97m'
blue = '\033[94m'
lightblue = '\033[94m'
GREEN = '\033[92m'
cyan = "\033[96m"
end = '\033[0m'
		
logo = """ 
     \033[97m╔════════════════════════════════╗
     \033[97m║   \033[92m╔══════╗ ╔══════╗ ╔══════╗   \033[97m║
     \033[97m║   \033[92m║      ║ ║      ╩ ║      ╩   \033[97m║
     \033[97m║   \033[92m╠══════╝ ║        ║     ═╦   \033[97m║ 
     \033[97m║   \033[92m║        ║      ╦ ║      ║   \033[97m║
     \033[97m║   \033[92m╩        ╚══════╝ ╚══════╝   \033[97m║
     \033[97m╚══════════════╗ ╔═══════════════╝
       \033[97m║ \033[91mDEVELOPER  \033[97m║ \033[97m║ \033[91mJOHN EX DEV \033[97m║ 
       \033[97m╚════════════╝ ╚═════════════╝
     \033[97m╔══════════════╝ ╚═══════════════╗
         \033[93mPLATOON CYBER GROUP TOOLKIT
      \033[97m╚═════════════╗ ╔══════════════╝  
  \033[97m╔═════════════════╝ ╚══════════════════╗
  \033[97m║ \033[96mNAME: \033[94mAUTO DORK      \033[96mTOOL: \033[94mPRIVATE   \033[97m║
  \033[97m║ \033[96mVERSION: \033[94m2           \033[96mENGINE: \033[94mGOOGLE  \033[97m║
  \033[97m║                                      \033[97m║
  \033[97m╚══════════════════════════════════════╝  
"""
os.system("clear")
print(blue+logo)

googledork = str(input("\033[1;31m[ \033[1;32mENTER YOUR DORK! \033[1;31m]\033[94m═══>> \033[1;36m"))
countingnum = int(input("\033[1;31m[ \033[1;32mNUMBER OF SITES! \033[1;31m]\033[94m═══>> \033[1;36m"))

if googledork == "":
        exit()
if countingnum == "":
        exit()

print("")
count = 0
for url in search(googledork,num=countingnum,start=0,stop=None,pause=2):
        print(f"\033[1;32m{url}")
        if count == countingnum:
                exit()
        count = count + 1
        
        
        
        
        
        
        
        
        
        
        
        
                    

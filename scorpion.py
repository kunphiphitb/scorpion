#Make in Python2
#Make by Zero

import os, sys, time
from time import sleep as timeout
def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()

#banner

os.system("figlet scorpion")
print "Install all Tools Hacking"
print
print "[01]> HPAS1369      [02]> Pntddos"
print "[03]> Optiva        [04]> Metasploit"
print "[05]> Spammer-grab  [06]> A-Rat"
print "[07]> SQLMap        [08]> Vbug"
print "[09]> RedHawk       [10]> FB brute"
print "[11]> Black Hydra   [12]> Youtube"
print "[13]> Weeman        [14]> WebSploit"
print "[15]> Xerxes        [16]> RouterSploit"
print "[17]> Ubuntu-Termux [18]> Kali-Termux"
print "[19]> Emalibomb     [20]> DosThunber"
print "[21]> Hammer        [22]> Social Fish"
print "[23]> santet-online [24]> Xshell"
print
print "[99]> Credit Creator"
print "[00]> Exit"
print
A = raw_input("instsll : ")


def hpas():
	os.system("apt-get upgrade -y && apt-get update -y")
	os.system("apt-get install git -y")
	os.system("apt-get install hydra -y")
	os.system("apt-get install python python2 -y")
	os.system("git clone https://github.com/DedSecCyber/HPAS1369.git")
	os.system("cp -rf HPAS1369 ~")
	os.system("rm -rf HPAS1369")

def pntddos():
	os.system("apt-get upgrade -y && apt-get update -y")
	os.system("apt-get install git -y")
	os.system("apt-get install python python2 -y")
	os.system("git clone https://github.com/Hydra7/Planetwork-DDOS.git")
	os.system("cp -rf Planetwork-DDOS ~")
	os.system("rm -rf Planetwork-DDOS")

def optiva():
	os.system("apt-get upgrade -y && apt-get update -y")
	os.system("apt-get install git -y")
	os.system("apt-get install python python2 -y")
	os.system("git clone https://github.com/joker25000/Optiva-Framework.git")
	os.system("cp -rf Optiva-Framework ~")
	os.system("rm -rf Optiva-Framework")
	os.system("cd Optiva-Framework")
	os.system("bash installer.sh")
	os.system("cd ~/scorpion")
	
def metasploit():
	os.system("apt-get upgrade -y && apt-get update -y")
	os.system("apt-get install curl -y")
	os.system("curl -LO https://raw.githubusercontent.com/Hax4us/Metasploit_termux/master/metasploit.sh")
	os.system("cd ~")
	os.system("sh metasploit.sh")
	
def spammer():
	os.system("apt-get upgrade -y && apt-get update -y")
	os.system("apt-get install git -y")
	os.system("apt-get install python python2 -y")
	os.system("git clone https://github.com/Noxturnix/Spammer-Grab.git")
	os.system("cp -rf Spammer-Grab ~")
	os.system("rm -rf Spammer-Grab")
	os.system("pip2 install requests")

def arat():
	os.system("apt-get upgrade -y && apt-get update -y")
	os.system("apt-get install git -y")
	os.system("apt-get install python python2 -y")
	os.system("git clone https://github.com/Xi4u7/A-Rat")
	os.system("cp -rf A-Rat ~")
	os.system("rm -rf A-Rat")

def sqlmap():
	os.system("apt-get upgrade -y && apt-get update -y")
	os.system("apt-gt install git")
	os.system("apt-get install python python2 -y")
	os.system("git clone https://github.com/sqlmapproject/sqlmap")
	os.system("cp -rf sqlmap ~")
	os.system("rm -rf sqlmap")
	
def vbug():
	os.system("apt-get upgrade -y && apt-get update -y")
	os.system("apt-get install git wget -y")
	os.system("apt-get install python python2 -y")
	os.system("git clone https://github.com/jota01234/Vbug.git")
	os.system("cp -rf Vbug ~")
	os.system("rm -rf Vbug")
	
def redhawk():
	os.system("apt-get upgrade -y && apt-get update -y")
	os.system("apt-get install git -y")
	os.system("apt-get install php -y")
	os.system("git clone https://github.com/Tuhinshubhra/RED_HAWK.git")
	os.system("cp -rf RED_HAWK ~ ")
	os.system("rm -rf RED_HAWK")
	
def facebook():
	os.system('apt update && apt upgrade')
	os.system('apt install python2 wget')
	os.system('pip2 install mechanize')
	os.system('mkdir ~/facebook-brute')
	os.system('wget http://override.waper.co/files/facebook.apk')
	os.system('wget http://override.waper.co/files/password.apk')
	os.system("mv facebook.apk ~/facebook-brute/facebook.py;mv password.apk ~/facebook-brute/facebook.py")
	
def youtube():
	os.system("apt-get upgrade -y && apt-get update -y")
	os.system("apt-get install git python -y")
	os.system("git clone https://github.com/FewHakko/Youtube-Sub---Like")
	os.system("cp -rf Youtube-Sub---Like ~")
	os.system("rm -rf Youtube-Sub---Like")
	
def weeman():
	os.system("apt-get upgrade -y apt-get update -y")
	os.system("apt-get install git python2 -y")
	os.system("git clone https://github.com/evait-security/weeman.git")
	os.system("cp -rf weeman ~")
	os.system("rm -rf weeman")
	
def websploit():
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('pip2 install scapy')
	os.system('git clone https://github.com/The404Hacking/websploit')
	os.system("cp -rf websploit ~")
	os.system("rm -rf websploit")
	
def xerxes():
	os.system('apt update && apt upgrade')
	os.system('apt install git')
	os.system('apt install clang')
	os.system('git clone https://github.com/zanyarjamal/xerxes')
	os.system('mv xerxes ~')
	os.system('cd ~/xerxes && clang xerxes.c -o xerxes')
	
def routersploit():
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('pip2 install requests')
	os.system('git clone https://github.com/reverse-shell/routersploit')
	os.system('mv routersploit ~;cd ~/routersploit;pip2 install -r requirements.txt;termux-fix-shebang rsf.py')
	
def blackhydra():
	os.system("apt-get upgrade -y && apt-get update -y")
	os.system("apt-get install git -y")
	os.system("apt-get install python python2 -y")
	os.system("apt-get install hydra -y")
	os.system("git clone https://github.com/Gameye98/Black-Hydra.git")
	os.system("mv -rf Black-Hydra ~")
	
def ubuntu():
	os.system("apt-get upgrade -y && apt-get update -y")
	os.system("apt-get install git -y")
	os.system("apt-get install python python2 -y")
	os.system("git clone https://github.com/Neo-Oli/termux-ubuntu.git")
	os.system("mv termux-ubuntu ~")
	os.system("cd ~/termux-ubuntu && ./ubuntu.sh")
	
def kali():
	os.system("apt-get upgrade -y && apt-get update -y")
	os.system("apt-get install git -y")
	os.system("git clone https://github.com/Hax4us/Nethunter-In-Termux.git")
	os.system("cp -rf  Nethunter-In-Termux ~ && rm -rf Nethunter-In-Termux")
	os.system("cd ~/Nethunter-In-Termux && ./kalinethunter")
	
def emailbomb():
	os.system("apt-get upgrade -y && apt-get update -y")
	os.system("apt-get install git python2 -y")
	os.system("git clone https://github.com/Ha3MrX/Emailbomb.git")
	os.system("mv Emailbomb ~")
	
def dost():
	os.system("apt-get upgrade -y && apt-get update -y")
	os.system("apt-get install python2 -y")
	os.system("git clone https://github.com/DedSecCyber/DosThunder.git")
	os.system("mv DosThunder ~")

def hammer():
	os.system("apt-get upgrade -y && apt-get update -y")
	os.system("apt-get install git python -y")
	os.system("git clone https://github.com/cyweb/hammer.git")
	os.system("mv hammer ~")
	os.system("chmod 7 ~/hammer.py")
	
def social():
	os.system("apt-get upgrade -y && apt-get update -y")
	os.system("apt-get install git python -y")
	os.system(" git clone https://github.com/UndeadSec/SocialFish.git")
	os.system("mv SocialFish ~")
	os.system("cd ~/SocialFish")
	os.system("pip install -r requirements.txt")

def santet():
        os.system("apt-get upgrade -y && apt-get update -y")
        os.system("apt-get install python python2 git")
        os.system("git clone https://github.com/Gameye98/santet-online.git")
        os.system("mv santet-online ~")

def xshell():
        os.system("apt-get upgrade -y && apt-get update -y")
        os.system("apt install lynx python2 figlet ruby php nano w3m")
        os.system("git clone https://github.com/Ubaii/Xshell")
        os.system("mv Xshell ~")

#options

if A == "1" or A == "01":
	hpas()

elif A == "2" or A == "02":
	pntddos()

elif A == "3" or A == "03":
	optiva()

elif A == "4" or A == "04":
	metasploit()

elif A == "5" or A == "05":
	spammer()

elif A == "6" or A == "06":
	arat()

elif A == "7" or A == "07":
	sqlmap()

elif A == "8" or A == "08":
	vbug()

elif A == "9" or A == "09":
	redhawk()

elif A == "10":
	facebook()

elif A == "11":
	blackhydra()

elif A == "12":
	youtube()

elif A == "13":
	weeman()

elif A == "14":
	websploit()

elif A == "15":
	xerxes()

elif A == "16":
	routersploit()

elif A == "17":
	ubuntu()

elif A == "18":
	kali()
	
elif A == "19":
	emailbomb()
	
elif A == "20":
	dost()

elif A == "21":
        hammer()

elif A == "22":
        social()

elif A == "23":
        santet()

elif A == "24":
        xshell()

elif A == "99":
    os.system("clear")
    print"Creator : Zero Hacker TH"
    print"YouTube : https://www.youtube.com/channel/UC0m4EAZ9_PMfygFXx9P25hg"
    print"Blog    : http://dedseccyberteam.blogspot.com"
    print"FB Group: https://m.facebook.com/groups/181290935835347"
    timeout(8)
    restart_program()


elif A == "00":
	sys.exit()

else:
	print "input errer"
	timeout(4)
	restart_program()
    
    
    
    

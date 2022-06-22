import os
os.system('pip3 install slowprint && clear && pip3 install requests && clear && pip3 install json  && clear && pip3 install colorama')
from colorama import Fore, Back, Style, init
import json
import requests
import time
from slowprint.slowprint import *
init(autoreset=True)
os.system('clear')
def home():
	os.system('clear')
	print(Fore.RED + '[TOS] You are not allowed to sell or miss use it and we are not responsible for your any action, Thanks!')
	print(Fore.BLUE + '''
		  ██╗     ██╗███╗   ██╗██╗   ██╗██╗  ██╗    ███████╗███████╗████████╗██╗   ██╗██████╗ 
		  ██║     ██║████╗  ██║██║   ██║╚██╗██╔╝    ██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗
		  ██║     ██║██╔██╗ ██║██║   ██║ ╚███╔╝     ███████╗█████╗     ██║   ██║   ██║██████╔╝
		  ██║     ██║██║╚██╗██║██║   ██║ ██╔██╗     ╚════██║██╔══╝     ██║   ██║   ██║██╔═══╝ 
		  ███████╗██║██║ ╚████║╚██████╔╝██╔╝ ██╗    ███████║███████╗   ██║   ╚██████╔╝██║     
		  ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝     
			''')
	print(Fore.RED + '''
╔════════════════════╗ 
║ Linux Basic Setup  ║   
║ 1) XAMPP           ║ 
║ 2) XAMPP FIX       ║   
║ 3) WEBMIN          ║
║ 4) WEBMIN FIX      ║
║ 5) SOME ESSTIALS   ║   
║ 6) TXADMIN         ║     
║ 7) START SERVER    ║  
║ 8) After Restart   ║
║ 9) Set DDoS Logs   ║  
╚════════════════════╝                      
''')


slowprint('Welcome to Linux Setup by unfriendme#3463', 0.3)
slowprint('Please insert a valid Webhook otherwise logs maybe broken.', 0.3)
webhook = input(Fore.CYAN + 'Webhook: ')
home()
	

alert = '''
echo -e "Alerts By Linux Setup"
echo
echo "If you need any assistence configuring or adding the notify message unfriendme#3463 on discord for help."
echo
echo -e "033[97mPackets/s \033[36m{}\n\033[97mBytes/s \033[36m{}\n\033[97mKbp/s \033[36m{}\n\033[97mGbp/s \033[36m{}\n\033[97mMbp/s \033[36m{}"
interface=eth0
dumpdir=/root/dumps
url=''' + f"'{webhook}'" + '''
while /bin/true; do
  old_b=`grep $interface: /proc/net/dev | cut -d :  -f2 | awk '{ print $1 }'`
  
  old_ps=`grep $interface: /proc/net/dev | cut -d :  -f2 | awk '{ print $2 }'`
  sleep 1
  new_b=`grep $interface: /proc/net/dev | cut -d :  -f2 | awk '{ print $1 }'`

  new_ps=`grep $interface: /proc/net/dev | cut -d :  -f2 | awk '{ print $2 }'`
  ##Defining Packets/s
  pps=$(( $new_ps - $old_ps ))
  ##Defining Bytes/s
  byte=$(( $new_b - $old_b ))

  gigs=$(( $byte/1024 ** 3 ))
  mbps=$(( $byte/1024 ** 2 ))
  kbps=$(( $byte/1024 ** 1 ))

  echo -ne "\r$pps packets/s\033[0K"
  tcpdump -n -s0 -c 1500 -w $dumpdir/capture.`date +"%Y%m%d-%H%M%S"`.pcap
  echo "`date` Detecting Attack Packets."
  sleep 1
  if [ $pps -gt 10000 ]; then ## Attack alert will display after incoming traffic reach 30000 PPS
    echo " Attack Detected Monitoring Incoming Traffic"
    curl -H "Content-Type: application/json" -X POST -d '{
      "embeds": [{
      	"inline": false,
        "title": "Attack Detected On",
        "username": "Attack Alerts",
        "color": 15158332,
         "thumbnail": {
          "url": "https://imgur.com/a/cZAa3Pu"
        },
         "footer": {
            "text": "Our system is attempting to mitigate the attack and automatic packet dumping has been activated.",
            "icon_url": "https://cdn.countryflags.com/thumbs/united-states-of-america/flag-800.png"
          },
    
        "description": "Detection of an attack ",
         "fields": [

      {
        "name": "**Incoming Packets**",
        "value": " '$pps' Pps ",
        "inline": false
      }
    ]
      }]
    }' $url
    echo "Paused for."
    sleep 120  && pkill -HUP -f /usr/sbin/tcpdump  ## The "Attack no longer detected" alert will display in 220 seconds
    ## echo "Traffic Attack Packets Scrubbed"
    echo -ne "\r$mbps megabytes/s\033[97"
    curl -H "Content-Type: application/json" -X POST -d '{
      "embeds": [{
      	"inline": false,
        "title": "Attack Stopped",
        "username": "  Attack Alerts",
        "color": 3066993,
         "thumbnail": {
          "url": "https://imgur.com/a/1YNwLCo.gif"
        },
         "footer": {
            "text": "Our system has mitigated the attack and automatic packet dumping has been deactivated.",
            "icon_url": "https://cdn.countryflags.com/thumbs/united-states-of-america/flag-800.png"
          },    
          
        "description": "End of attack",
         "fields": [

      {
        "name": "**Packets**",
        "value": "'$mbps' Mbps ",
        "inline": false
      }
    ]
      }]
    }' $url
  fi
done'''
service='''
[Unit]

Description=Discord DDoS Alert System
After=network.target
Wants=network-online.target

[Service]
Type=simple
User=root
WorkingDirectory=/root
ExecStart=/bin/bash discordalerts.sh
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target	
'''







while True:

	choice = input(Fore.YELLOW + '''╔═[root@installer]
╚════➢''')

	if choice == '1':
		os.system('wget https://www.apachefriends.org/xampp-files/8.0.8/xampp-linux-x64-8.0.8-0-installer.run')
		os.system('chmod 755 xampp-linux-x64-8.0.8-0-installer.run')
		os.system('./xampp-linux-x64-8.0.8-0-installer.run')
		home()
	if choice == '2':
		with open("/opt/lampp/phpmyadmin/config.inc.php") as f:
			content = f.read()

		content = content.replace("$cfg['Servers'][$i]['auth_type'] = 'config';", "$cfg['Servers'][$i]['auth_type'] = 'cookie';")

		with open("/opt/lampp/phpmyadmin/config.inc.php", 'w') as f:
			f.write(content)

		with open("/opt/lampp/etc/extra/httpd-xampp.conf") as y:
			content2 = y.read()

		content2 = content2.replace("Require local", "Require all granted")

		with open("/opt/lampp/etc/extra/httpd-xampp.conf", 'w') as y:
			y.write(content2)

		os.system('/opt/lampp/xampp restart')
		home()
	if choice == '3':
		os.system('apt update')

		with open("/etc/apt/sources.list", 'a') as y:
			y.write('\ndeb http://download.webmin.com/download/repository sarge contrib')

		os.system('apt update')
		os.system('apt install gnupg1 -y')
		os.system('apt update')
		os.system('wget -q -O- http://www.webmin.com/jcameron-key.asc | apt-key add')
		os.system('apt update')
		os.system('apt install webmin -y')
		home()
	if choice == '4':

		with open("/etc/webmin/miniserv.conf") as y:
			content2 = y.read()

		content2 = content2.replace("ssl=1", "ssl=0")

		with open("/etc/webmin/miniserv.conf", 'w') as y:
			y.write(content2)
		os.system('systemctl restart webmin')
		home()
	if choice == '5':
		os.system('apt update')
		os.system('apt install screen')
		os.system('apt install unrar')
		home()
	if choice == '6':
		os.system('cd /home && mkdir fivem && cd fivem && wget https://runtime.fivem.net/artifacts/fivem/build_proot_linux/master/4394-572b000db3f5a323039e0915dac64641d1db408e/fx.tar.xz && tar -xvf fx.tar.xz')
		home()
	if choice == '7':
		os.system('screen /home/fivem/run.sh')
		home()
	if choice == '8':
		os.system('/opt/lampp/xampp start')
		os.system('screen /home/fivem/run.sh')
		home()
	if choice == '9':
		os.system('apt update')
		alerts = alert
		with open('/root/discordalerts.sh', 'a') as f:
			f.write(alerts)

		with open('/etc/systemd/system/discord.service', 'a') as f:
			f.write(service)

		os.system('sudo apt-get update && sudo apt-get install tcpdump -y && sudo apt-get install dos2unix -y && sudo apt-get install curl -y && sudo apt-get install screen -y && systemctl daemon-reload && systemctl start discord && systemctl enable discord && service discord start && service discord status && screen bash /root/discordalerts.sh')
		home()


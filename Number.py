#BELAJAR_BARENG !!!
#My Friend : Jenderal92 - h0d3_g4n - Moslem - Kiddenta - Naskleng45
#Thanks To : https://www.lexisrex.com
#Official Blog : http://www.blog-gan.org
###Module###
import requests,re,os,sys,random,time
from colorama import Fore
###Banner###
def Banner():
    clear = '\x1b[0m'
    colors = [36, 32, 34, 35, 31, 37]

    x = '''
    _____  
^..^     \9
(oo)_____/ 
   WW  WW
NOMOR DALAM BAHASA INGGRIS
               
'''
    for N, line in enumerate(x.split('\n')):
        sys.stdout.write('\x1b[1;%dm%s%s\n' % (random.choice(colors), line, clear))
        time.sleep(0.02)
Banner()
###MULAI###
number = raw_input(Fore.YELLOW+"Number : "+Fore.WHITE)

def numbe():
	try:
		head = {'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36'}
		numb = "https://www.lexisrex.com/Bahasa%20Inggris/Angka-angka/"+number
		a = requests.post(numb, headers=head).content
		if 'Bahasa Inggris' in a:
			b = re.findall("<b><div style='border: 1px solid #dddddd;background:#dbffcc;color:#aa88aa;font-size:26px;text-align:center;width:70%;margin:0px 0px 2px 0px;'>(.*?)</div></font></b>", a)
			for c in b:
				print(Fore.GREEN+'Result : '+ '(' + c +')' +Fore.WHITE)
	except:
		pass
###PENGULANGAN###
def ulangi():
	d = raw_input("Apakah anda Ingin mengulangi program? Y/N : ")
	if d=="y":
		os.system("python2 Number.py")
	elif d =="n":
		print("CODED BY SHIN_CODE")
		sys.exit()

numbe()
ulangi()

###AKHIR###
import requests
from multiprocessing.dummy import Pool
import sys, os

if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")
	
print("""
 [#] CMS Tarayici
 [#] Coded by Trinity
 [#] www.trinityreturn.com
""")

def scan(site):
	try:
		if "http" in site:
			url = site
		else:
			url = "http://" + site
		r = requests.get(url,timeout=5)
		if "/wp-content/" in r.text:
			print
			with open("wordpress.txt","a") as f:
				f.write(url + "\n")
		elif "Joomla!" in r.text or "index.php?option=com_" in r.text:
			print
			with open("joomla.txt","a") as f:
				f.write(url + "\n")			
		elif "index.php?route=common/home" in r.text:
			print
			with open("opencart.txt","a") as f:
				f.write(url + "\n")
		elif "sites/default" in r.text:
			print
			with open("drupal.txt","a") as f:
				f.write(url + "\n")
		elif "prestashop" in r.text or "PrestaShop" in r.text:
			print
			with open("prestashop.txt","a") as f:
				f.write(url + "\n")
		elif "osCommerce" in r.text:
			print
			with open("oscommerce.txt","a") as f:
				f.write(url + "\n")
		elif "vBulletin" in r.text:
			print
			with open("vbulletin.txt","a") as f:
				f.write(url + "\n")
		elif "Mage.Cookies" in r.text:
			print
			with open("magento.txt","a") as f:
				f.write(url + "\n")
		else:
			print
			with open("othercms.txt","a") as f:
				f.write(url + "\n")
	except:
		print

sitelist = input("Sitelist : ")
print("")

try:
	sites = open(sitelist,"r").read().splitlines()
	pp = Pool(100)
	pr = pp.map(scan,sites)
except:
	print("Sites not found!")
	sys.exit()
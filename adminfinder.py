#!/usr/bin/python3

import requests,sys

print("""
                               (                            
   (     (                     )\ )           (             
   )\    )\ )   )   (         (()/( (         )\ )  (  (    
((((_)( (()/(  (    )\  (      /(_)))\  (    (()/( ))\ )(   
 )\ _ )\ ((_)) )\  ((_) )\ )  (_))_((_) )\ )  ((_)/((_(()\  
 (_)_\(_)_| |_((_)) (_)_(_/(  | |_  (_)_(_/(  _| (_))  ((_) 
  / _ \/ _` | '  \()| | ' \)) | __| | | ' \)/ _` / -_)| '_| 
 /_/ \_\__,_|_|_|_| |_|_||_|  |_|   |_|_||_|\__,_\___||_|   
                                                            
	""")
print("TY:Hackerslaboratory  SocialMedia:@MrKevinPeter\n\n")


print("Enter a Url (example.com/www.example.com")
url=input("{URL}==>> ")

def kevin():
	lives=[]
	lines=arq.readlines()
	arq.close
	fd="Not Found"
	fdb = str.encode(fd)

	for line in lines:
		line =line.replace("\n", "")
		request = 'http://'+url+'/'+line
		http = requests.get(request)
		code = http.status_code
		if code != 301 and code!= 404:
			if not fdb in http.content :
				print("[+] Page Found: "+request)
				lives.append(request)
			else:
				print("[-] Page Not Found: "+request)
		else:
			print("[-] Page Not Found: "+ request)
	print("\aFinish!")
	for live in lives:
		print(live)


print("Choose the wordlist Source:\n")
print("1)Custom Wordlist.")
print("2)Default Wordlist.")
scr=int(input(":>"))
if scr==1:
	wl=input("Enter a path for wordlist:")
	arq = open(wl,"r")
	kevin()
elif scr==2:
	print("Select the wordlist type you want:")
	print("1) HTML")
	print("2) PHP")
	print("3) ASP")
	print("4) CFM")
	print("5) JS")
	print("6) CGI")
	print("7) BRF")
	scrt=int(input("::>"))
	if scrt==1:
		arq = open("~/sourcefiles/hwtlml.txt","r")
		kevin()
	elif scrt==2:
		arq = open("~/sourcefiles/pwhlp.txt","r")
		kevin()
	elif scrt==3:
		arq = open("~/sourcefiles/awslp.txt","r")
		kevin()
	elif scrt==4:
		arq = open("~/sourcefiles/cwflm.txt","r")
		kevin()
	elif scrt==5:
		arq = open("~/sourcefiles/jwsl.txt","r")
		kevin()
	elif scrt==6:
		arq = open("~/soucrefiles/cwgli.txt","r")
		kevin()
	elif scrt==7:
		arq = open("~/sourcefiles/bwrlf.txt","r")
		kevin()
	else:
		print("Invaild Input!")
else:
	print("Invaild Input!")

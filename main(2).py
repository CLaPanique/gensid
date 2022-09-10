comId=""
import os
os.system("pip install websocket-client amino.py json_minify")
os.system("clear") 
import random,amino,names 
from amino import Client
from amino import SubClient
from amino.lib.util.exceptions import *
from concurrent.futures import ThreadPoolExecutor
from fancy_text import fancy
from os import path
import platform,socket,re,uuid,json,requests
print("name and photo changer of community\nMade By Human#1111")
THIS_FOLDER = path.dirname(path.abspath(__file__))
emailfile=path.join(THIS_FOLDER,"accounts.json")
dictlist=[]
with open(emailfile) as f:
    dictlist = json.load(f)
client=amino.Client()
def fancy_name():
	nm=''
	for i in names.get_first_name():
		nm=nm+i
	return nm
def threadit(acc : dict):
    email=acc["email"]
    password=acc["password"]
    device=acc["device"]
    client=amino.Client(device)
    try:
        client.login(email=email,password=password)
    except:
        pass
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    print(f"logged into {email}")
    try:
        num = ["download.jpeg-1.jpg","download.jpeg-2.jpg","download.jpeg-3.jpg","download.jpeg-4.jpg","download.jpeg.jpg","images.jpeg-1.jpg","images.jpeg-10.jpg","images.jpeg-11.jpg","images.jpeg-12.jpg","images.jpeg-13.jpg","images.jpeg-14.jpg","images.jpeg-15.jpg","images.jpeg-2.jpg","images.jpeg-3.jpg","images.jpeg-4.jpg","images.jpeg-5.jpg","images.jpeg-6.jpg","images.jpeg-7.jpg","images.jpeg-8.jpg","images.jpeg-9.jpg","images.jpeg.jpg"]
        human=random.choice(num)
        client.join_community(comId)
        os.system(f"cp img/{human} img.png")
        img=open("img.png","rb")
        nick=fancy_name()
        subclient=amino.SubClient(comId = comId,profile=client.profile)
        subclient.edit_profile(icon=img,nickname=nick)
        os.remove("img.png")
        print("The name has been changed to "+ nick)
        print("The image has been changed to "+ human)
    except:
    	pass
    
    
  
def main():
    print(f"{len(dictlist)} accounts loaded")
    for amp in dictlist:
        threadit(amp)
    print("all accounts have been modified")
        	         
if __name__ == '__main__':
	main()
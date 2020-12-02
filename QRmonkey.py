import requests as req
import socket , time
from colorama import Fore , init
init()

green = Fore.GREEN
Lgreen = Fore.LIGHTGREEN_EX
lred = Fore.LIGHTRED_EX
lcyan = Fore.LIGHTCYAN_EX

banner = """
  ░█▀▀█ ░█▀▀█ ── ░█▀▄▀█ █▀▀█ █▀▀▄ █─█ █▀▀ █──█ 
  ░█─░█ ░█▄▄▀ ▀▀ ░█░█░█ █──█ █──█ █▀▄ █▀▀ █▄▄█ 
  ─▀▀█▄ ░█─░█ ── ░█──░█ ▀▀▀▀ ▀──▀ ▀─▀ ▀▀▀ ▄▄▄█
   [+] By GH0STH4CK3R   [+] QRcodeMonkey Api
------------------------------------------------"""

print(green + banner)

try:
    ip = socket.gethostbyname("www.google.com") 
    print(Lgreen + "[+] Internet : Active\n")   
except Exception as e:
    print(lred + "[-] Internet : Not Available \nExitting in 5 seconds")  
    time.sleep(5)
    exit()

Data = input("Enter data to store in QR code : ")

url = "https://qr-generator.qrcode.studio/qr/custom"

#data = input("Enter url : ")

#payload = {"data":"https://www.qrcode-monkey.com","config":{"body":"rounded-pointed","eye":"frame14","eyeBall":"ball16","erf1":[],"erf2":["fh"],"erf3":["fv"],"brf1":[],"brf2":["fh"],"brf3":["fv"],"bodyColor":"#5C8B29","bgColor":"#FFFFFF","eye1Color":"#3F6B2B","eye2Color":"#3F6B2B","eye3Color":"#3F6B2B","eyeBall1Color":"#60A541","eyeBall2Color":"#60A541","eyeBall3Color":"#60A541","gradientColor1":"#5C8B29","gradientColor2":"#25492F","gradientType":"radial","gradientOnEyes":"false","logo":""},"size":"300","download":"false","file":"svg"}
payload1 = {"data":Data,"config":{"body":"square","eye":"frame13","eyeBall":"ball14","erf1":[],"erf2":[],"erf3":[],"brf1":[],"brf2":[],"brf3":[],"bodyColor":"#000000","bgColor":"#FFFFFF","eye1Color":"#021326","eye2Color":"#021326","eye3Color":"#021326","eyeBall1Color":"#074f03","eyeBall2Color":"#074f03","eyeBall3Color":"#074f03","gradientColor1":"#12a637","gradientColor2":"#0b509e","gradientType":"linear","gradientOnEyes":"true","logo":"","logoMode":"default"},"size":1000,"download":"imageUrl","file":"png"}
payload2 = {"data":Data,"config":{"body":"diamond","eye":"frame12","eyeBall":"ball17","erf1":[],"erf2":[],"erf3":[],"brf1":[],"brf2":[],"brf3":[],"bodyColor":"#000000","bgColor":"#FFFFFF","eye1Color":"#021326","eye2Color":"#021326","eye3Color":"#021326","eyeBall1Color":"#074f03","eyeBall2Color":"#074f03","eyeBall3Color":"#074f03","gradientColor1":"#12a637","gradientColor2":"#0b509e","gradientType":"linear","gradientOnEyes":"true","logo":"","logoMode":"default"},"size":1000,"download":"imageUrl","file":"png"}
payload3 = {"data":Data,"config":{"body":"circle-zebra-vertical","eye":"frame14","eyeBall":"ball18","erf1":[],"erf2":[],"erf3":[],"brf1":[],"brf2":[],"brf3":[],"bodyColor":"#000000","bgColor":"#FFFFFF","eye1Color":"#021326","eye2Color":"#021326","eye3Color":"#021326","eyeBall1Color":"#074f03","eyeBall2Color":"#074f03","eyeBall3Color":"#074f03","gradientColor1":"#12a637","gradientColor2":"#0b509e","gradientType":"linear","gradientOnEyes":"true","logo":"","logoMode":"default"},"size":1000,"download":"imageUrl","file":"png"}

print("\n1. Round Rectangle\n2. Circle\n3. Square\n")
ptype = int(input("Enter Design Type : "))
if ptype == 1 :
    payload = payload1
elif ptype == 2 :
    payload = payload2
elif ptype == 3 :
    payload = payload3
else :
    print("invalid option ! \nRedirect to Random Design Type")
    payload = payload1

resp = req.post(url , json=payload)

if resp.status_code == 200 :
    print("\n[+] Status : Success\n")
    OutPut = resp.json()
    Link = OutPut.get('imageUrl')
    Link = "http:" + Link
    print(lcyan + "Image Download Link : ",Link)    
    print(Lgreen + "")
    #Save = input("Enter name to save (example.png) : ")
    #Loc = "c:/Users/Dimuth De Zoysa/Desktop/" + Save
    response = req.get(Link)
    svnm = input("Name to save (sample.png) : ")
    if len(svnm) == 0 :
        svnm = "Sample_QRmonkey.png"

    file = open(svnm, "wb")
    file.write(response.content)
    file.close()
    #img = req.get(Link)
    #image = open(Loc,'wb')
    #image.write(img.content)
    #image.close()

    print(lcyan + "\nImage ",svnm," Saved (current directory)")
else:
    print(lred +"[-] Status : Error ",resp.status_code)

input("\nExit >")

import requests
import socket
from bs4 import BeautifulSoup
from Modules.func.log import con_log, url_log
from Modules.func.strip import strip_url


class Mailman:
    """
    Little way i created to grab a origin server ip from mailman
    (this will only apply to servers that use cpanel AKA cloudlinux since it includes the mailing service mailman)

    Grabs mailing list dest, from target env 
    extracts url and will cache to origin server
    """
    org_ip = []

    def __init__(self: object, url: str) -> None:
        self.mail(url)

    def mail(self: object, url: str) -> str:
        mail = False
        detectmailing = requests.get(f"{url}/mailman/listinfo/mailman", timeout=2).text
        
        if "About mailman" in detectmailing:
            mail = True
        
        if mail:
            bs = BeautifulSoup(detectmailing, 'html.parser')
            a = bs.find('a').get('href')
            sturl = strip_url(a)
            con_log("Origin: ", True, sturl)
            
            host = socket.gethostbyname(sturl)
            con_log("OriginIp: ", True, host)
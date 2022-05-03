from re import L
import socket, requests
from Modules.colors import Colors

class Server_info:
    cloudflare = ['172', '104', '103', '173', '8']
    
    def __init__(self, site: str) -> None:
        self.cf_detect(site)
        
        if self.get_server(site):
            self.con_log("ServerType: ", True, self.get_server(site))
        if self.content_type(site):
            self.con_log("ContentType: ", True, self.content_type(site))
        if self.pingback(site):
            self.con_log("XPingback: ", True, self.pingback(site))

    def cf_detect(self:object, site:str) -> None:
        urlS = self.strip_url(site)
        Sip = socket.gethostbyname(urlS)
        for _ in self.cloudflare:
            if Sip.startswith(_):
                return self.con_log("Server-ip: ", "Warning", f"{Sip} ({Colors.RED}Cloudflare{Colors.WHITE})")
            
        return self.con_log("ServerIp: ", True, f"{Sip}")
            
    def pingback(self: object, site: str) -> bool:
        re = requests.get(site).headers
        try:
            return re['X-Pingback']
        except:
            return False

    def get_server(self: object, site: str) -> bool:
        re = requests.get(site).headers
        try:
            return re['Server']
        except:
            return False
    
    def content_type(self: object, site: str) -> bool:
        re = requests.get(site).headers
        try:
            return re['Content-Type']
        except:
            return False

    def strip_url(self: object, site: str) -> str:
        # this could be a one liner but why not make it a function
        site = site.replace('https://', '')
        site = site.replace('http://', '')
        site = site.replace('://', '')
        site = site.replace('/', '')
        return site
    
    def con_log(self: object, text: str, status: str, data: str) -> None:
        if status == True:
            return print(f"{text}{Colors.BRIGHT}{Colors.GREEN}✓{Colors.WHITE} -> {data}")
        elif status == "Warning":
            return print(f"{text}{Colors.BRIGHT}{Colors.YELLOW}!{Colors.WHITE} -> {data}")
        else:
            return print(f"{text}{Colors.BRIGHT}{Colors.RED2}✘{Colors.WHITE} -> Not found")

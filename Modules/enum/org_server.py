from re import L
import dns.resolver
import socket, requests
from Modules.colors import Colors
from Modules.func.strip import strip_url
from Modules.func.log import con_log, url_log

class Server_info:

    """
    Looks for Cloudflare IPs, checks headers for content type and server type and returns them
    """
    cloudflare = ['172', '104', '103', '173', '8']
    
    def __init__(self, site: str) -> None:
        self.cf_detect(site)
    
        if self.get_server(site):
            con_log("ServerType: ", True, self.get_server(site))
            url_log(self.get_server(site), 'info', 'serverType')
        if self.content_type(site):
            con_log("ContentType: ", True, self.content_type(site))
            url_log(self.content_type(site), 'info', 'contentType')
        if self.pingback(site):
            con_log("XPingback: ", True, self.pingback(site))

    def cf_detect(self:object, site:str) -> None:
        urlS = strip_url(site)
        Sip = socket.gethostbyname(urlS)
        for _ in self.cloudflare:
            if Sip.startswith(_):
                return con_log("Server-ip: ", "Warning", f"{Sip} ({Colors.RED}Cloudflare{Colors.WHITE})")
        url_log(Sip, 'info', 'ip')
        return con_log("ServerIp: ", True, f"{Sip}")
            
    def pingback(self: object, site: str) -> bool:
        re = requests.get(site, timeout=2).headers
        try:
            return re['X-Pingback']
        except:
            return False

    def get_server(self: object, site: str) -> bool:
        re = requests.get(site, timeout=2).headers
        try:
            return re['Server']
        except:
            return False
    
    def content_type(self: object, site: str) -> bool:
        re = requests.get(site, timeout=2).headers
        try:
            return re['Content-Type']
        except:
            return False




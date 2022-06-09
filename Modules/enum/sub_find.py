import requests
from Modules.colors import Colors
from Modules.func.strip import strip_url
from Modules.func.log import con_log

class Subdomain:
    

    def __init__(self, site: str) -> None:
        sdomain = strip_url(site)
        self.subdomain(sdomain)
        
    def subdomain(self: object, site: str) -> None:
        sub = open('Modules/data/subdomain.txt', 'r').readlines()
        for _ in sub:
            try:
                subdom = f"http://{_.strip()}.{site}"
                requests.get(subdom, timeout=0.5)
                con_log("Subdomain: ", True, subdom)
            except:
                pass
        return
# go down list of subdomains and check if they are alive
def sub_find(site: str) -> None:
    print(Colors.green("\n[+] Checking subdomains"))
    Subdomain(site)
    print(Colors.green("[+] Finished checking subdomains"))

import requests
from Modules.colors import Colors


class Subdomain:
    

    def __init__(self, site: str) -> None:
        sdomain = self.strip_url(site)
        self.subdomain(sdomain)
        


    def subdomain(self: object, site: str) -> None:
        sub = open('Modules/data/subdomain.txt', 'r').readlines()
        for _ in sub:
            try:
                subdom = f"http://{_.strip()}.{site}"
                requests.get(subdom, timeout=0.5)
                self.con_log("Subdomain: ", True, subdom)
            except:
                pass

        return

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

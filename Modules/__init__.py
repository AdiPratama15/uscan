from Modules.enum.headers import HeaderModule
from Modules.enum.cms_detect import CmsDetector
from Modules.enum.org_server import Server_info
from Modules.enum.sub_find import Subdomain
from Modules.colors import Colors
from Uscan import intBanner
import os

def __init__(site):
    if os.name != 'nt':
        os.system("clear")
    else:
        os.system("cls")

    print(intBanner())
    print(f"{Colors.BRIGHT}{Colors.GREY}Url: {Colors.UNDERLINE}{site}{Colors.RESET}{Colors.WHITE}\n")
    match is_invalid(site):
        case 'Blacklist':
            return print("This URL is blacklisted because it has involvement with a federal government")
        case 'Novalid':
            return print("This URL is not valid (http://google.com/)")
        case _:
            #Subdomain(site) // takes to long
            print(f"{Colors.BRIGHT}-------------CMS_DETECTOR-------------")
            CmsDetector(site)
            print("-------------SERVER_INFO-------------")
            Server_info(site)
            print("-------------PROTECTION_HEADERS-------------")
            HeaderModule(site)



def is_invalid(url: str) -> bool:
   """
    Blacklisted URLS and EXT where added to prevent collisions with there websites.
    If you do remove this function from this module, all actions will be on you / USCAN will have no involvement
   """
   invalid_exts = [".gov", ".edu", ".us"]

   if not url.startswith(("http", "https")):
        return "Novalid"
   
   for ext in invalid_exts:
        if ext in url:
            return "Blacklist"


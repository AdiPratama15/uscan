from Modules.enum.headers import HeaderModule
from Modules.enum.cms_detect import CmsDetector
from Modules.enum.org_server import Server_info
from Modules.enum.mailman import Mailman
from Modules.enum.sub_find import Subdomain
from rich.console import Console
from Modules.enum.dns_records import dns_scanner
from Modules.enum.links_search import LinkFinder
from Modules.colors import Colors
from Uscan import intBanner
from Modules.func.log import *
import os, re

def __init__(site):
    if os.name != 'nt':
        os.system("clear")
    else:
        os.system("cls")

    print(intBanner())
    
    match is_invalid(site):
        case 'Blacklist':
            return print("This URL is blacklisted because it has involvement with a federal government")
        case 'Novalid':
            return print("This URL is not valid (http://google.com/)")
        case _:
            #Subdomain(site) // takes to long
            try:
                console = Console()
                tasks = [f"task {n}" for n in range(1, 5)]
                with console.status("Scanning url...") as status:
                    task = tasks.pop(0)
                    print(f"{Colors.BRIGHT}{Colors.GREY}Url: {Colors.ITALIC}{site}{Colors.RESET}{Colors.WHITE}\n")
                    print(f"{Colors.BRIGHT}═════════════════CMS_DETECTOR═════════════════")
                    CmsDetector(site)
                    
                    print("═════════════════SERVER_INFO═════════════════")
                    Server_info(site)
                    Mailman(site)
                    print("═════════════════DNS_RECORDS═════════════════")
                    dns_scanner(site)
                    print("═════════════════PROTECTION_HEADERS═════════════════")
                    HeaderModule(site)
                    print("═════════════════URL_LINKS═════════════════")
                # limit amount of links to show 
                    LinkFinder(site, limit=10)
                #LinkFinder(site)
                    url_log(site, None, True)
                    
            except Exception as e:
                """write to errorlog"""
                print("An error occured, check the log file")
                with open("errorlog.txt", "a") as f:
                    f.write(f"{e}\n")
                f.close()
            


def is_invalid(url: str) -> bool:
   """
    Blacklisted URLS and EXT where added to prevent collisions with there websites.
    If you do remove this function from this module, all actions will be on you / USCAN will have no involvement
   """
   invalid_exts = [".gov", ".edu", ".us"]

   if not is_valid(url):
        return "Novalid"
   
   for ext in invalid_exts:
        if ext in url:
            return "Blacklist"

def is_valid(url: str) -> bool:
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None
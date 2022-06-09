import random
from Modules.colors import Colors
from datetime import datetime
from pytermgui import pretty

import json

now = datetime.now()


def __init__():
    gen_seed()

url_saved = [
    {   
        "detect":
        {"cms": "",
        "version": "",
        "themes": "",
        "users": "",
        "plugin": ""
        }, 
        "info":
        {"seed":"","url": "",
        "ip": "",
        "serverType": "",
        "contentType": ""
        }
    },
    ]
def con_log(text: str, status: str, data: str) -> None:
    if status == True:
        return print(f"{text}{Colors.BRIGHT}{Colors.GREEN}✓{Colors.WHITE} -> {data}")
    elif status == "Warning":
        return print(f"{text}{Colors.BRIGHT}{Colors.YELLOW}!{Colors.WHITE} -> {data}")
    else:
        return print(f"{text}{Colors.BRIGHT}{Colors.RED2}✘{Colors.WHITE} -> Not found")

def url_log(data: str, obj:str, type: str):
    if obj == "detect":
        url_saved[0]["detect"][type] = data
    elif obj == "info":
        url_saved[0]["info"][type] = data

    if type == True:
        current_time = now.strftime("%H:%M:%S")
        
        url_saved[0]['info']['url'] = data

        url_saved[0]['info']['seed'] = gen_seed()
        
        time = current_time.replace(':', '_')
        
        with open(f'results/{time}.json', 'a+') as log:
            log.write(json.dumps(url_saved, indent=3)+'\n')
            log.close()
        
        print("═════════════════END_LOG═════════════════")
        print(f"{Colors.BRIGHT}{Colors.ITALIC}Scan log saved at {Colors.BLUE}{current_time}{Colors.WHITE}, location: {Colors.GREY}results/{time}.json {Colors.WHITE}")
        print(f"{Colors.BRIGHT}{Colors.ITALIC}Dns log saved at {Colors.BLUE}{current_time}{Colors.WHITE}, location: {Colors.GREY}results/{time}_DNS.txt{Colors.WHITE}")
        print(f"{Colors.BRIGHT}{Colors.ITALIC}Links log saved at {Colors.BLUE}{current_time}{Colors.WHITE}, location: {Colors.GREY}results/{time}_links.txt{Colors.RESET}")

def dns_log(data: str, url: str):
    current_time = now.strftime("%H:%M:%S")
    
    time = current_time.replace(':', '_')
    
    with open(f'results/{time}_DNS.txt', 'a+') as log:
        log.write(f'[{url}] -  | '+data+'\n')
        log.close()


def link_log(data: str):
    current_time = now.strftime("%H:%M:%S")
    
    time = current_time.replace(':', '_')
    
    with open(f'results/{time}_links.txt', 'a+') as log:
        log.write(data+'\n')
        log.close()

def gen_seed():
    seed = random.getrandbits(23)
    #__seed__.append(str(seed))
    return seed
import threading, readline
from pytermgui import tim
from __init__ import VERSION, PATHS, MODS


from Modules import __init__ as Scan
from Modules.colors import Colors



def intBanner():
    return f"""
                ╦ ╦┌─┐┌─┐┌─┐┌┐┌
                ║ ║└─┐│  ├─┤│││
                ╚═╝└─┘└─┘┴ ┴┘└┘
                        \033[1;91mスキャナー\033[00m
    """

def intHelp():
    return f"""
                                    
                              
             ╔══════════════════════════════════════════════════════════{Colors.WHITE}╗
       [blink2 red]U{Colors.RESET}     ║{Colors.WHITE}                                                          ║{Colors.WHITE}
       [bold blue]S[white]     ║{Colors.WHITE}   1. vulnscan - scans vulns in a target [reset]                 ║
       [red]C[white]     ║{Colors.WHITE}   2. autoscan - autodorks targets to scan for vulns      ║{Colors.WHITE}
       [blue]A[white]     ║{Colors.WHITE}                                                          ║{Colors.WHITE}
       [red]N[white]     ╚══════════════════════════════════════════════════════════{Colors.WHITE}╝

    """




if __name__ == '__main__':
    print(intBanner())
    try:
        while True:
            match input(f'[ {Colors.RED}{Colors.ITALIC}$can{Colors.WHITE}{Colors.RESET} ] {Colors.BRIGHT}>>{Colors.WHITE} '):
                case 'help':
                    tim.print(intHelp())
                case '1':
                    userinput = input(f'{Colors.RESET}[ {Colors.RED}{Colors.ITALIC}Url{Colors.WHITE}{Colors.RESET} ] {Colors.BRIGHT}>>{Colors.WHITE} ')
                    t1 = threading.Thread(target=Scan, args=([userinput]))
                    t1.start()
                    t1.join()
                case '2':
                    pass
                case '3':
                    pass
                case _:
                    print('Invalid command, please look at the help command list')
    except KeyboardInterrupt:
        exit(f"\n\nExiting {Colors.RED2}Uscan{Colors.WHITE}...\n")
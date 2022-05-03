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
                                    {Colors.UNDERLINE}{Colors.BRIGHT}Help menu{Colors.WHITE}{Colors.RESET}
                              
            $##########################################################{Colors.WHITE}$
            {Colors.RED}${Colors.WHITE}                                                          {Colors.RED}${Colors.WHITE}
            {Colors.RED}${Colors.WHITE}   1. vulnscan - scans mass vuln's in a website           {Colors.RED}${Colors.WHITE}
            {Colors.RED}${Colors.WHITE}   2. autoscan - autodorks websites to scan for vuln's    {Colors.RED}${Colors.WHITE}
            {Colors.RED}${Colors.WHITE}                                                          {Colors.RED}${Colors.WHITE}
            $##########################################################{Colors.WHITE}$

    """




if __name__ == '__main__':
    print(intBanner())
    while 1:
        match input(f'[ {Colors.RED}{Colors.UNDERLINE}{Colors.BRIGHT}$can{Colors.WHITE}{Colors.RESET} ] {Colors.BRIGHT}>>{Colors.WHITE} '):
            case 'help':
                print(intHelp())
            case '1':
                Scan(input(f'[ {Colors.RED}{Colors.UNDERLINE}{Colors.BRIGHT}Url{Colors.WHITE}{Colors.RESET} ] {Colors.BRIGHT}>>{Colors.WHITE} '))
            case '2':
                pass
            case '3':
                pass
            case _:
                print('Invalid command')
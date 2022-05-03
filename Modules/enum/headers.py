import requests
from Modules.colors import Colors


class HeaderModule:
    required = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-XSS-Protection",
        "X-Content-Type-Options",
        "Cross-Origin-Resource-Policy"
        ]


    def __init__(self: object, site: str) -> None:
        headers = requests.get(site, timeout=5).headers
        located = [header for header in headers if header in self.required]

        """
        Suggest you should take a look at the documentation for these protection headers
        DOCS: https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html 
        """
        
        print(f'Located a total of {Colors.GREEN}{len(located)}{Colors.WHITE} out of {Colors.RED2}{len(self.required)}{Colors.WHITE} required protection headers:')
        
        for count, header in enumerate(self.required, start=1):
            if header in located:
                print(f'{count}: {Colors.BRIGHT}{Colors.GREEN}✓{Colors.WHITE} -> {header} - ({Colors.YELLOW2}{headers[header]}{Colors.WHITE})')
            else:
                print(f'{count}: {Colors.BRIGHT}{Colors.RED2}✘{Colors.WHITE} -> {header}')
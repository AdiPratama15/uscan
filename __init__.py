import os
import ctypes


from Errors    import ErrorHandler
from importlib import util


VERSION = 0.1
PATHS   = ['results', 'proxies']
MODS    = ['requests', 'googlesearch', 'random', 'socket']


@lambda _: _()
class _:


    def __init__(self: object) -> None:
        if os.name != 'nt':
            os.system('clear')
            for func in [self.paths, self.mods]:
                func()
        
        else:
            os.system('cls')

            for func in [self.title, self.paths, self.mods]:
                func()
    

    def title(self: object) -> None:
        ctypes.windll.kernel32.SetConsoleTitleW(f'Uscan | v{VERSION}')
    

    def paths(self: object) -> None:
        for path in PATHS:
            if not os.path.exists(path):
                os.mkdir(path)


    def mods(self: object) -> None:
        for mod in MODS:
            detected = util.find_spec(mod)

            if detected is not None:
                return f'{ErrorHandler.missing_module} {mod}'
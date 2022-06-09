import os
import ctypes
import datetime


from Errors    import ErrorHandler
from importlib import util


VERSION = 0.1
PATHS   = ['results', 'proxies']
MODS    = ['requests', 'googlesearch', 'random', 'socket', 'readline', 'dnspython', 'threading', 'rich']
RESULTS = 'results/'

@lambda _: _()
class _:

    def __init__(self: object) -> None:
        if os.name != 'nt':
            os.system('clear')
            for func in [self.paths, self.mods, self.file_age]:
                func()
                os.system('clear')
        
        else:
            os.system('cls')
            for func in [self.title, self.paths, self.mods, self.file_age]:
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
    
    def file_age(self: object) -> None:
        # counts files in directory
        def count_files(path: str) -> int:
            return len(os.listdir(path))
       
        if count_files(RESULTS) == 0:
            return
        
        for _ in os.listdir(RESULTS):
            path = os.path.join(RESULTS, _)
            
            if os.path.isfile(path):
                age = datetime.datetime.fromtimestamp(os.path.getmtime(path)).strftime('%Y-%m-%d %H:%M:%S')
                
                print(f"File: {path}| Last modified: {age} | Size: {os.path.getsize(path)}")
        
        files = input("\nWould you like to delete this files? (y/n)")
        
        if files == 'y':
            for _ in os.listdir(RESULTS):
                
                path = os.path.join(RESULTS, _)
                
                if os.path.isfile(path):
                    os.remove(path)
                    print(f"Deleted: {path}")
        
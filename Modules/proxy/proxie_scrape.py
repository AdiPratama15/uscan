import threading
import socket, requests
class ProxyScraper:
    # proxy scraper
    def __init__(self):
        self.proxy_scrape()

    def proxy_scrape(self):
        # proxy scraper using api
        proxy_api_list = ["https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all"]
        for _ in proxy_api_list:
            try:
                proxy_list = requests.get(_).text.split("\n")
                for _ in proxy_list:
                    if _:
                        # test proxys connection with sockets
                        try:
                            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            socket.setdefaulttimeout(0.2)
                            ip = _.split(":")[0]
                            port = int(_.split(":")[1])
                            # using threading on connect
                            threading.Thread(target=s.connect((ip, port))).start()
                            print(f"[+] {ip}:{port}")
                        except Exception as e:
                            
                            pass
            except Exception as e:
                print(e)
                pass
if __name__ == "__main__":
    ProxyScraper()

from Modules.func.strip import strip_url
from Modules.func.log import con_log, url_log, dns_log
import dns.resolver, os
import datetime


class dns_scanner:
    def __init__(self, site: str) -> None:
        """
        DNS records resolver, uses dns.resolver python library users must have dns.resolver installed
        """
        self.dns_resolver(site)
        
    def dns_resolver(self, site: str) -> None:
        url = strip_url(site)
        try:
            a = dns.resolver.resolve(url, 'A')
            mx = dns.resolver.resolve(url, 'MX')
            ns = dns.resolver.resolve(url, 'NS')
            txt = dns.resolver.resolve(url, 'TXT')
            for adata in a:
                con_log("DNS-A: ", True, adata)

                dns_log(f'DNS-A: {adata}', url)
            for mdata in mx:
                con_log("DNS-MX: ", True, mdata)

                dns_log(f'DNS-MX: {mdata}', url)
            for tdata in txt:
                con_log("DNS-TXT: ", True, tdata)

                dns_log(f'DNS-TXT: {tdata}', url)
            for ndata in ns:
                con_log("DNS-NS: ", True, ndata)

                dns_log(f'DNS-NS: {ndata}', url)
                
        except Exception as e:            
            con_log("DNS: ", "Warning", "No DNS records found") 
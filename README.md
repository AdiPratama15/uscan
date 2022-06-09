```bash

                ╦ ╦┌─┐┌─┐┌─┐┌┐┌
                ║ ║└─┐│  ├─┤│││
                ╚═╝└─┘└─┘┴ ┴┘└┘
                        スキャナー
    
Url: https://google.com

═════════════════CMS_DETECTOR═════════════════
CMS: ✘ -> Not found
═════════════════SERVER_INFO═════════════════
ServerIp: ✓ -> 142.250.69.238
ServerType: ✓ -> gws
ContentType: ✓ -> text/html; charset=ISO-8859-1
═════════════════DNS_RECORDS═════════════════
DNS-A: ✓ -> 142.250.69.238
DNS-MX: ✓ -> 10 smtp.google.com.
DNS-TXT: ✓ -> "facebook-domain-verification=22rm551cu4k0ab0bxsw536tlds4h95"
DNS-TXT: ✓ -> "MS=E4A68B9AB2BB9670BCE15412F62916164C0B20BB"
DNS-TXT: ✓ -> 
"google-site-verification=wD8N7i1JTNTkezJ49swvWW48f8_9xveREV4oB-0Hf5o"
DNS-TXT: ✓ -> 
"webexdomainverification.8YX6G=6e6922db-e3e6-4a36-904e-a805c28087fa"
DNS-TXT: ✓ -> "docusign=05958488-4752-4ef2-95eb-aa7ba8a3bd0e"
DNS-TXT: ✓ -> "globalsign-smime-dv=CDYX+XFHUw2wml6/Gb8+59BsH31KzUr6c1l2BPvqKX8="
DNS-TXT: ✓ -> 
"google-site-verification=TV9-DBe4R80X4v0M4U_bd_J9cpOJM0nikft0jAgjmsQ"
DNS-TXT: ✓ -> "atlassian-domain-verification=5YjTmWmjI92ewqkx2oXmBaD60Td9zWon9r6
eakvHX6B77zzkFQto8PQ9QsKnbf4I"
DNS-TXT: ✓ -> "apple-domain-verification=30afIBcvSuDV2PLX"
DNS-TXT: ✓ -> "v=spf1 include:_spf.google.com ~all"
DNS-TXT: ✓ -> "docusign=1b0a6754-49b1-4db5-8540-d2c12664b289"
DNS-NS: ✓ -> ns3.google.com.
DNS-NS: ✓ -> ns2.google.com.
DNS-NS: ✓ -> ns4.google.com.
DNS-NS: ✓ -> ns1.google.com.
═════════════════PROTECTION_HEADERS═════════════════
Located a total of 1 out of 5 required protection headers:
1: ✘ -> Strict-Transport-Security
2: ✘ -> Content-Security-Policy
3: ✓ -> X-XSS-Protection - (0)
4: ✘ -> X-Content-Type-Options
5: ✘ -> Cross-Origin-Resource-Policy
═════════════════URL_LINKS═════════════════
LinkFinder: ✓ -> LinkFinder initialized
LinkFinder: ✓ -> Found 11 links only displaying the first 10
Links: ✓ -> ['http://schema.org/WebPage"', 
'https://www.google.com/imghp?hl=en&tab=wi">Images</a>', 
'https://maps.google.com/maps?hl=en&tab=wl">Maps</a>', 
'https://play.google.com/?hl=en&tab=w8">Play</a>', 
'https://www.youtube.com/?gl=US&tab=w1">YouTube</a>', 
'https://news.google.com/?tab=wn">News</a>', 
'https://mail.google.com/mail/?tab=wm">Gmail</a>', 
'https://drive.google.com/?tab=wo">Drive</a>', 
'https://www.google.com/intl/en/about/products?tab=wh"><u>More</u>', 
'http://www.google.com/history/optout?hl=en"']
═════════════════END_LOG═════════════════
Scan log saved at 23:13:54, location: results/23_13_54.json 
Dns log saved at 23:13:54, location: results/23_13_54_DNS.txt
Links log saved at 23:13:54, location: results/23_13_54_links.txt
[ $can ] >> 




```

# install
```sh
>> git clone https://github.com/l4tt/uscan/uscan.git
>> pip install google
>> python3 Uscan.py
```
# info
* uscan is defined as universal scanner, it was made to target (Wordpress,Joomla,Druple,Vbulletin) systems.
* uscan identifys vulns in a target VIA automation, this is basically Vulnnr but better

```bash

                ╦ ╦┌─┐┌─┐┌─┐┌┐┌
                ║ ║└─┐│  ├─┤│││
                ╚═╝└─┘└─┘┴ ┴┘└┘
                        スキャナー
    
Url: https://wordpress.com

═════════════════CMS_DETECTOR═════════════════
Cms: ✓ -> Wordpress
Version: ✘ -> Not found
Themes: ✓ -> h4
Users: ✘ -> Not found
Plugins: ✘ -> Not found
═════════════════SERVER_INFO═════════════════
ServerIp: ✓ -> 192.0.78.9
ServerType: ✓ -> nginx
ContentType: ✓ -> text/html; charset=utf-8
═════════════════DNS_RECORDS═════════════════
DNS-A: ✓ -> 192.0.78.17
DNS-A: ✓ -> 192.0.78.9
DNS-MX: ✓ -> 10 mx1.dfw.automattic.com.
DNS-MX: ✓ -> 10 mx2.ams.automattic.com.
DNS-TXT: ✓ -> "google-site-verification=CW2JYOoHSXW8x6QyQO_a0edu0gNOKsLIHcO49QquLdU"
DNS-TXT: ✓ -> "google-site-verification=n3nz_h_B9qhixMk_gaBgKTc-5oUrxic5JtbqiHNqg6w"
DNS-TXT: ✓ -> "v=spf1 include:_spf.automattic.com include:servers.mcsv.net include:_spf-wwd.automattic.com include:mail.zendesk.com include:sendgrid.net -all"
DNS-NS: ✓ -> ns4.wordpress.com.
DNS-NS: ✓ -> ns1.wordpress.com.
DNS-NS: ✓ -> ns2.wordpress.com.
DNS-NS: ✓ -> ns3.wordpress.com.
═════════════════PROTECTION_HEADERS═════════════════
Located a total of 3 out of 5 required protection headers:
1: ✓ -> Strict-Transport-Security - (max-age=15552000; preload)
2: ✘ -> Content-Security-Policy
3: ✓ -> X-XSS-Protection - (1; mode=block)
4: ✓ -> X-Content-Type-Options - (nosniff)
5: ✘ -> Cross-Origin-Resource-Policy
═════════════════URL_LINKS═════════════════
LinkFinder: ✓ -> LinkFinder initialized
LinkFinder: ✓ -> Found 370 links only displaying the first 10
Links: ✓ -> ['http://wp.me/1"', 'https://wordpress.com/"', 'https://wordpress.com/"', 'https://wordpress.com/"', 'https://wordpress.com/ar/"', 'https://wordpress.com/de/"', 'https://wordpress.com/el/"', 'https://wordpress.com/es/"', 'https://wordpress.com/fr/"', 
'https://wordpress.com/he/"']
═════════════════END_LOG═════════════════
Scan log saved at 23:20:03, location: results/23_20_03.json 
Dns log saved at 23:20:03, location: results/23_20_03_DNS.txt
Links log saved at 23:20:03, location: results/23_20_03_links.txt
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

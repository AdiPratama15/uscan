def strip_url(site: str) -> str:
    site = site.replace('https://', '')
    site = site.replace('http://', '')
    site = site.replace('://', '')
    site = site.replace('/', '')
    site = site.replace('mailman', '').replace('listinfo', '').replace('private', '')
    return site



import requests

from Modules.func.log import con_log, link_log

import re

class LinkFinder:
    def __init__(self, url: str, limit: int) -> None:
        content = self.get_content(url)

        if self.find_links(content):
            con_log("LinkFinder: ", True, "LinkFinder initialized")
            con_log("LinkFinder: ", True, f"Found {len(self.find_links(content))} links only displaying the first {limit}")
            con_log("Links: ", True, f"{self.find_links(content)[:limit]}")
            for _ in self.find_links(content):
                link_log(_)
        else:
            con_log("LinkFinder: ", "Warning", "No links found")


    def get_content(self, url: str) -> str:
        """
        Gets content from a given url
        """
        try:
            content = requests.get(url, timeout=2).text
            return content
        except Exception as e:
            con_log("LinkFinder: ", "Warning", "Could not get content")
            return False

    def find_links(self, content: str) -> list:
        """
        Finds links in a given string
        """
        links = list()
        url_regex = re.compile(r'(?P<url>https?://[^\s]+)')
        for url in url_regex.findall(content):
            # replace tags in url
            #url = url.replace("<", "").replace(">", "")

            links.append(url)
        return links
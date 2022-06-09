import requests
import re
from Modules.colors import Colors
from Modules.func.log import con_log, url_log

class CmsDetector():
    """
    Use's default detection tactic's, search for specific key word's / scan's through directory's 
    for CMS detection.
    Wordpress, joomla, drupal, vbulletin
    """
    Headers = {'User-Agent': 'Mozilla/5.0 (X11; USCAN; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
    wordpress_dirs = [
        "/wp-includes/js/jquery/jquery.js",
        "/wp-content/",
        "/wp-includes/"
    ]
    
    joomla_dirs = [
        "/administrator/help/en-GB/toc.json",
        "/administrator/language/en-GB/install.xml",
        "/plugins/system/debug/debug.xml",
        "/administrator/"
    ]
    
    druple_dirs = [
        "/misc/ajax.js",
        "/"
    ]
    
    vbullet_dirs = [
        "/js/header-rollup-554.js",
        "/images/editor/separator.gif"
    ]
    
    vbullet_search = ["GIF89a", "js.compressed/modernizr.min.js"]
    druple_search = ["Drupal.ajax", "/sites/default/files"]
    joomla_search = ['COMPONENTS_BANNERS_BANNERS', '<author>Joomla!', 'content="Joomla!']
    
    
    def __init__(self: object, site: str) -> None:
        
        match self.Detect(site):
            case 'Wordpress':
                con_log("Cms: ", True, "Wordpress")
                url_log('Wordpress', 'detect', 'cms')
                if self.wp_version(site):
                    con_log("Version: ", True, self.wp_version(site))
                    url_log(self.wp_version(site), 'detect', 'version')
                else:
                    con_log("Version: ", False, self.wp_version(site))
                
                if self.wp_themes(site):
                    con_log("Themes: ", True, self.wp_themes(site))
                    url_log(self.wp_themes(site), 'detect', 'themes')
                else:
                    con_log("Themes: ", False, self.wp_themes(site))
                
                if self.wp_user(site):
                    con_log("Users: ", True, self.wp_user(site))
                    url_log(self.wp_user(site), 'detect', 'users')
                else:
                    con_log("Users: ", False, self.wp_user(site))
                    
                if self.wp_plugin(site):
                    con_log("Plugins: ", True, self.wp_plugin(site))
                    url_log(self.wp_plugin(site), 'detect', 'plugin')
                else:
                    con_log("Plugins: ", False, self.wp_plugin(site))
                
            case 'Joomla':
                url_log('Joomla', 'detect', 'cms')
                return con_log("CMS: ", True, "Joomla")
                
            case 'Druple':
                url_log('Druple', 'detect', 'cms')
                return con_log("CMS: ", True, "Druple")
            case 'Bullet':
                url_log('VBulletin', 'detect', 'cms')
                return con_log("CMS: ", True, "VBulletin")
            case _:
                url_log('Not found', 'detect', 'cms')
                return con_log("CMS: ", False, "Not found")
    
    def Detect(self: object, site: str) -> None:
        WRead = requests.get(site + "/", timeout=5, headers=self.Headers).content
        
        for wordpress in self.wordpress_dirs: 
            if wordpress in str(WRead):
                return "Wordpress"
        
        for joo in self.joomla_dirs:
            JRead = requests.get(site + joo, timeout=5, headers=self.Headers).content
            for jcontent in self.joomla_search:
                if jcontent in str(JRead):
                    return "Joomla"
        
        for druple in self.druple_dirs:
            DRead = requests.get(site + druple, timeout=5, headers=self.Headers).content
            for dcontent in self.druple_search:
                if dcontent in str(DRead):
                    return "Druple"
        
        for bullet in self.vbullet_dirs:
            BRead = requests.get(site + bullet, timeout=5, headers=self.Headers).content
            for bcontent in self.vbullet_search:
                if bcontent in str(BRead):
                    return "Bullet"
    
    def wp_version(self: object, url: str) -> None:
        getversion = requests.get(url, timeout=5, headers=self.Headers).text
        versearch = re.search(re.compile(
            r'content=\"WordPress (\d{0,9}.\d{0,9}.\d{0,9})?\"'), getversion)
        if versearch:
            return versearch.group(1)
            
    
    
    def wp_themes(self: object, url: str) -> None:
        themes_array = []
        getthemes = requests.get(url, timeout=5, headers=self.Headers).text
        matches = re.findall(re.compile(r'themes/(\w+)?/'), getthemes)
        if len(matches) > 0:
            for theme in matches:
                if theme not in themes_array:
                    themes_array.append(theme)
            for i in range(len(themes_array)):
                return themes_array[i]
            
    
    def wp_user(self: object, url: str) -> None:
        
        getuser = requests.get(url + '/?author=1', timeout=5, headers=self.Headers, allow_redirects=True)
        matches = re.search(re.compile(r'author/(\w+)?/'), getuser.text)
        matches_url = re.search(re.compile(r'/author/(\w+)?/'), getuser.url)
        if matches:
            return matches.group(1)
        elif matches_url:
            return matches_url.group(1)
        else:
            return None
    

    def wp_plugin(self: object, url: str) -> None:
        plugins_array = []
        getplugin = requests.get(url, timeout=5, headers=self.Headers).text
        matches = re.findall(re.compile(r'wp-content/plugins/(\w+)?/'), getplugin)
        if len(matches) > 0:
            for plugin in matches:
                if plugin not in plugins_array:
                    plugins_array.append(plugin)
            for i in range(len(plugins_array)):
                return plugins_array[i]
    

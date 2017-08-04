# -*- coding: utf-8 -*-

# Scrapy settings for spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'spider'

SPIDER_MODULES = ['spider.spiders']
NEWSPIDER_MODULE = 'spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
]

#PROXIES = [
#	{'ip_port': '111.207.228.252:8080', 'user_pass': ''},
#	{'ip_port': '117.143.109.165:8080', 'user_pass': ''},
#	{'ip_port': '111.47.219.50:8081', 'user_pass': ''},
#	{'ip_port': '123.206.226.186:8088', 'user_pass': ''},
#	{'ip_port': '210.13.74.154:8080', 'user_pass': ''},
#	{'ip_port': '112.124.23.110:8080', 'user_pass': ''},
#]


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}
DEFAULT_REQUEST_HEADERS = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'deflate',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':' PHPSESSID=2g0pr03qjs267pqum5digcfjp3; SH_nlist=%7B%2260345145%22%3A%7B%22id%22%3A%2260345145%22%2C%22sell_price%22%3A1490%2C%22title%22%3A%22%5Cu5609%5Cu5b9a%5Cu5609%5Cu5b9a%5Cu65b0%5Cu57ce11%5Cu53f7%5Cu7ebf%5Cu767d%5Cu94f6%5Cu8def%5Cu76d8%5Cu53e4%5Cu5609%5Cu5fb74%5Cu5c45%5Cu5ba4-%5Cu5357%5Cu5367%22%2C%22add_time%22%3A1501836972%2C%22usage_area%22%3A13.2%2C%22floor%22%3A%2212%22%2C%22floor_total%22%3A%2220%22%2C%22room_photo%22%3A%22g2%5C%2FM00%5C%2F33%5C%2F4D%5C%2FChAFfVlbpgKAMadBAAK50fbezRc567.jpg%22%2C%22city_name%22%3A%22%5Cu4e0a%5Cu6d77%22%7D%2C%2260614920%22%3A%7B%22id%22%3A%2260614920%22%2C%22sell_price%22%3A3990%2C%22title%22%3A%22%5Cu6d66%5Cu4e1c%5Cu6d0b%5Cu6cfe6%5Cu53f7%5Cu7ebf%5Cu5fb7%5Cu5e73%5Cu8def%5Cu6cfe%5Cu4e1c%5Cu5c0f%5Cu533a1%5Cu5c45%5Cu5ba4-%5Cu5357%5Cu5367%22%2C%22add_time%22%3A1501833276%2C%22usage_area%22%3A10.6%2C%22floor%22%3A%2206%22%2C%22floor_total%22%3A%226%22%2C%22room_photo%22%3A%22g2%5C%2FM00%5C%2F45%5C%2F6B%5C%2FChAFfVl5zYCANm-SAAIHch8QfBY929.JPG%22%2C%22city_name%22%3A%22%5Cu4e0a%5Cu6d77%22%7D%7D; CURRENT_CITY_NAME=%E4%B8%8A%E6%B5%B7; mapType=%20; CURRENT_CITY_CODE=310000',
    'Host':'sh.ziroom.com',
    'Upgrade-Insecure-Requests':'1',
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    #'spider.middlewares.SpiderSpiderMiddleware': 543,
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'spider.middlewares.RandomUserAgentMiddleware': 900,
#    'spider.middlewares.RandomProxyMiddleware': 901,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725, 
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

SPLASH_URL = 'http://192.168.253.141:8050'
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'spider.pipelines.SpiderPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'


# 默认Item并发数：100
CONCURRENT_ITEMS = 100
# 默认Request并发数：16
CONCURRENT_REQUESTS = 16
# 默认每个域名的并发数：8
CONCURRENT_REQUESTS_PER_DOMAIN = 8
# 每个IP的最大并发数：0表示忽略
CONCURRENT_REQUESTS_PER_IP = 0




#REDIRECT_ENABLED = False #关掉重定向,不会重定向到新的地址 
#HTTPERROR_ALLOWED_CODES = [504,] #返回504时,按正常返回对待
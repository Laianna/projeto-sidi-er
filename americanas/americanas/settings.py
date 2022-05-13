# Scrapy settings for americanas project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'americanas'

SPIDER_MODULES = ['americanas.spiders']
NEWSPIDER_MODULE = 'americanas.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'americanas.middlewares.AmericanasSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'americanas.middlewares.AmericanasDownloaderMiddleware': 543,
#}
# PROXY_POOL_ENABLED = True

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400
    # 'rotating_proxies.middlewares.RotatingProxyMiddleware': 800,
    # 'rotating_proxies.middlewares.BanDetectionMiddleware': 800,
}


'''ROTATING_PROXY_LIST = [
    "92.42.8.23:4153",
    "1.0.173.138:4145",
    "151.106.17.125:1080",
    "116.162.157.253:4145",
    "185.17.134.149:61535",
    "109.238.222.1:4153",
    "181.48.15.227:9991",
    "170.78.92.30:5678",
    "103.78.254.78:80",
    "66.98.0.107:4673",
    "197.211.24.206:5678",
    "43.224.10.22:6667",
    "180.180.124.248:49992",
    "154.236.179.226:1981",
    "178.253.212.118:1080",
    "103.87.201.135:4145",
    "113.108.247.146:20086",
    "88.247.103.30:4153",
    "181.78.24.26:5678",
    "80.191.162.2:514",
    "159.65.106.46:9050",
    "122.116.29.68:4145",
    "176.241.82.149:5678",
    "51.254.49.255:27594",
    "109.122.86.234:4153",
    "188.18.10.140:5678",
    "217.117.142.25:3629",
    "203.153.113.238:5678",
    "45.166.135.6:4145",
    "125.25.204.117:14153",
    "103.166.191.202:5678",
    "185.104.94.244:4145",
    "142.11.236.172:9050",
    "202.65.158.237:83",
    "115.85.74.114:5678",
    "177.72.115.65:31164",
    "185.46.170.253:4145",
    "5.189.184.6:80",
    "197.82.166.158:1080",
    "79.106.246.174:4145",
    "176.236.232.65:9090",
    "103.145.162.179:4153",
    "84.236.185.247:61710",
    "213.74.191.35:1080",
    "191.253.198.205:5678",
    "1.4.198.60:4145",
    "212.102.103.134:4153",
    "77.46.138.38:8080",
    "203.98.76.64:5678",
    "45.173.6.201:999",
    "91.90.180.185:8080",
    "24.106.221.230:53281",
    "45.238.57.1:3629",
    "51.91.157.66:80",
    "31.146.161.194:5678",
    "139.255.45.67:5678",
    "191.5.205.164:5678",
    "190.196.176.5:60080",
    "12.144.254.185:9080",
    "103.210.29.201:31433",
    "193.29.63.45:57299",
    "119.93.123.229:4145",
    "151.106.13.219:1080",
    "58.82.154.3:8080",
    "197.248.249.147:5678",
    "70.82.75.118:4153",
    "80.244.234.23:1256",
    "41.220.114.154:8080",
    "87.98.221.94:1000",
    "190.216.56.177:4153",
    "91.202.230.219:8080",
    "213.21.56.20:4153",
    "118.174.14.65:44336",
    "202.148.12.90:51302",
    "8.218.213.95:10809",
    "61.255.239.33:8008",
    "103.135.50.36:8080",
    "110.77.149.50:5678",
    "27.72.59.99:5678",
    "125.141.133.99:556"
]'''



# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'americanas.pipelines.AmericanasPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

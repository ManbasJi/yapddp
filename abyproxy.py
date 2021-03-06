import requests

# 要访问的目标页面
# targetUrl = "http://test.abuyun.com"
# targetUrl = "http://proxy.abuyun.com/switch-ip"
targetUrl = "http://proxy.abuyun.com/current-ip"

# 代理服务器
proxyHost = "http-pro.abuyun.com"
proxyPort = "9010"

# 代理隧道验证信息
proxyUser = "H51Y75S0R7J605AP"
proxyPass = "04FFA59423F82295"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}

proxies = {
    "http": proxyMeta,
    "https": proxyMeta,
}

resp = requests.get(targetUrl, proxies=proxies)

print(resp.status_code)
print(resp.text)

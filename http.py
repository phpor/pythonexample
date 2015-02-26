import httplib2
import sys

url = "http://baidu.com/"
if len(sys.argv) > 1:
    url = sys.argv[1]

h = httplib2.Http()
headers, body = h.request(url)
print body

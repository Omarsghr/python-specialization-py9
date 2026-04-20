 urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
# ignore ssl certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input("enter: ")
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
# retrieve all of the anchor tags
tags = soup("span")
total_sum = 0
counts = 0
for tag in tags:
    sum = int(tag.contents[0])
    total_sum += sum
    counts += 1
   # print('TAG:', tag)
   # print('URL:', href)
   # print('Contents:', text)
    # "print('Attrs:', tag.attrs)
   # print('-' * 20)  # Visual separator

print(" counts: ", counts)
print("  sum: ", total_sum)
#Initial version of the scraper

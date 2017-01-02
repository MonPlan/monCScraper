from lxml import html
import time
import requests

#alphabet = '01234ABCDEFLMPS'
alphabet = '01234ABCDEFLMPS'.lower()
l = []
links = []

for letter in alphabet:
    html_file = open("{:s}.html".format(letter), "r")
    tree = html.fromstring(html_file.read())
    l += tree.xpath('//*[@id="content_page"]/div/div/div[2]/div[2]/div[3]/ul/li//text()')
    links += tree.xpath('//*[@id="content_page"]/div/div/div[2]/div[2]/div[3]/ul/li/a/@href')

print(l)
print(links)

url = "http://monash.edu.au/pubs/2017handbooks/courses/{:s}"

for link in links:
    print("Getting {:s}".format(link))
    page = requests.get(url.format(link))
    html_file = open(link, "w")
    html_file.write(page.text)
    html_file.close()
    print("Done. Delay set to 5 seconds...")
    time.sleep(5)

quit()
print("---------------")
tree = html.fromstring(page.content)
print(tree.xpath('//*[@id="content_page"]/div/div/div[2]/div[2]/div[2]/ul/text()'))



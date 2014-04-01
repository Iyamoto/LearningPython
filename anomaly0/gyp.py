import re
import os
import urllib.request
from urllib.parse import urlparse
import hashlib

def file2text(path):
    """Reads utf-8 file from path"""    
    path = str(path)
    import codecs
    f = codecs.open(path, 'r', encoding='utf-8')
    text = f.read()
    f.close()
    return text

def getLinks(text):
    assert type(text)==str
    links = re.findall(r'<a href="(http[^"]+data.txt)',text)
    return links

def saveUrlsfromSerp(filepath):
    files = []
    for i in range(3):
        files.append('serp'+str(i)+'.html')
    f = open(filepath,'w')
    for file in files:
        html = file2text(file)
        links = getLinks(html)
        for link in links:
            f.write(link+'\n')
    f.close()        
    return None

def file2list(path):   
    path = str(path)
    list = []
    f = open(path, 'rU')
    for line in f:
        list.append(line)
    f.close()
    return list

def getDomain(url):
    BaseUrl = urlparse(url).netloc
    #tmp = BaseUrl.split('.')
    #BaseUrl = tmp[-2]+'.'+tmp[-1]
    return BaseUrl

def getID(s):
    assert type(s)==str
    id = hashlib.md5(s.encode('utf-8')).hexdigest()
    return id

#saveUrlsfromSerp('urls.txt')

urls = file2list('urls.txt')
urls.sort()
print(len(urls))
datadir = 'R:\\lucid\\anomaly\\0\\data\\'

for url in urls:
    domain = getDomain(url)
    id = getID(domain)
    print(url, domain, id)
    if os.path.isfile(os.path.join(datadir, id)) == False:
        try:
            urllib.request.urlretrieve(url, os.path.join(datadir, id))
        except urllib.error.HTTPError:
            print('error')
    
        




    

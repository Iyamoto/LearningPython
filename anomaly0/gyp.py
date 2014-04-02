import re
import os
import urllib.request
from urllib.parse import urlparse
import hashlib
import subprocess
import socket

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

def getIndex1(items):
    return items[1]
def getIndex2(items):
    return items[2]

def showData(data):
    for item in data:
        print(item)
    return None

def getUniq(filepath):
    cmd = 'wc '+filepath
    output=subprocess.check_output(cmd, shell=True)
    uniq = int(output.split()[0])
    #print(uniq)
    return uniq

def getWhois(domain, cachedir):
    cachefile = os.path.join(cachedir, domain)
    if os.path.isfile(cachefile) == True:
        lines = file2list(cachefile)
    else:
        cmd = 'whois '+domain
        output=subprocess.check_output(cmd, shell=True)
        s = output.decode()
        lines = s.splitlines()
        f = open(cachefile,'w')
        f.write(s)
        f.close()
    return lines

def getCreationDate(domain, cachedir):
    lines = getWhois(domain, cachedir)
    date = ''
    for line in lines:
        if line.find('Creation Date')>=0:
            date = line.split(':')[1].strip()
    return date

def getIP(host):
    try:
        ips = socket.gethostbyname_ex(host)
    except socket.gaierror:
        ips=[]
    return ips[2][0]

def getIndex(url, indexfile):
    url = url.strip()
    parts = url.split('/')
    url = ''
    for part in parts[:-1]:
        url+=part+'/'
    if os.path.isfile(indexfile) == False:
        try:
            urllib.request.urlretrieve(url, indexfile)          
        except urllib.error.HTTPError:
            print('error')
    print(url)
    return None

def isDate(part):
    if part.count('-')==2:
        return True
    else:
        return False

def getFileDate(indexfile):
    lines = file2list(indexfile)
    for line in lines:
        if line.find('data.txt')>=0:
            parts = line.strip().split()
            for part in parts:
                if isDate(part):
                    return part
    return None

def save2csv(data, filepath, sep=';'):
    f = open(filepath,'w')
    top = 'id;Domain;size;uniqs;domain creation_date;ip;file_date;\n'
    f.write(top)
    for items in data:
        s = ''
        for item in items:
            s=s+str(item)+sep
        f.write(s+'\n')
    f.close()
    return    

#saveUrlsfromSerp('urls.txt')

urls = file2list('urls.txt')
urls.sort()
print(len(urls))

basedir = 'R:\\lucid\\anomaly\\0\\'
datadir = os.path.join(basedir, 'data')
sorteddir = os.path.join(basedir, 'sorted')
uniqdir = os.path.join(basedir, 'uniq')
cachedir = os.path.join(basedir, 'cache')
indexdir = os.path.join(basedir, 'indexes')

csvfile = 'save.csv'

data = []

for url in urls:
    domain = getDomain(url)
    id = getID(domain)
    # TODO get date from index
    # TODO get domain whois
    # TODO get IP
    datafile = os.path.join(datadir, id)
    # Retrieving
##    if os.path.isfile(datafile) == False:
##        try:
##            urllib.request.urlretrieve(url, datafile)          
##        except urllib.error.HTTPError:
##            print('error')
##            continue
    if os.path.isfile(datafile) == True:
        size = os.path.getsize(datafile)
        sortedfile = os.path.join(sorteddir, id)
        uniqfile = os.path.join(uniqdir, id)
        indexfile = os.path.join(indexdir, id)
        # Sorting
##        cmd = 'sort '+datafile+' > '+sortedfile
##        subprocess.call(cmd, shell=True)
        # Uniq
##        cmd = 'uniq '+sortedfile+' > '+uniqfile
##        subprocess.call(cmd, shell=True)
        uniq = getUniq(uniqfile)
        creation_date = getCreationDate(domain, cachedir)
        ip = getIP(domain)
        # Get indexes
        #getIndex(url, indexfile)
        if os.path.isfile(indexfile) == True:
            file_date = getFileDate(indexfile)
        else:
            file_date = None
        #break
        data.append((id, domain, size, uniq, creation_date, ip, file_date))

#print(('id','Domain','size','uniqs', 'domain creation_date', 'ip', 'file_date'))                
#showData(sorted(data,key=getIndex1, reverse=True))
# TODO save to csv
save2csv(sorted(data,key=getIndex2, reverse=True),csvfile)
print('done')            
    
        




    

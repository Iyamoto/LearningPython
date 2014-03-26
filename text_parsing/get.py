#Learning to parse text in Python

url = 'http://spisok.mobi/%D0%BF%D0%BE%D0%BB%D0%BD%D1%8B%D0%B9-%D1%81%D0%BF%D0%B8%D1%81%D0%BE%D0%BA-%D0%B6%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D1%85-%D0%B8%D0%BC%D0%B5%D0%BD-%D0%B8-%D0%B8%D1%85-%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D1%8F.html'
#url = 'https://vk.com/'
html = 'F:\\tmp\\py\\test.html'
png = 'F:\\tmp\\py\\page.png'

def url2file(url, html, png):
    """PhantomJS wrapper
    url - http://name.tld
    html - where to save page code (html)
    png - where to save rendered page (image)"""
    import subprocess
    code = subprocess.call(['save.cmd', url, html, png])
    return code

def file2text(path):
    """Reads utf-8 file from path"""    
    path = str(path)
    import codecs
    f = codecs.open(path, 'r', encoding='utf-8')
    text = f.read()
    f.close()
    return text

url2file(url, html, png)
text = file2text(html)
print(text)

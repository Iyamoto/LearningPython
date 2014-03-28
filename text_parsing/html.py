def file2text(path):
    """Reads utf-8 file from path"""    
    path = str(path)
    import codecs
    f = codecs.open(path, 'r', encoding='utf-8')
    text = f.read()
    f.close()
    return text

def rebuild(id, items):
    print('Start of:',id)
    for child in items[id].getchildren():
        #print(child.attrib)
        if child.tag=='a':
            if child.attrib.has_key('href'):
                print(child.attrib['href'])
            if child.attrib.has_key('title'):
                print(child.attrib['title'])
        if child.text!=None:
            print(child.text)
    #items[id].text_content()
    print('End of:',id)
    print()
    return None

path = 'F:\\tmp\\py\\test.html'
text = file2text(path)
#print(text)

data = {}
items = {}

from lxml import html
tree = html.document_fromstring(text)
id=0
c=0
for element in tree.body.iter():
    items[id] = element
    pool = ()
    save = False
    a=0
    for child in element.getchildren():
        if len(element.getchildren())>2:# Filter by amount of tags
            pool += (child.tag,)
            if child.tag == 'a':# Filter by tag (a href)
                save = True
                a+=1
    if save and a==1:
        data[id] = data.get(id,(element.tag,)) + pool
        c+=1
    id+=1
print('Good blocks:',c)   
#for k,v in data.items(): print(k,v)

for id in data.keys():
    rebuild(id,items)

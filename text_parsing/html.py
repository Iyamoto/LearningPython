def file2text(path):
    """Reads utf-8 file from path"""    
    path = str(path)
    import codecs
    f = codecs.open(path, 'r', encoding='utf-8')
    text = f.read()
    f.close()
    return text

def rebuild(id, items):
    for child in items[id].getchildren():
        if child.tag=='a':
            print(child.attrib['href'])
            print(child.attrib['title'])
        if child.text!=None:
            print(child.text)
    items[id].text_content()        
    return None

path = 'F:\\tmp\\py\\test.html'
text = file2text(path)
#print(text)

data = {}
items = {}

from lxml import html
tree = html.document_fromstring(text)
id=0
for element in tree.body.iter():
    items[id] = element
    pool = ()
    save = False
    
    for child in element.getchildren():
        if len(element.getchildren())>2:# Filter by amount of tags
            pool += (child.tag,)
            if child.tag == 'a':# Filter by tag (a href)
                save = True
    if save:
        data[id] = data.get(id,(element.tag,)) + pool
    id+=1
   
#for k,v in data.items(): print(k,v)

rebuild(671,items)

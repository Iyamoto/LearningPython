import hashlib

def byte(x): 
    import io 
    s = io.BytesIO() 
    s.write(bytearray((x,))) 
    return s.getvalue() 

def getBEGUID(s):
    """Give me Steam ID
    Take Battle Eye GUID"""
    assert type(s)==str
    steamid = int(s)
    tmp = b'BE'
    for i in range(8):
        tmp += byte(steamid & 0xFF)
        steamid >>= 8
    guid = hashlib.md5(tmp).hexdigest()
    return guid

#testing    
steamid = '76561198057447143'
guid = 'd4d20ab6f6e413c129a2bcbaa17677e5'
rez = getBEGUID(steamid)
if rez==guid:
    print('well done')
    print(rez)
else:
    print('blablabla')


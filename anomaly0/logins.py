import os
id = 'a7834b8acd01611ddaf36c8cb553ab56'
basedir = 'R:\\lucid\\anomaly\\0\\'
uniqdir = os.path.join(basedir, 'uniq')
loginsdir = os.path.join(basedir, 'logins')
grep = os.path.join(uniqdir, id)
out = os.path.join(loginsdir, id)

f = open(grep,'rU')
count = {}
good = {}
last = ''

for line in f:
    pair = line.strip().split(':')
    if len(pair)==2:
        login = pair[0].lower()
        if len(login)==0:
            continue
        if login!=last:            
            pas = pair[1]
            if len(pas)<10:
                continue
            if login==pas:
                continue
            count[login] = count.get(login, 0) + 1
            #print(login, last,count[login])
            if count[login]==1:
                good[pair[0]] = pas
                last = login
            elif count[login]>1:
                last = login
                del(good[last])

f.close()    

#print(good)

f = open(out,'w')
for k,v in good.items():
    f.write(k+':'+v+'\n')

f.close()    
    

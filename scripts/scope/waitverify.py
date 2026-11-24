import os,time,sys
start=time.time()
def last():
    m=0
    for r,d,f in os.walk('content/en'):
        for x in f: m=max(m,os.path.getmtime(os.path.join(r,x)))
    return m
began=False
for i in range(58):
    l=last()
    if l>start: began=True
    if began and time.time()-l>int(sys.argv[1]): print('quiet'); break
    time.sleep(10)
else: print('still going', began)

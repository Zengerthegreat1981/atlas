import time,sys,os
SP='C:/Users/HP/AppData/Local/Temp/claude/19ef3e7a5f94f486/9f724022-fc83-42d3-8ed5-4fb83c1b342c/scratchpad'
L=[l.split('|')[2] for l in open(f'{SP}/{sys.argv[1]}').read().split('\n') if l]
for i in range(58):
    n=sum(os.path.exists(x) for x in L)
    if n>=len(L): break
    time.sleep(10)
print('written',n,'of',len(L))

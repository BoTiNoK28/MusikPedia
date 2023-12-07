from fnmatch import fnmatch
for i in range(0,10**8,273):
    k=str(i)
    if fnmatch(k,'12??36*1'):
        print(i,i//273)

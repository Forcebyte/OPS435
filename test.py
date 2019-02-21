def wc(file):
    f = open(file,'r').read()
    test = f.gettype()
    print(test)
    for c in '!@#$%^&*()_-+=[].,:;?':
        f = f.replace(c,'')
    f = f.replace('\n','')
    word = f.lower().split()
    s = set(word)
    a = len(word)
    d = len(s)
    return a, d

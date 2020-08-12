import string
from bruteforce.binarysearch import bruteforce,MORE,LESS,EQUALS

def brute(s, charset):
    password = "Hello123pytho3"
    if len(s)>len(password):
        return MORE
    i=charset.index(s[len(s)-1])
    i2=charset.index(password[len(s)-1])

    if i<i2:
        return MORE
    elif i2<1:
        return LESS
    else:
        return EQUALS

    print(bruteforce(brute,string.ascii_letters+string.digits))

from base64 import b64encode
from base64 import b64decode
import binascii
import itertools
  
def xor(text,key):
  new_text=list(text)
  for i in range(len(text)):
    new_text[i]=key[i%len(key)]^text[i]
  return bytes(new_text)


# Check base64
def check(num):
    # A - Z
    if((num >= 65) and (num <= 90)):
        return True
    # a - z
    if((num >= 97) and (num <= 122)):
        return True
    # 0 - 9
    if((num >= 48) and (num <= 57)):
        return True
    # + / = 
    if((num == ord('+')) or (num == ord('/')) or (num == ord('='))):
        return True
    return False

def calc(num):
    ret = list()
    for i in range(0, 256):
        if(check(num ^ i)):
            ret.append(i)
    return ret

cipher='Dq4l/8bPnCsynznU2relLC+oGsq+xIBhBrgF+ZKHgjkM6yrxxsOyDzLuB4mDp6kHKZYkyqWf+HIGqDv1xITzJhutD/nGkpwoMp89y82doQcshjjKubX9cwbpAdudk7gGA+lY7I+8+R4umAOKho65CDOsO82lnJx/BrgJyZjA/ycOvg/qwMOYEzCkPdWEgeQMcOUJyLmMjCURkUPbnZeGPA+6WIU='

onelv = b64decode(cipher.encode())

for le in range(7, 14):
    ok = True
    gao = list("A" * le)
    for i in range(0, len(onelv)):
        possSet = calc(onelv[i])
        if(gao[i % le] == 'A'):
            gao[i % le] = possSet
        else:
            x = set(gao[i % le])
            y = set(possSet)
            z = x.intersection(y)
            z = list(z)
            if(len(z) == 0):
                ok = False
                break
            gao[i % le] = z
    if(ok):
        print(le)
        x = list(itertools.product(*gao))
        for xx in x:
            print(xor(b64decode(xor(onelv, xx)), xx))
        



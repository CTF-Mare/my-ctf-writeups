text_list=' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\t\n'

cipher=open('cipher.txt','r').read()

xxxx = [('e', 1), ('o', 1), ('a', 1), ('s', 1)]


def encrypt(s,k):
    out=''
    for i in range(len(s)):
        index=text_list.index(s[i])
        index*=k[i%len(k)]
        index%=97
        out+=text_list[index]
    return out

def decrypt(c,k):
    s=''
    for i in range(len(c)):
        index=text_list.index(c[i])
        index*=pow(k[i%len(k)], 95, 97)
        index%=97
        s+=text_list[index]
    return s


def gao(l):
    w = [[0 for j in range(97)] for i in range(l)] 
    for i in range(len(cipher)):
        for c, p in xxxx:
            index = text_list.index(cipher[i]) * pow(text_list.index(c) ,95, 97) % 97
            if index:
                w[i % l][index] += p
    key = [w[i].index(max(w[i])) for i in range(l)]
    print(decrypt(cipher, key))
    return key

for key_len in range(15,30):
    print(gao(key_len))


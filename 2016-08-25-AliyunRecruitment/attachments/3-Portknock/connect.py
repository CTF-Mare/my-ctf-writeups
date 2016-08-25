# 1234 -> 2713 -> 6350 -> 6175 -> 8764

from zio import *

port_list = [1234, 2713, 6350, 6175, 8764]

def calc(a1, a2):
    ret = 0
    if a2 & 1:
        ret = 4 * (a2 + 1) + 2 + a1
    else:
        ret = a1 * (((a2 + 2) >> 1) + 2)
    return ret

for i in xrange(5):
    print i
    io = zio(("114.215.211.232", port_list[i]), print_read=COLORED(RAW), print_write=COLORED(RAW, 'green'))
    
    gao = io.read(4)
    res = calc(l32(gao), i)
    payload = l32(res)
    io.write(payload)
    
io.interact()

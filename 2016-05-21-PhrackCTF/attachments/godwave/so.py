#!/usr/bin/env python

import wave
from PIL import Image
#matplotlib.pyplot as plt

wav = wave.open('godwave.wav' , 'rb')

a = wav.readframes(-1)
n = len(a) // 4

def getdata():
	for i in range(n):
		s = a[i*4: (i+1)*4]
		v = ord(s[0]) + (ord(s[1]) << 8) + (ord(s[2]) << 16) + (ord(s[3])<<24)
		yield v if v < (1<<31) else v - (1<<32)

def printtu(imWidth, imHeight):
    gao = Image.new("RGB", (imHeight, imWidth))

    for i in range(m):
    	if(b[i] == 1):
            xxxx = int(i / imWidth)
            yyyy = i % imWidth
            #print(xxxx)
            #print(yyyy)
            gao.putpixel([xxxx, yyyy], (255, 255, 255))

    gao.show()

a = list(map(abs, getdata()))


h = 32
l = h * 2

m = n // l

print(n / l, m)

b = []



for i in range(m):
	u = a[i * l : (i + 1) * l]
	le, ri = sum(u[:h]) , sum(u[h:])
	#plt.plot(range(l), u)
	#plt.show()
	assert(le * 10 < ri or le > ri * 10)
	#b.append(1 if le * 10 < ri else 0)
        b.append(0 if le * 10 < ri else 1)

s = m // 8

#for i in range(m - 1):
#	b[i+1] ^= b[i]


k1 = "".join(map(str,b))
f = open("finwave.bin", "w")
for i in range(0, m, 8):
    f.write(chr(int(k1[i:i+8],2)))
f.close()


#for i in xrange(13560):
#    print i
#    imWidth = i + 1
    #if 13560 % imHeight != 0:
    #    continue
    #imWidth = 13560 / imHeight
#    imHeight = int(13560 / imWidth) + (13560 % imWidth != 0)

#printtu(13560 / 5, 5)


#r  = ''
#for i in range(s):
#	t = b[i * 8 : i * 8 + 8]
#	#print(t)

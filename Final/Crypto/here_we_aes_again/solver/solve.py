from pwn import *

while True:
    r = remote("localhost", 5000)

    r.recvuntil("admin code : ")
    admin_code = r.recvline()[:-1].decode()
    
    r.sendlineafter("> ", "1")

    r.sendlineafter("(in hex) : ", "0"*len(admin_code))
    r.recvline()
    first_tag = r.recvline()[:-1].decode().split("Tag : ")[1]

    r.sendlineafter("> ", "1")

    r.sendlineafter("(in hex) : ", "0"*(len(admin_code)-1) + "1")
    r.recvline()
    second_tag = r.recvline()[:-1].decode().split("Tag : ")[1]

    r.sendlineafter("> ", "1")

    r.sendlineafter("(in hex) : ", admin_code[:-2] + hex(int(admin_code[-2:],16)-1).replace("0x",""))
    fake_cipher = r.recvline()[:-1].decode().split("Code : ")[1]
    third_tag = r.recvline()[:-1].decode().split("Tag : ")[1]
    
    final_tag = hex(int(first_tag, 16) ^ int(second_tag, 16) ^ int(third_tag, 16)).replace("0x", "")
    final_cipher = fake_cipher[:-2] + hex(int(fake_cipher[-2:],16)-1).replace("0x","")

    r.sendlineafter("> ", "2")
    r.sendlineafter(": ", final_cipher)
    r.sendlineafter(": ", final_tag)

    result = r.recv()

    if b"JOINTS21{" in result:
        print(result)
        exit()

    r.close()
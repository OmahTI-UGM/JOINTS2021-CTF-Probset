#!/usr/bin/env python3

from Crypto.Cipher import AES
import os
import sys

import sys

class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def writelines(self, datas):
       self.stream.writelines(datas)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)

def encrypt(plain, key, nonce):
    aes_obj = AES.new(key, AES.MODE_GCM, nonce)
    return aes_obj.encrypt_and_digest(plain)

def decrypt(enc, key, nonce, tag):
    aes_obj = AES.new(key, AES.MODE_GCM, nonce)
    try:
        return aes_obj.decrypt_and_verify(enc, tag)
    except:
        return None


print("""===========================
Super Secret Agent Service
===========================
""")

flag = open("flag.txt").read()
key = os.urandom(16)
nonce = os.urandom(16)
admin_code = os.urandom(16)

print(f"Here is the admin code : {admin_code.hex()}")
print("But here, we implement tag as 2fa for admin\n")
print("""Menu :
1. Generate Encrypted Code
2. Enter as agent""")

while True:
    try:
        choice = input("> ")

        if choice == "1":
            code = input("Code (in hex) : ")
            code = bytes.fromhex(code)
            
            if code == admin_code:
                print("You can't generate encrypted admin code !")
            
            enc_code, code_tag = encrypt(code, key, nonce)
            print(f"Encrypted Code : {enc_code.hex()}")
            print(f"Code Tag : {code_tag.hex()}")

        elif choice == "2":
            enc_code = input("Encrypted Code (in hex) : ")
            code_tag = input("Code Tag (in hex) : ")
            enc_code = bytes.fromhex(enc_code)
            code_tag = bytes.fromhex(code_tag)

            verify = decrypt(enc_code, key, nonce, code_tag)
            
            if verify == admin_code:
                print(f"Welcome admin, here is your flag : {flag}")
                exit()
            else:
                print("Welcome agent, have fun here :)")

        else:
            print("Invalid Choice !")
        
    except:
        print("Something Error !")
            
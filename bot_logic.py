import random

def gen_pass(pass_length):
    karakter="qwertyuiop12345<>?:=-"
    sandi=" "
    for i in range(pass_length):
        sandi += random.choice(karakter)
    print(sandi)
gen_pass(10)
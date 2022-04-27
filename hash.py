import hashlib
import blake512
import blake3
import groestlcoin_hash2
import skein
import sha3
import gostcrypto
import whirlpool
import sm3_hash

def RIPEMD160(binary_text):
    hashed=hashlib.new('ripemd160')
    hashed.update(binary_text)
    return hashed.hexdigest()

switcher = {
1: hashlib.md5,
2: hashlib.sha1,
3: hashlib.sha256,
4: blake512.hash,
5: hashlib.blake2b,
6: hashlib.blake2s,
7: blake3.blake3,
8: groestlcoin_hash2.groestl_hash,
9: skein.skein256,
10: skein.skein512,
11: skein.skein1024,
12: sha3.keccak_256,
13: gostcrypto.gosthash.new,
14: whirlpool.new,
15: RIPEMD160,
16: sm3_hash.sm3_hash,
}
names={
1: " md5",
2: " sha1",
3: " sha256",
4: " Blake 1 512",
5: " Blake 2b",
6: " Blake 2s",
7: " Blake 3",
8: " Grøstl (Groestl)",
9: " Skein 256",
10: "Skein 512",
11: "Skein 1024",
12: "Keccak 256",
13: "GOST",
14: "Whirlpool",
15: "RIPEMD 160",
16: "SM3"
}
def default(text):
    return "You haven't selected any function!\nYou have entered text:{}".format(text.decode("utf-8"))
def switch(hash,text):
    if hash==13:
        return switcher.get(hash, default)('streebog256',data=text)
    return switcher.get(hash, default)(text)

if __name__=="__main__":
    text=input("say something:\n> ").encode("utf-8")
    print("---\nwhich one?:")
    for name in names:
        print(" {}. {}".format(name, names[name]))

    select=int(input("> "))
    hash_obj=switch(select,text)
    print("___________----____________")
    try:
        print("the {} hash of {} is:".format(names[select],text.decode("utf-8")))
    except:
        pass
    try:
        hash_obj=hash_obj.hexdigest()
    except:
        try:
            hash_obj=hash_obj.hex()
        except:
            pass
    print(hash_obj)
    print("-----------____------------")
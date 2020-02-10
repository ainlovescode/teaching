'''
Exercise 1

by @ainlovescode
'''
import hashlib
import time
### Q1 ###

TARGET = "Blockchain Technology".encode("utf-8")

print("SHA2-256: " + hashlib.sha256(TARGET).hexdigest())
print("SHA2-512: " + hashlib.sha512(TARGET).hexdigest())
print("SHA3-256: " + hashlib.sha3_256(TARGET).hexdigest())
print("SHA3-512: " + hashlib.sha3_512(TARGET).hexdigest())

### Q2 ###
hashes = {}

def H(n, msg):
    return hashlib.sha512(msg.encode("utf-8")).digest()[:n]

for num in range(1, 6):
    start, end, msg = time.time(), None, 0
    while end == None:

        hashval = H(num, str(msg))
        if hashes.get(hashval):
            end = time.time()
        else:
            hashes[hashval] = str(msg)
            msg += 1
    print("{} - collision found after {} seconds".format(num, str(end - start)))

print("complete)")
        




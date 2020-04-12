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

print("Preimage is some x' such that hashvalue = h(x')")
hash_of_preimages = [b"\x00", b"\x00"*2, b"\x00"*3, b"\x00"*4, b"\x00"*5]
for num in range(1, 6):
    start, end, msg = time.time(), None, 0
    while end == None:
        hashval = H(num, str(msg))
        if (hashes.get(hashval) 
            and hashval in hash_of_preimages):
            end = time.time()
        else:
            hashes[hashval] = str(msg)
            msg += 1
    print("{} - preimage found after {} seconds".format(num, str(end - start)))

## Finding a preimage takes much longer than finding a collision
## because while many inputs can generate the same hash, the converse is true vice versa


"""
## Q3 ##   

Generate key pairs for ECDSA and sign the string `"Blockchain Technology"`
using this signature scheme with the generated key. Then verify the obtained
signature.

**Note:** the `ecdsa` package uses NIST192p as the default elliptic curve, but in
real applications a longer/more secure curve should be considered.


import ecdsa

signing_key = ecdsa.SigningKey.generate()
verifying_key = signing_key.get_verifying_key()

signature = signing_key.sign(b"Blockchain Technology")
print(verifying_key.verify(signature, b"Blockchain Technology"))


## Q4 ##
from datetime import datetime
import json
from ecdsa import VerifyingKey
 
class Transaction:
    def __init__(self, sender, receiver, amount, comment):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.comment = comment
        self.signature = None

    @classmethod
    def new(cls, sender, receiver, amount, comment, signature = None):
        # Instantiates object from passed values
        tx = cls(sender, receiver, amount, comment)
        senderPrivKey = sender.get_verifying_key()
        tx.sign(False)

    def serialize(self, isSigned = True):
        """
        # Serializes transaction information into JSON
        """
        tx = {
            "senderKey": self.sender.to_string().hex(),
            "receiverKey": self.receiver.to_string().hex(),
            "amount": self.amount,
            "comment": self.comment,
        }

        if isSigned:
            tx["signature"] = self.signature.hex()

        return json.dumps(tx)

    @classmethod
    def deserialize(cls, obj):
        # Instantiates/Deserializes object from CBOR or JSON string
        deserialized = json.loads(obj)

        senderKey = VerifyingKey.from_string(bytes.fromhex(deserialized["senderKey"]))
        receiverKey = VerifyingKey.from_string(bytes.fromhex(deserialized["receiverKey"]))
        amount = deserialized["amount"]
        comment = deserialized["comment"]

        signature = bytes.fromhex(deserialized["signature"]) if deserialized["signature"] else None

        tx = cls(senderKey, receiverKey, amount, comment)
        tx.signature = signature

        if tx.validate():
            return tx
        elif not signature:
            raise Exception("ValidationError: Signature cannot be verified")
        else:
            raise Exception("ValidationError: Signature cannot be found")


    def sign(self, private_key):
        # Sign object with private key passed
        # That can be called within new()
        # just use ecdsa
        s = self.serialize(False)
        new_sign = private_key.sign(s.encode())
        self.signature = new_sign
        

    def validate(self):
        # Validate transaction correctness.
        # Can be called within from_json()
        # check signature = 
        sig = self.signature
        s = self.serialize(False)
        return self.sender.verify(sig, s.encode())

    def __eq__(self, other):
        # Check whether transactions are the same
        if (self.sender == other.sender
            and self.receiver == other.receiver
            and self.signature == other.signature
            and self.comment == other.comment
            and self.amount == other.amount):
            return True
        else:
            return False

"""

class MerkleTree(...):
    def __init__(self):
        self.tree = [[]]
        self.entries = []

    def add(self, entries):
        # Add entries to tree
        self.entries = entries
        print("{} entries have been added.".format(len(entries)))
        

    def build(self):
        # Build tree computing new root
        # given a list from oldest to youngest
        def merge_hash(left, right):
            left_hash = hashlib.sha512(left.encode("utf-8")).digest()
            right_hash = hashlib.sha512(right.encode("utf-8")).digest()

            merged_hash = hashlib.sha512((str(left_hash) + str(right_hash)).encode("utf-8")).digest()

        temp = [merge_hash(self.entries[i], self.entries[i + 1]) for i in range(len(self.entries) // 2)]
        if len(self.entries) > len(temp) * 2:
            temp.append(merge_hash(self.entries[-1], ""))

        while len(temp) > 1:
            num_of_pairs = len(temp) // 2

            extra = temp[-1] if len(temp) % 2 else None
            temp = [merge_hash(self.entries[i], self.entries[i + 1]) for i in range(num_of_pairs)]
            if extra:
                temp.append(merge_hash(extra, ""))
            
        
            








    def get_proof(...):
        # Get membership proof for entry
        # min no, of nodes to construct root
        ...

     def get_root(...):
        # Return the current root
        ...

def verify_proof(entry, proof, root):
    # Verify the proof for the entry and given root. Returns boolean.
    ...


import hashlib

def sha3(text = 'abc', length = 512):

    # Introduction
    """
    It is a function that encrypts words by Keccak (Security Hash Algorithm-3 (SHA-3)).
    """
    # Introduction

    if length == 224:
        m = hashlib.sha3_224()
    elif length == 256:
        m = hashlib.sha3_256()
    elif length == 384:
        m = hashlib.sha3_384()
    elif length == 512:
        m = hashlib.sha3_512()
    else:
        print(
f"""
Error:
    In function sha3(), argument 'length' invalid.
    It should be one of [224, 256, 384, 512], but it is {length}.
    Function sha3() Quitted.
""")
        return ''
    
    m.update(text.encode("utf-8"))
    return m.hexdigest()
    
def test():
    str = input("Please enter a character string for test: ")

    print(f"Encrypted string for '{str}' is:\n", sha3(str))

test()

import hashlib



def crack_sha1_hash(hash, use_salts = False):
    a = 0
    with open('top-10000-passwords.txt', 'r') as file:
        for line in file:
            if(not(use_salts)):
               pass
    return True
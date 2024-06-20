import hashlib

top_10000_passwords = []


def crack_sha1_hash(hash, use_salts=False):

    with open('top-10000-passwords.txt', 'r') as passwords_file:
        Lines = passwords_file.readlines()
        for line in Lines:
            top_10000_passwords.append(line.strip())

    hashed_passwords = {}

    for password in top_10000_passwords:
        encoded_password = password.encode()

        if not use_salts:
            hashed_password = hashlib.sha1(encoded_password).hexdigest()
            hashed_passwords[hashed_password] = password
            continue

       
        with open('known-salts.txt', 'r') as salts_file:
            Lines = salts_file.readlines()

            for line in Lines:
                salt = line.strip()
                encoded_salt = salt.encode()
              
                encoded_passwords_with_salt = [
                    encoded_salt + encoded_password, encoded_password + encoded_salt]

                for p in encoded_passwords_with_salt:
                    hashed_password = hashlib.sha1(p).hexdigest()
                    hashed_passwords[hashed_password] = password

    if hash in hashed_passwords:
        return hashed_passwords[hash]

    return 'PASSWORD NOT IN DATABASE'
import secrets

def gen_secret_key():
    secret_key = secrets.token_hex(32)
    return secret_key

if __name__ == "__main__":
    print(gen_secret_key())
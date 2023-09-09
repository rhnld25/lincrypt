import lincrypt

if __name__ == "__main__":
    #get key
    key = lincrypt.get_key()

    #
    lincrypt.encrypt(key, list_of_modules, encryption_idx)
from cryptography.fernet import Fernet

def get_key(key, Fernet=Fernet):
    if len(key) == 0: # if the key doesn't exist yet, generate a new key
        key = Fernet.generate_key()
    return key

def encrypt(key, list_of_modules, encryption_idx): #encryption_idx 
    encrypted_code_lines = []
    for module in list_of_modules:
        #grab raw code lines
        f = open(module, "w")

        #dump into list
        code_lines = list(f.readlines())
        
        #make key passable
        f = Fernet(key)

        #encrypt lines
        for i in range(len(code_lines)):
            if encryption_idx[i] == 1:
                line = f.encrypt(bytes(code_lines[i], "utf-8"))
            else:
                line = code_lines[i]
            encrypted_code_lines.append(line)

        toWrite = open(module, "w")
        toWrite.writelines(encrypted_code_lines)
        toWrite.close()
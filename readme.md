This is a library to be used for encrypting parts of a code under development. The code that needs to be encrypted must be put inside a python module, not main.py

The flow of the encryption is as such:
1. Load the library into main.py
2. Pass in the the names of the modules that needs to be encrypted
3. After the encryption commencement, create the key to encrypt the modules and keep it in a .pyc file locally, and replace the modules with the encrypted modules. (For development, backup the folders first into a separate directory)

The flow of the decription is as such:
1. Run the encryption flow first
2. Load the library into main.py
3. have a list of encrypted modules to decrypt
4. make a loop, to loop over the list of encrypted modules, inside the loop, there is a decrypt function, a tempfile creation function, and a section to load in the decrypted modules from the tempfile 
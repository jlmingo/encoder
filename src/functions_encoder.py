from Crypto.Cipher import AES
import pandas as pd

public_job_title="pv power plant manager"

def encrypt_text(data, key, dictionary_nonces):
    '''
    input: string to be encrypted
    output: text and nonce encrypted in hexadecimal
    global variables accessed: key (bytes), dictionary_nonces (dictionary) 
    '''
    if data != public_job_title:
        cipher = AES.new(key, AES.MODE_EAX)
        nonce = cipher.nonce
        data = str(data).encode()
        ciphertext = cipher.encrypt(data)
        dictionary_nonces[ciphertext.hex()] = nonce.hex()
        return ciphertext.hex()
    else:
        return data

def decrypt_text(data, key, dictionary_nonces):
    '''
    input: string in hexadecimal
    output: decrypted string
    '''
    if data != public_job_title:
        nonce=dictionary_nonces[data]
        cipher = AES.new(key, AES.MODE_EAX, nonce=bytes.fromhex(nonce))
        plaintext = cipher.decrypt(bytes.fromhex(data))
        return plaintext.decode()
    else:
        return data

def read_path(input_all_paths, denomination):
    df = pd.read_excel(input_all_paths, sheet_name="inputs")
    return df[df.denomination==denomination].path.iloc[0]
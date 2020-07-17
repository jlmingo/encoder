from functions_encoder import *
from Crypto.Random import get_random_bytes
import pandas as pd
import json

#declare excel file with path to all inputs
print("Reading paths from inputs.xlsx...")
input_all_paths = "./inputs.xlsx"

#obtain input file path
path_input_file = read_path(input_all_paths, "input_excel")

#declaring variables
dictionary_nonces = {}
encrypting_cols = ["Employee ID", "Employee Name", "Job Title"]
public_job_title="pv power plant manager"

#generate key
print("Generating random key")
key = get_random_bytes(16)
print("key: ", key)
with open("key.txt", "w") as f:
    f.write(key.hex())
    f.close

#reading dataframe
print("Generating dataframe from input Excel file")
df=pd.read_excel(path_input_file, dtype="str")

#encrypting selected columns. encrypt_text function updates dictionary_nonces
print("Encrypting data...")
df.loc[:, encrypting_cols] = df[encrypting_cols].applymap(lambda x: encrypt_text(x, key, dictionary_nonces))

#generating excel file
print("Generating encrypted excel file...")
df.to_excel("encrypted_file.xlsx", index=False)

#generating JSON file
print("Generating json with nonces...")
with open("nonces.json", "w") as f:  
    json.dump(dictionary_nonces, f)
from Crypto.Random import get_random_bytes
import pandas as pd
from functions_encoder import *
import json

#declare excel file with path to all inputs
print("Reading paths from inputs.xlsx...")
input_all_paths = "./inputs.xlsx"

#encrypted colummns
encrypting_cols = ["Employee ID", "Employee Name", "Job Title"]

#obtain paths
encrypted_file_path = read_path(input_all_paths, "encrypted_file")
key_path = read_path(input_all_paths, "key")
json_nonces_path = read_path(input_all_paths, "json")

#create dataframe
df = pd.read_excel(encrypted_file_path, dtype=dict(zip(encrypting_cols, ["str"]*len(encrypting_cols))), parse_dates=["Hire Date"])

#establish date format
df.loc[:,"Hire Date"]=df["Hire Date"].dt.strftime("%d/%m/%Y")

#obtain key
with open(key_path, "r") as f:
    key = bytes.fromhex(f.read())
    f.close()

#obtain nonces
with open(json_nonces_path, "r") as f:
    dictionary_nonces = json.load(f)
    f.close()
print("Decrypting file...")
df.loc[:, encrypting_cols] = df[encrypting_cols].applymap(lambda x: decrypt_text(x, key, dictionary_nonces))
df.to_excel("decrypted_file.xlsx", index=False)
print("Decrypted file generated.")
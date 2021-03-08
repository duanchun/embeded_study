from Crypto.Cipher import DES3
import base64
KEY = b'UO2FvZTA3s5GEEvAilwiTav2'
 
 
#def encrypt_data(data):

data = "123456789"
padLen = (8 - len(data) % 8)%8

str_bytes = bytearray(data, encoding = "utf8")

for i in range(padLen):
    str_bytes.append(0)

des3 = DES3.new(KEY, DES3.MODE_ECB)
des3_data = des3.encrypt(str_bytes)
base64_des3_data = base64.standard_b64encode(des3_data)
print(base64_des3_data)


def decrypt_data(data):
    base64_data = base64.standard_b64decode(data)
    des = DES3.new(KEY, DES3.MODE_ECB)
    decrypt_data = des.decrypt(base64_data)
    print(decrypt_data)
    return decrypt_data

decrypt_str = decrypt_data(str(base64_des3_data, encoding = "utf8") )
print (decrypt_str)    



from Crypto.Cipher import DES3
import base64
KEY = b'dqj3S4HXpJmmkzwYZGSmKFbr'
print(len(KEY))

#print(KEY.hex())
 

b=b'\x4E\x6F\x77\x20\x69\x73\x20\x74'
#print(b)
string=str(b,'utf-8')
#print(string)

KEY_T=b'\x01\x23\x45\x67\x89\xAB\xCD\xEF\
\x23\x45\x67\x89\xAB\xCD\xEF\x01\
\x45\x67\x89\xAB\xCD\xEF\x01\x23'
#string=str(KEY_T,'utf-8')
#print(KEY_T.hex())


#def encrypt_data(data):

data_e = "app_id=202120445967396126737&biz_content={\"create_ip\":\"10.127.111.179\",\"total_amount\":\"0.01\",\"out_order_no\":\"0\",\"body\":\"WHEATEK\",\"store_id\":\"100001\"}&method=trade.percreate&nonce=2139193777&sign_type=MD5&timestamp=2021-03-12 11:12:30"
print(data_e)
data = data_e.replace("\"",'\\\"')
print(data)
#data = b
padLen = (8 - len(data) % 8)%8
#padLen = (8 - len(data) % 8)

str_bytes = bytearray(data, encoding = "utf8")
#str_bytes = bytes(data, encoding = "utf8")


for i in range(padLen):
    str_bytes.append(0)

des3 = DES3.new(KEY, DES3.MODE_ECB)
des3_data = des3.encrypt(str_bytes)
#print(des3_data.hex())
#print('\r\n')
#print(des3_data)
#print('\r\n')
base64_des3_data = base64.standard_b64encode(des3_data)
print(base64_des3_data)


def decrypt_data(data):
    base64_data = base64.standard_b64decode(data)
    des = DES3.new(KEY, DES3.MODE_ECB)
    decrypt_data = des.decrypt(base64_data)
    print(decrypt_data.hex())
    return decrypt_data

#decrypt_str = decrypt_data(str(base64_des3_data, encoding = 'utf-8') )
#print (str(decrypt_str, encoding = 'utf-8') )    



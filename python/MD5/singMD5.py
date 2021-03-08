import Crypto.Cipher.DES3
import base64
import binascii
def auto_fill(x):
  if len(x) > 24:
    raise "密钥长度不能大于等于24位！"
  else:
    while len(x) < 16:
      x += " "
    return x.encode()
    
key = "jPMfmn5y5oHQ5lDxGlEeq4lh"
content = "date=20200501&mer_id=663101000017582&nonce=123456&store_id=100001&term_id=TID30559&term_model=S1&term_sn=SD110470T00100001&term_type=SMART_POS&timestamp=2020-05-05 11:11:1&vendor_code=WHEATEK"
x = Crypto.Cipher.DES3.new(auto_fill(key), Crypto.Cipher.DES3.MODE_ECB)
a = base64.encodebytes(x.encrypt(content.encode()))
print(a)
b = x.decrypt(base64.decodebytes(a))
print(b)


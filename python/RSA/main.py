#!/usr/bin/env python3
# coding=utf-8
# Author: Luosu201803
"""
create_rsa_key() - 创建RSA密钥
my_encrypt_and_decrypt() - 测试加密解密功能
rsa_sign() & rsa_signverify() - 测试签名与验签功能
"""

#https://www.cnblogs.com/kuzaman/p/8584200.html

from binascii import unhexlify
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5
import base64
from Crypto.Hash import SHA1
from Crypto.Signature import pkcs1_15

def create_rsa_key(password=None):
    """
    创建RSA密钥,步骤说明：
    1、从 Crypto.PublicKey 包中导入 RSA，创建一个密码(此密码不是RSA秘钥对)
    2、生成 1024/2048 位的 RSA 密钥对(存储在私钥文件和公钥文件)
    3、调用 RSA 密钥实例的 exportKey 方法(传入"密码"、"使用的 PKCS 标准"、"加密方案"这三个参数)得到私钥。
    4、将私钥写入磁盘的文件。
    5、使用方法链调用 publickey 和 exportKey 方法生成公钥，写入磁盘上的文件。
    """
    key = RSA.generate(1024)
    #encrypted_key = key.exportKey(passphrase=password, pkcs=8,protection="scryptAndAES128-CBC")
    encrypted_key = key.exportKey(passphrase=password, pkcs=1,protection="scryptAndAES128-CBC")
    # encrypted_key = key.exportKey(pkcs=1)
    print('encrypted_key:',encrypted_key)
    with open("my_private_rsa_key.pem", "wb") as f:
        f.write(encrypted_key)
    with open("my_rsa_public.pem", "wb") as f:
        f.write(key.publickey().exportKey())


def encrypt_and_decrypt_test(password=None):
    # 加载私钥用于加密
    recipient_key = RSA.import_key(
        open("my_rsa_public.pem").read()
    )
    cipher_rsa = PKCS1_v1_5.new(recipient_key)
    #使用base64编码保存数据方便查看，同样解密需要base64解码
    en_data = base64.b64encode(cipher_rsa.encrypt(b"123456,abcdesd"))
    print("加密数据信息：",type(en_data),'\n',len(en_data),'\n',en_data)

    # 加载公钥用于解密
    encoded_key = open("my_private_rsa_key.pem").read()
    private_key = RSA.import_key(encoded_key,passphrase=password)
    cipher_rsa = PKCS1_v1_5.new(private_key)
    data = cipher_rsa.decrypt(base64.b64decode(en_data), None)
    print(data)

def rsa_sign(message,password=None):
    #读取私钥信息用于加签
    private_key = RSA.importKey(open("my_private_rsa_key.pem").read(),passphrase=password)
    hash_obj = SHA1.new(message)
    # print(pkcs1_15.new(private_key).can_sign())  #check wheather object of pkcs1_15 can be signed
    #base64编码打印可视化
    signature = base64.b64encode(pkcs1_15.new(private_key).sign(hash_obj))
    return signature

def rsa_signverify(message,signature):
    #读取公钥信息用于验签
    public_key = RSA.importKey(open("my_rsa_public.pem").read())
    #message做“哈希”处理，RSA签名这么要求的
    hash_obj = SHA1.new(message)
    try:
        #因为签名被base64编码，所以这里先解码，再验签
        pkcs1_15.new(public_key).verify(hash_obj,base64.b64decode(signature))
        print('The signature is valid.')
        return True
    except (ValueError,TypeError):
        print('The signature is invalid.')

if __name__ == '__main__':
    #create_rsa_key()
    #encrypt_and_decrypt_test()

    message = b'code=200&data={\"store_id\":\"100001\",\"vendor_code\":\"WHEATEK\",\"term_model\":\"S1\",\"mer_id\":\"663101000017582\",\"term_sn\":\"SD110470T00100001\",\"term_id\":\"TID30559\",\"term_type\":\"SMART_POS\",\"sign_key\":\"F8F5TZujOao6G+vvwXzfodTacQ47jNHi/q8wiwFqvRKgMrYJUlE6ONv74vFCNbelQhfJQQFi/mDcLdPDAWJpo1oRoVd7ClG5qC/JZfwXJttrT8JTYTRNkG+eItsP75nFyiPnent3GZdfNNencu3Z7n1LvjG8Eq7BIZe6oLyFj5M=\"}'
    #signature = rsa_sign(message)
    #print('signature:',signature)
    #print(rsa_signverify(message,signature))

    str = '&msg=网关请求成功，请判断业务返回码'
    str_a = str.encode('utf-8')
    message_t = b'Luosu is a Middle-aged uncle.f'
    signature_t = b'NWSGSML+prKI26m0fWFqpld3q2WWdh/+fLblugga76gYdRz5sbD6Tyd16TDfEEE29v/kPLmLjHhOIAba/F1fH6Ew52Qj6WiLIcj7QvNPiX2TBnqtUDgr+/0euFrPI8kge9SkBu/IouNOHyZ1D9p2PzKvNJQjWJV7mV2IfkLdBaY='
    print(rsa_signverify(message+str_a,signature_t))


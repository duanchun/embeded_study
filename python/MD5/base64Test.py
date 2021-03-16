
import base64


data_src = b'fBoPpG/vLzLYQR2+LN+dD+jktQuCobLRJiRt0lseeqXt2qJifcyr+BiVwaCK0vogW00+5Qup/GrLrgQxiDRF0cEZnT0Nje9OUYOYJTJH9EyLvb9n1eHgHUt03DYOCfSAzZXdR7AkAHztOcfczwfdXMCc+G3a9rPXU9iPjfHjVmA='

print(data_src)


data_decryto = base64.b64decode(data_src)
print(len(data_decryto))
print(data_decryto.hex())
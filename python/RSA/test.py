print ("Hellow world!")

str_a='b9:3c:6a:c4:bd:e7:f6:5a:b6:04:42:7b:2d:8d:\
b5:9f:2c:6f:54:94:47:e9:2d:34:e8:38:e5:98:80:\
f1:25:89:41:68:81:88:f1:a5:f4:a0:62:e7:30:d4:\
5e:63:9d:5c:e3:08:09:48:26:0d:9a:21:ea:ab:90:\
12:47:3e:12:f5'

str_b = str_a.replace(':','')
str_c = str_b.upper()
print (str_a)
print (str_b)
print ('\r\n')
print (str_c)

with open('data.txt','w') as f:
    f.write(str_c)
    f.close()



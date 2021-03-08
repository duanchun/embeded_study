import json

"""
:param data: 需要签名的数据，字典类型
:return: 处理后的字符串，格式为：参数名称=参数值，并用&连接
"""
def data_parse(data):
        
    dataList = []
    for key in sorted(data):
        if data[key]:
            dataList.append("%s=%s" % (key, data[key]))
    return "&".join(dataList).strip()

data_src = '{"vendor_code":"WHEATEK",\
"term_sn":"SD110470T00100001",\
"term_model":"S1",\
"term_type":"SMART_POS",\
"timestamp":"2020-05-05 11:11:11",\
"nonce":"123456",\
"mer_id":"663101000017582",\
"store_id":"100001",\
"term_id":"TID30559",\
"date":"20200501",\
"sign":"Efitv73Xzm0Y/rzZuksa2ZMT2gq8ycAVI6RMHtMDDEfQJJ9UgtjFLlAn2wKvabk3Y9BdwRQSqzyfTYeZnodWzIdRTJbUmeHr+CgUklNgsjirsjEHly9wqzs0qrdxfKQafK5tpFrAJAjbe6G5vtQ7x2m0gjlt3ymVVB7xykXPulE="}'
     

json_str = json.dumps(data_src)
#print ("JSON 对象：", json_str)

# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print(data2)
strmm=json_str['nonce']
print(strmm)
#data_parse(data2)
#print(data_parse(data2))  






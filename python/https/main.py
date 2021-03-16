import requests

url = "https://hmpay.sandpay.com.cn/gateway/term/api"

payload="{\"app_id\":\"202120445967396126737\",\"method\":\"trade.percreate\",\"sign_type\":\"MD5\",\"timestamp\":\"2021-03-14 14:11:52\",\"nonce\":\"2028664838\",\"biz_content\":\"{\\\"create_ip\\\":\\\"123456\\\",\\\"total_amount\\\":0.01,\\\"out_order_no\\\":\\\"1\\\",\\\"store_id\\\":\\\"100001\\\",\\\"body\\\":\\\"wheatek\\\",\\\"out_order_no\\\":\\\"1\\\"}\",\"sign\":\"3154C5FD5339F63A82CCBC7A3FF02F04\"}"
headers = {
  'Content-Type': 'application/json',
  'Cookie': 'JSESSIONID=C4B574C738199639535C52D2CF89B812'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


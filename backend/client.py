import requests

# 定义要发送的数据
data = {
    'id': 1,
    'name': 'John Doe',
    'salary': 50000,
    'dept_id': 'IT'
}

# 发送 POST 请求到后端 API
response = requests.post('http://127.0.0.1:5000/create_employee', json=data)

# 输出服务器响应
print(response.json())

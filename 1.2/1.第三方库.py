# 1. requests - 简单发起HTTP GET请求
import requests
import urllib3

# 禁用 SSL 警告（仅用于学习演示，生产环境应使用正确的证书）
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

response = requests.get("https://api.github.com", verify=False)
print(f"GitHub API响应状态码: {response.status_code}")

# 2. numpy & pandas - 数值和数据分析
import numpy as np
import pandas as pd

arr = np.array([1, 2, 3, 4, 5])
print(f"\nNumPy数组均值: {np.mean(arr)}")

data = {"姓名": ["张三", "李四"], "成绩": [90, 85]}
df = pd.DataFrame(data)
print("\npandas DataFrame:")
print(df)

# 3. matplotlib - 画图
import matplotlib.pyplot as plt
import matplotlib

# 设置中文字体支持
matplotlib.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "DejaVu Sans"]
matplotlib.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题

plt.plot([1, 2, 3], [4, 5, 6])
plt.title("简单折线图")
plt.show()

# 4. beautifulsoup4 - 解析网页
from bs4 import BeautifulSoup

html = "<html><body><h1>Hello, World!</h1></body></html>"
soup = BeautifulSoup(html, "html.parser")
print(f"\n网页标题内容: {soup.h1.text}")

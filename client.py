"""
1,导入模块
2，创建套接字 TCP
3，建立连接 connect（）
4，发送数据
5，关闭套接字
"""

# 1,导入模块
import socket
# 2，创建套接字 TCP
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3，建立连接 connect（）
tcp_client.connect(("192.168.88.1",8080))
# 4，发送数据
print("this is A")
temp = ""
for i in range(1, 100):
    temp = temp + "%d," % i
temp = temp + "100"
cotent = temp
print(cotent)
tcp_client.send(cotent.encode("GBK"))
# 接受数据
recv_data = tcp_client.recv(1024)
print("从B发来的数据")
recv_text = recv_data.decode("GBK")
recv_list = recv_text.split(',')
for i in recv_list:
    print(i, end=' ')

# 5，关闭套接字
tcp_client.close()
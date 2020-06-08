"""
1,导入模块
2，创建套接字
3，绑定端口和ip
4，要开启监听（设置套接字为被动模式）
5，等待客户端连接
6，收发数据
7，关闭连接
"""
# 1,导入模块
import socket
# 2，创建套接字
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3，绑定端口和ip
tcp_server.bind(("", 8080))
# 4，要开启监听（设置套接字为被动模式）
# 128 允许接收最大的连接数
tcp_server.listen(128)
# 5，等待客户端连接
print("this is B")
new_client_socket, client_ip_port = tcp_server.accept()
print("新客户端A来了", str(client_ip_port))
# 6，收发数据
recv_data = new_client_socket.recv(1024)
recv_text = recv_data.decode("GBK")
recv_list = recv_text.split(',')
for i in recv_list:
    print(i, end=' ')

temp = ""
for i in range(100, 1, -1):
     temp = temp+"%d,"%i
temp = temp + "1"
cotent = temp
print("\n"+cotent)
new_client_socket.send(cotent.encode("GBK"))
new_client_socket.close()
# 7，关闭连接
tcp_server.close()
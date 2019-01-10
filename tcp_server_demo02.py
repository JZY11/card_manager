import socket


def main():
    """循环为多个客户端服务"""

    # 1.买个手机(创建套接字 socket)
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 监听套接字：等待有新的客户端进行连接

    # 2.插入手机卡(绑定本地信息 bind)
    tcp_server_socket.bind("", 7890)

    # 3.将手机设置为正常的响铃模式(让默认的套接字由主动变为被动 listen)
    tcp_server_socket.listen(128)

    while True:
        # 4.等待别人的电话到来(等待客户端的连接 accept) accept返回的是一个元组
        new_client_socket, clientAddr = tcp_server_socket.accept()  # 左边第一个是accept产生的套接字用来为客户端服务，第二个是某客户端连接过来的信息，也是一个元组(客户端ip，客户端port)

        # 5.接受客户端发送过来的请求
        receive_data = new_client_socket.recv(1024)  # 接受1024个字节  返回不是元组，是一个普通数据

        # 6.恢复一部分数据给客户端
        tcp_server_socket.send("hahaha")

        # 7.关闭套接字
        new_client_socket.close()
    tcp_server_socket.close()

if __name__ == "__mian__":
    main()
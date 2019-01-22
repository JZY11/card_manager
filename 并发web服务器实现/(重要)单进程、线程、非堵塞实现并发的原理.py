import socket
import time


tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind(("", 1000))
tcp_server.listen(128)
tcp_server.setblocking(False)   # 设置套接字为非堵塞的方式

client_socket_list = list() # 定义一个列表

while True:
    time.sleep(2)

    try:
        new_socket, new_addr = tcp_server.accept()
        print("--- 来了一个新客户端 ---")
    except Exception as ret:
        print("---- 没有新的客户端到来 ----")
    else:
        print("--- 只要没有产生异常，那么就意味着来了一个新的客户端 ---")
        new_socket.setblocking(False)   # 设置套接字为非堵塞的方式
        client_socket_list.append(new_socket)

    for client_socket in client_socket_list:
        try:
            recv_data = client_socket.recv(1024)
        except Exception as ret:
            print("---- 这个客户端没有发送来数据 ----")
        else:
            if recv_data:
                print("--- 客户端发送过来了数据 ---")
            else:
                # 浏览器客户端调用了close导致 rev返回
                client_socket_list.remove(new_socket)
                client_socket.close()
                print("--- 客户端已经关闭 ---")
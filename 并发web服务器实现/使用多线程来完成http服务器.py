import socket
import re
# import multiprocessing
import threading


def service_client(new_socket):
    """为这个客户端返回数据"""

    # 1. 接受浏览器发送过来的请求即http发送过来的请求
    # GET / HTTP/1.1
    #......

    request = new_socket.recv(1024).decode("utf-8") # 服务器对接收到的客户端发送过来的请求进行解码
    # print(request)
    request_lines = request.splitlines()
    print(">" * 20)
    print(request_lines)

    ret = re.match(r"[^/]+/[^ ]*", request_lines[0])   # r是为了原生字符串不用转义
    if ret:
        file_name = ret.group(1)

    # 2.2 准备好发送给浏览器的数据 ---  body
    try:
        f = open("./html/index.html", "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "----- file not found --- "
        new_socket.send(response.encode("utf-8"))

    else:
        html_content = f.read()
        f.close()
        # 2. 返回http格式的数据给浏览器
        # 2.1 准备好发送给浏览器的数据 ---  header
        response = "HTTP/1.1 200 0K\r\n"
        response += "\r\n"
        new_socket.send(response.encode("utf-8"))  # 发送头部信息
        new_socket.send(html_content)  # 发送body信息


    # 关闭套接字
    new_socket.close()


def main():
    """用来完成整体的控制"""
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置当服务器先close，即服务器4词挥手之后资源能够立即释放，这样就保证了，下次运行程序时，可以立即执行
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)

    # 2. 绑定
    tcp_server_socket.bind(("", 7890))

    # 3. 变为监听套接字
    tcp_server_socket.listen(128)

    while True:
        # 4. 等待新客户端的链接
        new_socket, client_address = tcp_server_socket.accept()

        # 5. 为这个客户端服务
        t = threading.Thread(target=service_client, args=(new_socket, )) # 用Thread创建多线程
        t.start()
        # 套接字对象就指向fd：文件描述符  创建子线程的时候不会复制资源所以扔然只有一个指向该fd， 而创建子进程的话会复制资源，就会有有两个同时指向该fd

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()


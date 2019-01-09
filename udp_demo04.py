import socket

"""循环发送数据并且带有退出功能并且绑定本地信息"""
def main():
    """创建一个udp套接字"""
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 可以使用套接字收发数据 (发送任意数据，不单单局限于字节数据)

    # 绑定本地信息
    udp_socket.bind(("", 7890))
    while True:
        # 从键盘获取数据
        send_data = input("请输入要发送的数据：")

        # 如果输入的数据是exit的话，那就退出程序
        if send_data == "exit":
            break

        destaddr = ("192.168.0.4", 8080)  # 对方的ip和端口  要写在一个元组里
        #udp_socket.sendto(b"hahaha",destaddr)
        udp_socket.sendto(send_data.encode("utf-8"), destaddr) # encode 编码

        udp_socket.recvfrom(1024) # 接收数据，最大为1024个字节
    # 关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()
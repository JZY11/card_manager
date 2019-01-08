import socket

"""从键盘接收数据然后发送，注意从键盘接收的是字符串数据，但是发送的数据只可是字节数据，所以要用到encode编码"""
def main():
    """创建一个udp套接字"""
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 可以使用套接字收发数据 (发送任意数据，不单单局限于字节数据)
    # 从键盘获取数据
    send_data = input("请输入要发送的数据：")


    destaddr = ("192.168.0.4", 8080)  # 对方的ip和端口  要写在一个元组里
    #udp_socket.sendto(b"hahaha",destaddr)

    udp_socket.sendto(send_data.encode("utf-8"), destaddr) # encode 编码
    # 关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()
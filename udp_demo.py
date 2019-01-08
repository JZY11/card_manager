import socket

def main():
    """创建一个udp套接字"""
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 可以使用套接字收发数据
    destaddr = ('192.168.0.4', 8080)  # 对方的ip和端口  要写在一个元组里
    udp_socket.sendto('hahaha',destaddr)
    # 关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()
import urllib.request
import gevent
from gevent import monkey


monkey.patch_all()


def downloader(img_name, img_rul):
    req = urllib.request.urlopen(img_rul)
    image_content = req.read()
    with open(img_name, "wb") as f:
        f.write(image_content)


def main():
    gevent.joinall([
        gevent.spawn(downloader, "1.jpg", 'https://rpic.douyucdn.cn/live-cover/roomCover/2018/12/21/a77342abaa632c7760684a6a99f1f387_big.png'),
        gevent.spawn(downloader,  "2.jpg", 'https://rpic.douyucdn.cn/live-cover/appCovers/2019/01/03/3659788_20190103132115_small.jpg'),
    ])


if __name__ == "__main__":
    main()



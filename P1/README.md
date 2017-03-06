
依赖
===========
1. python2
2. selenium
3. chromedriver
4. Beautifulsoup & lxml


安装步骤
===========

安装python2
---------

对于 Windows 用户，Python 安装目录和其中的 Script 文件夹加入到环境变量中。例如 `C:\Python27` 是你Python的安装目录，那么把`C:\Python27`和`C:\Python27\Scripts`加入到你的环境变量中。

安装 selenium
--------

```
pip install selenium
```

安装 chromedriver
--------
[点此](https://chromedriver.storage.googleapis.com/index.html?path=2.27/) 选择下载对应操作系统的 chromedrive


安装 Beautifulsoup & lxml
--------
```
pip install bs4
pip install lxml
```


运行
===========

先把数据文件夹复制进来，执行
```
python main.py
```

运行会弹出一个chrome界面，需要现在网页登录输入用户名 `tli144@syr.edu` 密码 `Helloworld1`

程序自动在弹出的网页中模拟鼠标操作抓取数据。如需终止请按 `Ctrl-c`。

如果遇到网络中断或其他情况导致程序崩溃，请重新执行即可。

记得在根目录下创建一个文件夹名为data  为爬取数据结果存储位置


跑endata时需要安装node.js  安装地址：https://nodejs.org/en/download/

随后重启Python IDE（一定要记得重启！！！）

先运行config.py配置execjs引擎

再运行endata.py  不出意外会报错：IndexError: list index out of range

顺着报错路径找到"subprocess.py"的源文件  一般是报错信息的最后一行

在subprocess.py源文件中搜索encoding  大约再738行左右出现以下代码：

pass_fds=(), *, encoding=None, errors=None, text=None):

再将该段源码中的encoding变量改为'utf-8'，即：

pass_fds=(), *, encoding='utf-8', errors=None, text=None):

重新运行endata.py得到结果
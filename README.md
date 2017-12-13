# jumper
> jump to other server just like ssh

#### version : 0.1


### 1.说明
远程ssh服务器的时候经常会被一堆不同环境的用户名密码困扰, 该rep会提供一个python脚本, 读取env.json配置文件中username password等信息, 一键登录远程服务器.

### 2.使用
* step 0: 准备

需要python3的环境

```
➜ ~ python3 --version
Python 3.6.0
```
安装pexpect运行库

```
➜  ~ pip3 install pexpect
```
* step 1: 下载

```
➜  ~ git clone https://github.com/hrf1159/jumper.git
➜  ~ cd jumper
➜  jumper git:(master) ✗ ll
total 24
-rw-r--r--@ 1 hanruofei  staff   527B  4  1 14:51 README.md
-rw-r--r--  1 hanruofei  staff   265B  4  1 14:33 env.json
-rw-r--r--  1 hanruofei  staff   1.3K  4  1 14:32 jump.py
```
* step 2: 修改配置文件env.json

> 添加覆盖自己的远程服务器相关配置

```
[
    {
        "env": "dev",  #环境名称
        "ip": "127.0.0.1", #目标服务器ip
        "port": "36000", #目标服务器port,default值22
        "username": "root", #用户名
        "password": "passwd" #密码
    },
    {
        "env": "test",
        "ip": "127.0.0.1",
        "username": "root",
        "password": "passwd"
    }
]
```
* step 3: 使用

> dev 为在env.json中env对应的value, 即服务器别名, 登录的是对应的远程服务器

```
➜  jumper git:(master) ✗ python3 jump.py dev
 
Last login: Sat Apr  1 14:34:08 2017 from 10.101.51.15
[root@kafka39 ~]$ 
```
* step 4: 帮助

> --conf 或者 --env 展示当前所有已配置环境

```
➜  jumper git:(master) ✗ python3 jump.py dev
 
Last login: Sat Apr  1 14:34:08 2017 from 10.101.51.15
[root@kafka39 ~]$ 

➜  jumper git:(master) ✗ python3 jump.py --env
[
    {
        "env": "dev",
        "ip": "10.101.51.15",
        "password": "passwd",
        "username": "root"
    }
]
```


**强烈建议在自己常用的shell中定义别名**

```
alias jumper="python3 /Users/hanruofei/Documents/tools/jumper/jump.py "
```
然后就可以更优雅的使用

```
➜  ~ jumper dev

Last login: Sat Apr  1 15:20:54 2017 from 10.101.51.15
[root@kafka39 ~]$ 

➜  ~ jumper --env
[
    {
        "env": "dev",
        "ip": "10.101.51.15",
        "password": "passwd",
        "username": "root"
    }
]
```

### 3.版本
* version 0.1

> 基本的用户名 密码 登录功能

### 4.友链
> 如果你是忠实的shell用户,可以尝试下shell版本的jumper

> [猛戳这里](https://github.com/LuoDi-Nate/Jumper)

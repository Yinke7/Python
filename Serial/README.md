## 2021.01.28

运行环境：

* ` Linux`平台

命令格式：
* ` sudo python3 SerialSend.py -p /dev/ttyUSB0 -b 115200`

安装包：

`$ pip3 install pyserial`

* 该脚本用于在Linux上通过串口通信

* 可向串口发送数据，但需手动输入十六进制数

## 2021.02.01
* 修改串口收发流程，采用两个线程分别负责发送和传输
* 新增发送数据功能

## 2021.01.19
运行环境：

* ` Linux`主机（不能是虚拟机，我用的是树莓派）

* ` Python3.7.3`

该脚本用于向手机发送文件，是一个` test.txt`文件；文件中的内容为：

` bluettoth test`   

安装相关Python库：

` $ pip3 install PyBluez`

` $ pip3 install PyOBEX`

安装驱动：

` $ sudo apt-get install libbluetooth-dev`

执行脚本：

` $ python3 Bluettoth_Sendfile2phone.py "AOSP on BullHead"`

` "AOSP on BullHead"`是设备的蓝牙名称，执行脚本时需换成对应手机的蓝牙设备名称。

运行结果为：

<img src="https://github.com/Yinke7/Python/blob/main/Bluetooth/Image/execute%20script.jpg" style="zoom:25%;" />

此时，手机端会收到蓝牙传输文件：

<img src="https://github.com/Yinke7/Python/blob/main/Bluetooth/Image/recieve%20request.jpg" style="zoom:25%;" />

点击接受，打开文件可以看到` Hello Bluetooth`的内容：

<img src="https://github.com/Yinke7/Python/blob/main/Bluetooth/Image/context.jpg" style="zoom:25%;" />




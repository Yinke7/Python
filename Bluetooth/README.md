## 2021.01.18

该脚本用于向手机发送文件，是一个` test.txt`文件；文件中的内容为：

` bluettoth test`  

安装相关Python库：

` $ pip3 install PyBluez`

` $ pip3 install PyOBEX`

执行脚本：

` $ python3 Bluettoth_Sendfile2phone.py "AOSP on BullHead"`

` "AOSP on BullHead"`是设备的蓝牙名称，执行脚本时徐焕成对应手机的蓝牙设备名称。

运行结果为：

![](C:\Users\yk152\Pictures\Saved Pictures\蓝牙传输.jpg)

此时，手机端会收到蓝牙传输文件：

<img src="C:\Users\yk152\Pictures\Saved Pictures\蓝牙文件.jpg" style="zoom:25%;" />

点击接受，打开文件可以看到` Hello Bluetooth`的内容：

<img src="C:\Users\yk152\Pictures\Saved Pictures\接受文件.jpg" style="zoom:25%;" />




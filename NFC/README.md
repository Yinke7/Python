##2021.02.25 

运行环境:
* ` Raspberrypi4 B`

所需工具：
* ` PN532`模块` PN532 NFC HAT`（微雪）
* ` Mifareonetool`破解密码用，直接串口连接` PN532`模块，打开软件即可操作
* ` Proxmark3开发板`, ` Proxmark3 Easy GUI`破解密码用  https://github.com/Proxmark/proxmark3.git
* ` Mifare Classic EV1 1K` `nfc`卡

python包：
* ` RPi.GPIO`

功能描述：
* 使用` python`脚本可对` Mifare`卡进行读写操作，若卡为加密卡，可使用` Proxmark`先行破解，获取密码后再访问数据

Remark：
* ID卡数据存储格式 [https://blog.csdn.net/TonnyBrown/article/details/75200601](https://blog.csdn.net/TonnyBrown/article/details/75200601) 

* NFC Tag 各类型介绍 https://bbs.huaweicloud.com/blogs/169354 `2.2`小节

##2021.03.01

* 新增` x-nucleo-nfc06a1`，该文件夹是基于` st25r3916`的扩展板，可连接树莓派的` spi`接口，使用文件夹中的` demo`进行测试（详见` st`官网）
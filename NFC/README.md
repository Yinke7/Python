#2021.02.25
运行环境:
* ` Raspberrypi4 B`

所需工具：
* ` PN532`模块` PN532 NFC HAT`（微雪）
* ` Proxmark3开发板`, ` Proxmark3 Easy GUI`（破解密码用, https://github.com/Proxmark/proxmark3）
* ` Mifare Classic EV1 1K`nfc卡

python包：
* ` RPi.GPIO`

功能描述：
* 使用` python`脚本可对` Mifare`卡进行读写操作，若卡位加密卡，可使用` Proxmark`先行破解，获取密码后再访问数据



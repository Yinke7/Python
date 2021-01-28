#!/bin/bash
# -*- coding:utf-8 -*-

import serial
import sys

def Run(Serialport, senddata, timeout):

    # 设置串口端口号，波特率 115200bps，超时时间 0.1s
    ser = serial.Serial(port=Serialport, baudrate=115200, timeout=float(timeout))
    print("waitting for %f s" % float(timeout))

    # 发送数据
    ser.write(bytes.fromhex(senddata))

    # 接收数据并打印
    try:
        while True:
            readdata = ser.read(size=0xffffff)
            if readdata:
                print(readdata.decode('utf-8'))
    except KeyboardInterrupt:
        if None != ser:
            ser.close()
            print("serial closed")

    return

if __name__ == "__main__":
    if sys.argv[1].lower() == "help":
        print("usage: <help/port(/dev/tty*)> <baudrate(int)> <data(str)> <timeout(float)>")
        exit()

    Run(sys.argv[1], sys.argv[2], sys.argv[3])


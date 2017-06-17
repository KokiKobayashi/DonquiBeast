#!/usr/bin/env python

import subprocess
import time

def control(text):
    if (text == 'stop'):
        # モータ停止
        subprocess.call("./motor 0", shell = True)
    if (text == 'go forward' or text == 'forward' or text == 'front' ):
        # 前進
        subprocess.call("./motor 1", shell = True)
#        time.sleep(5)
#        subprocess.call("./motor 0", shell = True)
    if (text == 'go backward' or text == 'backward' or text == 'back'):
        # 後退
        subprocess.call("./motor 2", shell = True)
#        time.sleep(5)
#        subprocess.call("./motor 0", shell = True)
    if (text == 'turn left'):
        # 方向転換：左
        subprocess.call("./motor 3", shell = True)
#        time.sleep(1)
#        subprocess.call("./motor 0", shell = True)
    if (text == 'turn right'):
        # 方向転換：右
        subprocess.call("./motor 4", shell = True)
#        time.sleep(1)
#        subprocess.call("./motor 0", shell = True)

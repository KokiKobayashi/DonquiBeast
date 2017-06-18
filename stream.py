#!/usr/bin/env python

from picamera import PiCamera
import time
import io

camera = PiCamera()
#camera.resolution(640, 480)
time.sleep(5)
stream = io.BytesIO()

for foo in camera.capture_continuous(stream, "jpeg", use_video_port=True):
	stream.seek(0)
	frame = stream.getvalue()
	stream.seek(0)
	stream.truncate()

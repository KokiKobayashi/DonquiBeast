import io
import picamera

stream = io.BytesIO()
with	picamera.PiCamera() as camera:
	camera.resolution = (1920, 1080)
	camera.start_recording('video.mjpeg')
	camera.wait_recording(15)
	camera.stop_recording()

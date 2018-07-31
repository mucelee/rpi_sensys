from rplidar import RPLidar
import os

device = os.getenv('LIDAR_USB_DEVICE', '/dev/ttyUSB0')

lidar = RPLidar(device)

info = lidar.get_info()
print(info)

health = lidar.get_health()
print(health)

iterator = lidar.iter_scans()
for i, scan in enumerate(iterator):
	print('%d: Got %d measurements' % (i, len(scan)))
	print("Data organization: quality (?), angle (degrees), distance (mm)")
	scanData = scan
	print(scanData)
	if i == 2:
		break

lidar.stop()
lidar.stop_motor()
lidar.disconnect()

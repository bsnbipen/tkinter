from zaber_motion import units
from zaber_motion.ascii import Connection


with Connection.open_serial_port("COM3") as connection:
    device_list = connection.detect_devices()
    print("Found {} devices".format(len(device_list)))
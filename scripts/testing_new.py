from DeltaArray import DeltaArray
import numpy as np
import time

da = DeltaArray('/dev/tty.usbmodem142301')

da.reset()
da.wait_until_done_moving()
print(da.get_joint_positions())

p = np.ones((1,12)) * 0.02
duration = [1.0]
da.move_joint_position(p,duration)
da.wait_until_done_moving()
print(da.get_joint_positions())

da.close()
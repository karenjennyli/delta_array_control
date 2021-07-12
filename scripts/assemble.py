from DeltaArray import DeltaArray
import numpy as np
import time

da = DeltaArray('/dev/ttyACM0')

print(da.get_joint_positions())

d0 = 0.01
d1 = 0.03

p = np.ones((1, 12)) * d0
# duration = [0.5]
# da.move_joint_position(p,duration)
# da.wait_until_done_moving()
# print(da.get_joint_positions())


p[:,9:] = d1

duration = [0.5]
da.move_joint_position(p,duration)
da.wait_until_done_moving()
print(da.get_joint_positions())

# # da.reset()
# # da.wait_until_done_moving()
# # print(da.get_joint_positions())

p[:,10] = d1 + 0.005

duration = [1.0]
da.move_joint_position(p,duration)
da.wait_until_done_moving()
print(da.get_joint_positions())

p[:,11] = d1 + 0.005

duration = [1.0]
da.move_joint_position(p,duration)
da.wait_until_done_moving()
print(da.get_joint_positions())

da.close()
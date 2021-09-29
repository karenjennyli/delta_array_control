from DeltaArray import DeltaArray
import numpy as np
import time

da = DeltaArray('/dev/tty.usbmodem14201')

# p = [[0.010, 0.010, 0.010, # 1, 2, 3
#       0.010, 0.010, 0.010, # 4, 5, 6
#       0.010, 0.010, 0.010, # 7, 8, 9
#       0.010, 0.010, 0.010]] # 10, 11, 12

# p = [[0.010, 0.010, 0.010, # 1, 2, 3
#       0.000, 0.000, 0.000, # 4, 5, 6
#       0.010, 0.010, 0.010, # 7, 8, 9
#       0.000, 0.000, 0.000]] # 10, 11, 12

# p = [[0.030, 0.030, 0.030, # 1, 2, 3
#       0.000, 0.000, 0.000, # 4, 5, 6
#       0.030, 0.030, 0.030, # 7, 8, 9
#       0.000, 0.000, 0.000]] # 10, 11, 12

# hold yellow cube

# p = [[0.010, 0.014, 0.010, # 1, 2, 3
#       0.000, 0.000, 0.000, # 4, 5, 6
#       0.010, 0.014, 0.010, # 7, 8, 9
#       0.000, 0.000, 0.000]] # 10, 11, 12

positions = []

# positions.append([[0.000, 0.000, 0.000, # 1, 2, 3
#                    0.000, 0.000, 0.000, # 4, 5, 6
#                    0.000, 0.000, 0.000, # 7, 8, 9
#                    0.020, 0.020, 0.020]]) # 10, 11, 12

# positions.append([[0.010, 0.010, 0.010, # 1, 2, 3
#                    0.010, 0.010, 0.010, # 4, 5, 6
#                    0.010, 0.010, 0.010, # 7, 8, 9
#                    0.010, 0.010, 0.010]]) # 10, 11, 12

# positions.append([[0.010, 0.010, 0.010, # 1, 2, 3
#                    0.010, 0.010, 0.010, # 4, 5, 6
#                    0.010, 0.010, 0.010, # 7, 8, 9
#                    0.010, 0.010, 0.010]]) # 10, 11, 12

i = 1

p = [0.0] * 12

p[i-1] = 0.050

# p = [0.050] * 12

positions.append([p])

duration = [1.0]

da.reset()
da.wait_until_done_moving()
print(da.get_joint_positions())

# da.move_joint_position(np.array(p), duration)
# da.wait_until_done_moving()
# print(da.get_joint_positions())

for p in positions:
    print("------------------------------------------------")
    print(p)
    print("------------------------------------------------")
    da.move_joint_position(np.array(p), duration)
    da.wait_until_done_moving()
    print(da.get_joint_positions())

# da.reset()
# da.wait_until_done_moving()
# print(da.get_joint_positions())
da.close()

print("Finished.")
import json


with open('/home/jianqi/Documents/code/RoboVerse/metasim/cfg/tasks/debug/reach_v2.json','r') as f:
    data = json.load(f)
    content = data["franka"]
    print(content[0])
    if "franka" in content[0]: print("franka")
    if "init_state" in content[0]: print("init_state")
# {
#     "franka": [
#         {
#             "init_state": {
#                 "franka": {
#                     "dof_pos": {
#                         "panda_joint1": 0.0,
#                         "panda_joint2": 0.0,
#                         "panda_joint3": 0.0,
#                         "panda_joint4": 0.0,
#                         "panda_joint5": 0.0,
#                         "panda_joint6": 0.0,
#                         "panda_joint7": 0.0,
#                         "panda_finger_joint1": 0.0,
#                         "panda_finger_joint2": 0.0
#                     },
#                     "pos": [
#                         0.0,
#                         0.0,
#                         0.0
#                     ],
#                     "rot": [
#                         1.0,
#                         0.0,
#                         0.0,
#                         0.0
#                     ]
#                 }
#             }
#         }
#     ]
# }

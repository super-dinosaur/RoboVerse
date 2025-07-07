from metasim.utils.setup_util import SimType, get_robot, get_sim_env_class, get_task
import importlib
import os.path as osp
from icecream import ic
import sys

project_root = osp.dirname(osp.abspath(__file__))
sys.path.insert(0,project_root)

moduel = importlib.import_module('test_class')
myClass = getattr(moduel,'Grasp')
instance = myClass()
print(instance)



# task = get_task(
#     task_id='arnold.arnold_task_cfg:ArnoldTask'
# )
# print("ok;pass")

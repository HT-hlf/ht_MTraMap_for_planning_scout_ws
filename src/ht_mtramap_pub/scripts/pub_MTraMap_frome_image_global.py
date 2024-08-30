#!/usr/bin/env python
import sys
import os.path

import rospy
from grid_map_msgs.msg import GridMap
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import MultiArrayDimension

import cv2

import numpy as np

def publish_grid_map(pub,data,resolution=0.2):

    # 创建一个 Publisher，用于发布网格地图数据

    # 创建一个网格地图消息
    grid_map = GridMap()
    # print(grid_map)
    grid_map.basic_layers.append('elevation')
    grid_map.layers.append('elevation')

    grid_map.info.header.seq = 0
    grid_map.info.header.frame_id = "map"
    grid_map.info.header.stamp = rospy.Time.now()

    # 设置地图分辨率、宽度、高度和原点坐标
    grid_map.info.resolution = resolution
    grid_map.info.length_x = data.shape[0]*grid_map.info.resolution
    grid_map.info.length_y = data.shape[1]*grid_map.info.resolution
    grid_map.info.pose.position.x = 0
    grid_map.info.pose.position.y = 0
    grid_map.info.pose.position.z = 0
    grid_map.info.pose.orientation.x = 0
    grid_map.info.pose.orientation.y = 0
    grid_map.info.pose.orientation.z = 0
    grid_map.info.pose.orientation.w = 1


    mat = Float32MultiArray()
    mat.layout.dim.append(MultiArrayDimension())
    mat.layout.dim.append(MultiArrayDimension())
    mat.layout.dim[0].label = "column_index"
    mat.layout.dim[1].label = "row_index"
    mat.layout.dim[0].size = data.shape[0]
    mat.layout.dim[1].size = data.shape[1]
    mat.layout.dim[0].stride = data.shape[1]*data.shape[0]
    mat.layout.dim[1].stride = data.shape[1]
    mat.layout.data_offset = 0
    mat.data = data.flatten()

    grid_map.data.append(mat)




    # 发布网格地图消息
    # rate = rospy.Rate(1)  # 1 Hz
    pub.publish(grid_map)
    # rate.sleep()


def publish_grid_map_publishtra(pub,data,data_tra,resolution=0.2):

    # 创建一个 Publisher，用于发布网格地图数据

    # 创建一个网格地图消息
    grid_map = GridMap()
    # print(grid_map)
    grid_map.basic_layers.append('elevation')
    grid_map.layers.append('elevation')
    # grid_map.basic_layers.append('tra')
    grid_map.layers.append('tra')

    grid_map.info.header.seq = 0
    grid_map.info.header.frame_id = "map"
    grid_map.info.header.stamp = rospy.Time.now()

    # 设置地图分辨率、宽度、高度和原点坐标
    grid_map.info.resolution = resolution
    grid_map.info.length_x = data.shape[0]*grid_map.info.resolution
    grid_map.info.length_y = data.shape[1]*grid_map.info.resolution
    grid_map.info.pose.position.x = 0
    grid_map.info.pose.position.y = 0
    grid_map.info.pose.position.z = 0
    grid_map.info.pose.orientation.x = 0
    grid_map.info.pose.orientation.y = 0
    grid_map.info.pose.orientation.z = 0
    grid_map.info.pose.orientation.w = 1


    mat = Float32MultiArray()
    mat.layout.dim.append(MultiArrayDimension())
    mat.layout.dim.append(MultiArrayDimension())
    mat.layout.dim[0].label = "column_index"
    mat.layout.dim[1].label = "row_index"
    mat.layout.dim[0].size = data.shape[0]
    mat.layout.dim[1].size = data.shape[1]
    mat.layout.dim[0].stride = data.shape[1]*data.shape[0]
    mat.layout.dim[1].stride = data.shape[1]
    mat.layout.data_offset = 0
    mat.data = data.flatten()

    grid_map.data.append(mat)

    mat = Float32MultiArray()
    mat.layout.dim.append(MultiArrayDimension())
    mat.layout.dim.append(MultiArrayDimension())
    mat.layout.dim[0].label = "column_index"
    mat.layout.dim[1].label = "row_index"
    mat.layout.dim[0].size = data_tra.shape[0]
    mat.layout.dim[1].size = data_tra.shape[1]
    mat.layout.dim[0].stride = data_tra.shape[1] * data_tra.shape[0]
    mat.layout.dim[1].stride = data_tra.shape[1]
    mat.layout.data_offset = 0
    mat.data = data_tra.flatten()

    grid_map.data.append(mat)




    # 发布网格地图消息
    # rate = rospy.Rate(1)  # 1 Hz
    pub.publish(grid_map)
    # rate.sleep()

def publish_grid_map_publishtra_multi(pub,data,data_tra_multi,traversability_label, traversability_poss_mean,resolution=0.2):

    # 创建一个 Publisher，用于发布网格地图数据

    # 创建一个网格地图消息
    grid_map = GridMap()
    # print(grid_map)
    grid_map.basic_layers.append('elevation')
    grid_map.layers.append('elevation')
    # grid_map.basic_layers.append('tra')


    grid_map.info.header.seq = 0
    # grid_map.info.header.frame_id = "map"
    grid_map.info.header.frame_id = "odom"
    grid_map.info.header.stamp = rospy.Time.now()

    # 设置地图分辨率、宽度、高度和原点坐标
    grid_map.info.resolution = resolution
    grid_map.info.length_x = data.shape[0]*grid_map.info.resolution
    grid_map.info.length_y = data.shape[1]*grid_map.info.resolution
    grid_map.info.pose.position.x = 0
    grid_map.info.pose.position.y = 0
    grid_map.info.pose.position.z = 0
    grid_map.info.pose.orientation.x = 0
    grid_map.info.pose.orientation.y = 0
    grid_map.info.pose.orientation.z = 0
    grid_map.info.pose.orientation.w = 1


    mat = Float32MultiArray()
    mat.layout.dim.append(MultiArrayDimension())
    mat.layout.dim.append(MultiArrayDimension())
    mat.layout.dim[0].label = "column_index"
    mat.layout.dim[1].label = "row_index"
    mat.layout.dim[0].size = data.shape[0]
    mat.layout.dim[1].size = data.shape[1]
    mat.layout.dim[0].stride = data.shape[1]*data.shape[0]
    mat.layout.dim[1].stride = data.shape[1]
    mat.layout.data_offset = 0
    mat.data = data.flatten()

    grid_map.data.append(mat)

    for i in range(8):
        grid_map.layers.append('tra_{}'.format(str(i)))
        mat = Float32MultiArray()
        mat.layout.dim.append(MultiArrayDimension())
        mat.layout.dim.append(MultiArrayDimension())
        mat.layout.dim[0].label = "column_index"
        mat.layout.dim[1].label = "row_index"
        mat.layout.dim[0].size = data_tra_multi[:,:,2*i+1].shape[0]
        mat.layout.dim[1].size = data_tra_multi[:,:,2*i+1].shape[1]
        mat.layout.dim[0].stride = data_tra_multi[:,:,2*i+1].shape[1] * data_tra_multi[:,:,2*i+1].shape[0]
        mat.layout.dim[1].stride = data_tra_multi[:,:,2*i+1].shape[1]
        mat.layout.data_offset = 0
        mat.data = data_tra_multi[:,:,2*i+1].flatten()

        grid_map.data.append(mat)

    grid_map.layers.append('tra_{}'.format('intersection'))
    mat = Float32MultiArray()
    mat.layout.dim.append(MultiArrayDimension())
    mat.layout.dim.append(MultiArrayDimension())
    mat.layout.dim[0].label = "column_index"
    mat.layout.dim[1].label = "row_index"
    mat.layout.dim[0].size = traversability_label.shape[0]
    mat.layout.dim[1].size = traversability_label.shape[1]
    mat.layout.dim[0].stride = traversability_label.shape[1] * traversability_label.shape[0]
    mat.layout.dim[1].stride = traversability_label.shape[1]
    mat.layout.data_offset = 0
    mat.data = traversability_label.flatten()

    grid_map.data.append(mat)

    grid_map.layers.append('tra_{}'.format('mean'))
    mat = Float32MultiArray()
    mat.layout.dim.append(MultiArrayDimension())
    mat.layout.dim.append(MultiArrayDimension())
    mat.layout.dim[0].label = "column_index"
    mat.layout.dim[1].label = "row_index"
    mat.layout.dim[0].size = traversability_poss_mean.shape[0]
    mat.layout.dim[1].size = traversability_poss_mean.shape[1]
    mat.layout.dim[0].stride = traversability_poss_mean.shape[1] * traversability_poss_mean.shape[0]
    mat.layout.dim[1].stride = traversability_poss_mean.shape[1]
    mat.layout.data_offset = 0
    mat.data = traversability_poss_mean.flatten()

    grid_map.data.append(mat)




    # 发布网格地图消息
    # rate = rospy.Rate(1)  # 1 Hz
    pub.publish(grid_map)
    # rate.sleep()


def tra_padding(input_image, padding_size):


    # 使用np.pad()函数在输出图像周围添加padding
    padded_image = np.pad(input_image, ((padding_size, padding_size), (padding_size, padding_size)), mode='constant', constant_values=0)

    return padded_image

def tra_padding_multi(input_image, padding_size):
    input_image = input_image.astype(np.float32)


    # 使用np.pad()函数在输出图像周围添加padding
    padded_image = np.pad(input_image, ((padding_size, padding_size), (padding_size, padding_size),(0,0)), mode='constant', constant_values=0.5)

    return padded_image
def tra_padding_multi_poss(input_image, padding_size):
    input_image = input_image.astype(np.float32)


    # 使用np.pad()函数在输出图像周围添加padding
    padded_image = np.pad(input_image, ((padding_size, padding_size), (padding_size, padding_size),(0,0)), mode='constant', constant_values=0.5)

    return padded_image

if len(sys.argv) >= 4:
    world_name = sys.argv[1].split('.')[0]
    conf_threshold = float(sys.argv[2])
    print(world_name)
else:
    rospy.logerr(usage())
    sys.exit(1)

rospy.init_node('ht_MTraMap_global_publisher', anonymous=True)
pub = rospy.Publisher('MTraMap_global', GridMap, queue_size=10)
rate = rospy.Rate(1)  # 1 Hz
model_path = '/home/ht/ht_code/PLAN_WS/ht_MTraMap_for_planning_scout_ws/src/ht_terrain_MTraMap/model/'

# world_name = 'elemap_internet_mass_uzh_elevation_height_1_distancex_42_distancey_42'
# # 这个只可以设置为 0.5，0.6,0.7,0.8,0.9
# conf_threshold = 0.5

# max_hm_z = float(world_name.split('_')[-5])
max_hm_z = float(world_name.split('_')[-5])/100
#是否发布0-1的通过性图
pub_tra_poss = True
#是否发布0和1的通过性图
pub_tra_label = True
#是否发布八个方向通过性的平均值
pub_tra_poss_mean= True
#是否发布八个方向通过性的平均值
pub_tra_poss_mean= True
#是否发布八个方向通过性的与/交集
pub_tra_label_all= True
#是否发布八个方向通过性的或/并集
pub_tra_label_any= True
height_tra_dir  = os.path.join(model_path,world_name,'materials/textures')
height_image_path =  os.path.join(height_tra_dir,world_name+'.png')

pub_tra_list_sum = []
pub_tra_dict_sum = dict()
if pub_tra_poss_mean:
    pub_tra_list_sum  +=['tra_poss_mean_conf{}.jpg'.format(int(conf_threshold * 100))]
if pub_tra_label_all:
    pub_tra_list_sum  +=['tra_label_all_conf{}.jpg'.format(int(conf_threshold*100))]
if pub_tra_label_any:
    pub_tra_list_sum  +=['tra_label_any_conf{}.jpg'.format(int(conf_threshold * 100))]
if pub_tra_label:
    pub_tra_list_sum  += ['tra_label_{}_conf{}.jpg'.format(i,int(conf_threshold* 100)) for i in range(8)]

if pub_tra_poss:
    pub_tra_list_sum  += ['tra_poss_{}_conf{}.jpg'.format(i,int(conf_threshold* 100)) for i in range(8)]


tra_image_shape = None

for tra_image_name in pub_tra_list_sum:
    tra_image_path = os.path.join(height_tra_dir, tra_image_name )
    tra_image = cv2.imread(tra_image_path)
    tra_image = cv2.flip(tra_image , 1)
    tra_image = tra_image[:, :, 0]
    tra_image = tra_image / 255
    pub_tra_dict_sum[tra_image_name.split('.')[0]]= tra_image
    tra_image_shape = tra_image.shape

height_image = cv2.imread(height_image_path)
height_image = cv2.flip(height_image , 1)
height_image = cv2.resize(height_image,tra_image_shape)
height_image = height_image[:,:,0]
height_data = height_image / 255
height_data = max_hm_z * height_data

pub_tra_dict_sum_items = pub_tra_dict_sum.items()
while not rospy.is_shutdown():
    grid_map = GridMap()
    # print(grid_map)
    grid_map.basic_layers.append('elevation')
    grid_map.layers.append('elevation')
    # grid_map.basic_layers.append('tra')

    grid_map.info.header.seq = 0
    grid_map.info.header.frame_id = "map"
    # grid_map.info.header.frame_id = "odom"
    grid_map.info.header.stamp = rospy.Time.now()

    # 设置地图分辨率、宽度、高度和原点坐标
    grid_map.info.resolution = 0.04
    grid_map.info.length_x = height_data.shape[0] * grid_map.info.resolution
    grid_map.info.length_y = height_data.shape[1] * grid_map.info.resolution
    grid_map.info.pose.position.x = 0
    grid_map.info.pose.position.y = 0
    grid_map.info.pose.position.z = 0
    grid_map.info.pose.orientation.x = 0
    grid_map.info.pose.orientation.y = 0
    grid_map.info.pose.orientation.z = 0
    grid_map.info.pose.orientation.w = 1

    mat = Float32MultiArray()
    mat.layout.dim.append(MultiArrayDimension())
    mat.layout.dim.append(MultiArrayDimension())
    mat.layout.dim[0].label = "column_index"
    mat.layout.dim[1].label = "row_index"
    mat.layout.dim[0].size = height_data.shape[0]
    mat.layout.dim[1].size = height_data.shape[1]
    mat.layout.dim[0].stride = height_data.shape[1] * height_data.shape[0]
    mat.layout.dim[1].stride = height_data.shape[1]
    mat.layout.data_offset = 0
    mat.data = height_data.flatten()

    grid_map.data.append(mat)

    for key,value in pub_tra_dict_sum_items :
        grid_map.layers.append(key)
        mat = Float32MultiArray()
        mat.layout.dim.append(MultiArrayDimension())
        mat.layout.dim.append(MultiArrayDimension())
        mat.layout.dim[0].label = "column_index"
        mat.layout.dim[1].label = "row_index"
        mat.layout.dim[0].size = value.shape[0]
        mat.layout.dim[1].size = value.shape[1]
        mat.layout.dim[0].stride = value.shape[1] * value.shape[0]
        mat.layout.dim[1].stride = value.shape[1]
        mat.layout.data_offset = 0
        mat.data = value.flatten()

        grid_map.data.append(mat)

    pub.publish(grid_map)
    rate.sleep()
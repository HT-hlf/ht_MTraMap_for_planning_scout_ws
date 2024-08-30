> 包含多向通过性图的仿真环境代码库，关于多向通过性图的定义参考 多向通过性图的定义.pdf



- [x] 2024/08/30 更新1544个地形，通过性图使用scout通过性网络（之前是 hunter_se 模型），代码有相应调整，需要重新clone下来

  - 地形在百度网盘链接：

    链接: https://pan.baidu.com/s/16RUlYkA7CzoiMWP2OlzNtw?pwd=p1d4 提取码: p1d4 
    --来自百度网盘超级会员v7的分享

  - 地形名称解释

    version2_C4D_20_map3-height_height_高度范围 cm_distancex_ 长度范围 cm_distancey_ 宽度范围 cm

    version2_C4D_20_map3-height_height_200_distancex_2050_distancey_2050：表示地图高度是0-200cm  长度是2050cm 宽度是2050cm 。在使用时如果高度100cm不合适可以选择50cm 150cm 200cm 试试

  - 下载完使用需要 设置地形仿真模型路径 (路径换成自己的) （下面有说明）
  - 有通过性计算错误或者其它代码问题，给我截图反馈

# 仿真地形配置

- 设置地形仿真模型路径

  ```
  export GAZEBO_MODEL_PATH={model文件夹路径}
  ```

  例如：

  ```
  export GAZEBO_MODEL_PATH=/home/ht/ht_code/PLAN_WS/ht_MTraMap_for_planning_scout_ws/src/ht_terrain_MTraMap/model
  ```

- 启动仿真地形

  ```
  gazebo  xxxx.world
  ```


# MTraMap图发布

> MTraMap图的生成算法目前正在测试，有通过性计算错误或者问题，给我反馈

- 发布的gridmap 可选图层 (代码里可以根据需要选择性发布图层)
  - 高程图
    - elevation
  - 0和1的八个方向通过性图：
    - tra_label_0, tra_label_1, ...... tra_label_7,  
  - 0～1的八个方向通过性图
    - tra_poss_0, tra_poss_1, ...... tra_poss_7,  
  - 八个方向通过性的平均值
    - tra_poss_mean
  - 八个方向通过性的与/交集
    - tra_label_all
  - 八个方向通过性的或/并集
    - tra_label_any

# 使用

- 设置地形仿真模型路径 (路径换成自己的)

  - 命令行输入：

    ```
    export GAZEBO_MODEL_PATH={model文件夹路径}
    ```

  - roslaunch scout_gazebo_sim scout_v2_gps_pub_MTraMap.launch 文件中修改world_name中的仿真环境路径对应自己文件夹

    ```
    <include file="$(find gazebo_ros)/launch/empty_world.launch">
            <arg name="world_name" value="/home/ht/ht_code/PLAN_WS/ht_MTraMap_for_planning_scout_ws/src/ht_terrain_MTraMap/world/$(arg world_name)"/>
    
    ```

  - pub_MTraMap_frome_image_global.py 和 pub_MTraMap_frome_image_global.py 文件中修改model_path仿真环境路径对应自己文件夹

- 启动机器人和仿真地形 定位程序 全局和局部高程图/多向通过性图 

  ```
  source devel/setup.bash
  roslaunch scout_gazebo_sim scout_v2_gps_pub_MTraMap.launch 
  ```

  （如果很卡，可以在里面注释掉全局地图发布 pub_MTraMap_global.launch）


- 效果：

  ![](README.assets/2023-11-04%2016-16-08%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)

  ![](README.assets/2023-11-04%2016-15-53%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)

  [![video](https://bb-embed.herokuapp.com/embed?v=BV1wy4y1c7yv)](https://www.bilibili.com/video/BV1wy4y1c7yv/?vd_source=c81e9e4a6abdaa49045ee8304823fb81)

  
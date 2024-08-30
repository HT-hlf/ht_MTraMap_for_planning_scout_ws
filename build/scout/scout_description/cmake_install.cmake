# Install script for directory: /home/ht/ht_code/PLAN_WS/ht_MTraMap_for_planning_scout_ws/src/scout/scout_description

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/ht/ht_code/PLAN_WS/ht_MTraMap_for_planning_scout_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/ht/ht_code/PLAN_WS/ht_MTraMap_for_planning_scout_ws/build/scout/scout_description/catkin_generated/installspace/scout_description.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/scout_description/cmake" TYPE FILE FILES
    "/home/ht/ht_code/PLAN_WS/ht_MTraMap_for_planning_scout_ws/build/scout/scout_description/catkin_generated/installspace/scout_descriptionConfig.cmake"
    "/home/ht/ht_code/PLAN_WS/ht_MTraMap_for_planning_scout_ws/build/scout/scout_description/catkin_generated/installspace/scout_descriptionConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/scout_description" TYPE FILE FILES "/home/ht/ht_code/PLAN_WS/ht_MTraMap_for_planning_scout_ws/src/scout/scout_description/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/scout_description" TYPE DIRECTORY FILES
    "/home/ht/ht_code/PLAN_WS/ht_MTraMap_for_planning_scout_ws/src/scout/scout_description/launch"
    "/home/ht/ht_code/PLAN_WS/ht_MTraMap_for_planning_scout_ws/src/scout/scout_description/meshes"
    "/home/ht/ht_code/PLAN_WS/ht_MTraMap_for_planning_scout_ws/src/scout/scout_description/urdf"
    )
endif()


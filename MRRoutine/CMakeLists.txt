CMAKE_MINIMUM_REQUIRED(VERSION 3.15)
project(MRROUTINE)
FILE(GLOB SRC_LIST ${PROJECT_SOURCE_DIR}/src/*.cpp)
add_executable(mrroutine ${SRC_LIST}) #生成可执行文件(.exe) 

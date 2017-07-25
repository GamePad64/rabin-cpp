cmake_policy(SET CMP0048 NEW)

project(rabin-cpp VERSION 1.0)
if(EXISTS "${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake")
	include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
	conan_basic_setup(TARGETS)
endif()

add_library(rabin-cpp STATIC Rabin.cpp Rabin.h)
target_include_directories(rabin-cpp PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

set_property(TARGET rabin-cpp PROPERTY CXX_STANDARD 11)
set_property(TARGET rabin-cpp PROPERTY CXX_STANDARD_REQUIRED TRUE)

find_library(Boost 1.58 REQUIRED)
target_link_libraries(rabin-cpp PRIVATE Boost::boost)

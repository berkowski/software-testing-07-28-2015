PROJECT(WhoiMath)
CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

LIST(APPEND CMAKE_CXX_FLAGS "-std=c++0x")


SET(WhoiMath_HEADERS 
  whoiMath.h)

SET(WhoiMath_SOURCES
  whoiMath.cpp)

ADD_LIBRARY(WhoiMath SHARED
  ${WhoiMath_SOURCES})

ENABLE_TESTING()
ADD_SUBDIRECTORY(tests)

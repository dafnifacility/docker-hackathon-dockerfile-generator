cmake_minimum_required(VERSION 3.18 FATAL_ERROR)

project(SourceCode VERSION 1.0.0)

include(ExternalProject)


ExternalProject_Add(
    ExternalProject
    SOURCE_DIR ${CMAKE_CURRENT_BINARY_DIR}/data/source
    BINARY_DIR ${CMAKE_CURRENT_BINARY_DIR}/ExternalProject
    GIT_REPOSITORY ${GIT_URL}
    GIT_TAG ${GIT_TAG}
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND ""
)
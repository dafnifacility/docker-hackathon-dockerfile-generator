#! /bin/sh

# Install CMake
curl -o cmake.tgz -L https://github.com/Kitware/CMake/releases/download/v3.25.1/cmake-3.25.1-linux-x86_64.tar.gz
tar xzf cmake.tgz && rm cmake.tgz
ln -s cmake-*x86_64 cmake || true
export PATH="$PWD/cmake/bin:$PATH"
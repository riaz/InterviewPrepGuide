# Creating a Simple Extension using NanoBind
=============================

### Installation

    python -m pip install nanobind

    Create a CMakeLists.txt file as the example

    # Next we run the following commands
    # make sure my_ext.cpp is created or equivalent

    cmake -S . -B build

    cmake --build build

## Usage

    cd build

    python # get into a python interpreter

    import my_ext

    my_ext.add(1,2)
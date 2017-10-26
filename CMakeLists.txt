# set (libname "HX711")
# set (libdescription "24 Bit Analog-to-digital Convertor")
# set (module_src ${libname}.cxx)
# set (module_hpp ${libname}.hpp)
# upm_module_init(mraa)
enable_language(CXX)

add_executable (h7 src/try.cpp)

target_link_libraries (h7 mraa stdc++)

# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.3

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/root/server/SC2.0

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/root/server/SC2.0/build

# Include any dependencies generated for this target.
include CMakeFiles/h7.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/h7.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/h7.dir/flags.make

CMakeFiles/h7.dir/src/try.o: CMakeFiles/h7.dir/flags.make
CMakeFiles/h7.dir/src/try.o: ../src/try.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/root/server/SC2.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/h7.dir/src/try.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/h7.dir/src/try.o -c /home/root/server/SC2.0/src/try.cpp

CMakeFiles/h7.dir/src/try.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/h7.dir/src/try.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/root/server/SC2.0/src/try.cpp > CMakeFiles/h7.dir/src/try.i

CMakeFiles/h7.dir/src/try.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/h7.dir/src/try.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/root/server/SC2.0/src/try.cpp -o CMakeFiles/h7.dir/src/try.s

CMakeFiles/h7.dir/src/try.o.requires:

.PHONY : CMakeFiles/h7.dir/src/try.o.requires

CMakeFiles/h7.dir/src/try.o.provides: CMakeFiles/h7.dir/src/try.o.requires
	$(MAKE) -f CMakeFiles/h7.dir/build.make CMakeFiles/h7.dir/src/try.o.provides.build
.PHONY : CMakeFiles/h7.dir/src/try.o.provides

CMakeFiles/h7.dir/src/try.o.provides.build: CMakeFiles/h7.dir/src/try.o


# Object files for target h7
h7_OBJECTS = \
"CMakeFiles/h7.dir/src/try.o"

# External object files for target h7
h7_EXTERNAL_OBJECTS =

h7: CMakeFiles/h7.dir/src/try.o
h7: CMakeFiles/h7.dir/build.make
h7: CMakeFiles/h7.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/root/server/SC2.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable h7"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/h7.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/h7.dir/build: h7

.PHONY : CMakeFiles/h7.dir/build

CMakeFiles/h7.dir/requires: CMakeFiles/h7.dir/src/try.o.requires

.PHONY : CMakeFiles/h7.dir/requires

CMakeFiles/h7.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/h7.dir/cmake_clean.cmake
.PHONY : CMakeFiles/h7.dir/clean

CMakeFiles/h7.dir/depend:
	cd /home/root/server/SC2.0/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/root/server/SC2.0 /home/root/server/SC2.0 /home/root/server/SC2.0/build /home/root/server/SC2.0/build /home/root/server/SC2.0/build/CMakeFiles/h7.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/h7.dir/depend


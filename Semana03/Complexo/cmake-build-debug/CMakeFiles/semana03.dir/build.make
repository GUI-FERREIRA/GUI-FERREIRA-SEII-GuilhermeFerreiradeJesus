# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.17

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "C:\Program Files\JetBrains\CLion 2020.3.2\bin\cmake\win\bin\cmake.exe"

# The command to remove a file.
RM = "C:\Program Files\JetBrains\CLion 2020.3.2\bin\cmake\win\bin\cmake.exe" -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = C:\Users\gf154\OneDrive\Documentos\semana03

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = C:\Users\gf154\OneDrive\Documentos\semana03\cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/semana03.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/semana03.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/semana03.dir/flags.make

CMakeFiles/semana03.dir/main.cpp.obj: CMakeFiles/semana03.dir/flags.make
CMakeFiles/semana03.dir/main.cpp.obj: CMakeFiles/semana03.dir/includes_CXX.rsp
CMakeFiles/semana03.dir/main.cpp.obj: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=C:\Users\gf154\OneDrive\Documentos\semana03\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/semana03.dir/main.cpp.obj"
	C:\MinGW\bin\g++.exe  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles\semana03.dir\main.cpp.obj -c C:\Users\gf154\OneDrive\Documentos\semana03\main.cpp

CMakeFiles/semana03.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/semana03.dir/main.cpp.i"
	C:\MinGW\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E C:\Users\gf154\OneDrive\Documentos\semana03\main.cpp > CMakeFiles\semana03.dir\main.cpp.i

CMakeFiles/semana03.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/semana03.dir/main.cpp.s"
	C:\MinGW\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S C:\Users\gf154\OneDrive\Documentos\semana03\main.cpp -o CMakeFiles\semana03.dir\main.cpp.s

CMakeFiles/semana03.dir/complexo.cpp.obj: CMakeFiles/semana03.dir/flags.make
CMakeFiles/semana03.dir/complexo.cpp.obj: CMakeFiles/semana03.dir/includes_CXX.rsp
CMakeFiles/semana03.dir/complexo.cpp.obj: ../complexo.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=C:\Users\gf154\OneDrive\Documentos\semana03\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/semana03.dir/complexo.cpp.obj"
	C:\MinGW\bin\g++.exe  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles\semana03.dir\complexo.cpp.obj -c C:\Users\gf154\OneDrive\Documentos\semana03\complexo.cpp

CMakeFiles/semana03.dir/complexo.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/semana03.dir/complexo.cpp.i"
	C:\MinGW\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E C:\Users\gf154\OneDrive\Documentos\semana03\complexo.cpp > CMakeFiles\semana03.dir\complexo.cpp.i

CMakeFiles/semana03.dir/complexo.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/semana03.dir/complexo.cpp.s"
	C:\MinGW\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S C:\Users\gf154\OneDrive\Documentos\semana03\complexo.cpp -o CMakeFiles\semana03.dir\complexo.cpp.s

# Object files for target semana03
semana03_OBJECTS = \
"CMakeFiles/semana03.dir/main.cpp.obj" \
"CMakeFiles/semana03.dir/complexo.cpp.obj"

# External object files for target semana03
semana03_EXTERNAL_OBJECTS =

semana03.exe: CMakeFiles/semana03.dir/main.cpp.obj
semana03.exe: CMakeFiles/semana03.dir/complexo.cpp.obj
semana03.exe: CMakeFiles/semana03.dir/build.make
semana03.exe: CMakeFiles/semana03.dir/linklibs.rsp
semana03.exe: CMakeFiles/semana03.dir/objects1.rsp
semana03.exe: CMakeFiles/semana03.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=C:\Users\gf154\OneDrive\Documentos\semana03\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable semana03.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\semana03.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/semana03.dir/build: semana03.exe

.PHONY : CMakeFiles/semana03.dir/build

CMakeFiles/semana03.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\semana03.dir\cmake_clean.cmake
.PHONY : CMakeFiles/semana03.dir/clean

CMakeFiles/semana03.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" C:\Users\gf154\OneDrive\Documentos\semana03 C:\Users\gf154\OneDrive\Documentos\semana03 C:\Users\gf154\OneDrive\Documentos\semana03\cmake-build-debug C:\Users\gf154\OneDrive\Documentos\semana03\cmake-build-debug C:\Users\gf154\OneDrive\Documentos\semana03\cmake-build-debug\CMakeFiles\semana03.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/semana03.dir/depend


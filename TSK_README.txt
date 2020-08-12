Last Updated 8.12.2020

This file describes how to build 32-bit and 64-bit Visual Studio 2015 libvhdi library for use with TSK. This process should be followed when new release of libvhdi comes out.

----------------------------------------------------------------
Download source code tag.gz file from https://github.com/libyal/libvhdi/releases, make sure it has all libraries like libcstring etc. Do not download just git repository or "sorce code" link, they don't include all libraries and require executing multiple scripts, some of which don't run on Windows.

If you are upgrading from a previous version of libvhdi, delete all contents of libvhdi_64bit git folder (i.e. the previous version of libvhdi) on local drive except this file, the .git subfolder, .gitignore, and.gitattributes (if using git).

Extract the archve containg source code into libvhdi_64bit folder. It usually extracts in something like libvhdi-20140608 sub-folder. Move contents of that folder into top level git libvhdi_64bit folder

Open project in VS2015 and let it convert the solution.

Do a git add on any new base folders. It's easiest to do a git commit now, making sure to pick up any additional new files.

Remove pyvhdi, and vhdimount projects from the Visual Studio solution

At this point you should be able to build the 32-bit libvhdi solution.

Next we need to create the 64-bit targets.
* Go to Configuration manager -> Active solution platform
* Select "<New>"
* Type or select the new platform: "x64"
* Copy settings from: "Win32"
* Create new project platforms: enabled
* Right click on one of the projects and select "Properties" then "Librarian". Verify that "Target Machine" includes "X64" for the x64 platform.

At this point you should be able to build the 64-bit libvhdi solution. 

Previously it was necessary to change the output folder, but it appears to default to the correct spot now. Right click on one of the projects and go to Properties. Select "All configurations" and "x64" at the top, then the "General" tab. Verify that "Output Directory" is set to "$(SolutionDir)$(Platform)\$(Configuration)\". Also confirm that when you build the x64 target the output goes into "libvhdi_64bit\msvscpp\x64\Release". If this is not the case, follow the instructions on changing it in the bottom section of this document.

In order to be used with TSK the user needs to define an environment LIBVHDI_HOME variable pointed at the top level folder where this repository will be checked out to.

For example, if this repository is checked out into C:\cygwin64\home\user_name\libvhdi_64bit then LIBVHDI_HOME = C:\cygwin64\home\user_name\libvhdi_64bit



----------------------------------------------------------------
10.19.2016 version of the instructions

Download source code tag.gz file from https://github.com/libyal/libvhdi/releases, make sure it has all libraries like libcstring etc. Do not download just git repository or "sorce code" link, they don't include all libraries and require executing multiple scripts, some of which don't run on Windows.

If you are upgrading from a previous version of libvhdi, delete all contents of libvhdi_64bit git folder (i.e. the previous version of libvhdi) on local drive except .git subfolder, .gitignore, and.gitattributes (if using git).

Extract the archve containg source code into libvhdi_64bit folder. It usually extracts in something like libvhdi-20140608 sub-folder. Move contents of that folder into top level git libvhdi_64bit folder

Open project in VS2015 and let it convert the solution

Remove dokan, pyvhdi, and vhdimount projects from the Visual Studio solution

At this point you should be able to build the 32-bit libvhdi solution

Run both 64-bit conversion scripts as described in 
https://github.com/libyal/libvhdi/wiki/Building

At this point you should be able to build the 64-bit libvhdi solution

Now need to modify where libraries are being stored after build. By default all output is stored in /Release folder so when you build a 32-bit library and then build a 64-bit library, the 32-bit binaries get overwritten. We need to modify where the 64-bit binaries get stored.

Select the "x64" configuration in VS. Then for each project in libvhdi solution:
- right click on the project, select properties
- in "configuration:" pull-down menu select "All configurations"
- Select "Configuration Properties" -> "General"
- Change "Output directory" from "$(SolutionDir)$(Configuration)\" to "$(SolutionDir)$(Platform)\$(Configuration)"
Repeat these steps for all VS projects in the libvhdi solution

In order to be used with TSK the user needs to define an environment LIBVHDI_HOME variable pointed at the top level folder where this repository will be checked out to.

For example, if this repository is checked out into C:\cygwin64\home\user_name\libvhdi_64bit then LIBVHDI_HOME = C:\cygwin64\home\user_name\libvhdi_64bit
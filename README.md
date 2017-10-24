# Document on ACR experiments

The ACR experiments envolve various separated projects:

* The UnrealCV virtual environments for `proof-of-concept` implement (python2.7, I failed to use python3, needs revisit)
* The corresponding implements using our platform and ZED camera
* The `executable` files slightly changed from OpenMVG official examples
* The `SfM based` implements on OpenMVG
* Some other files calling OpenCV functions

And some `Restful-API` for (somewhat) cleaner interaction with sensors and hardwares:

* The `Restful ZED`, a flask app, grab and provide images from ZED camera
* The `Restful SixDof`, API from C# with the help of [sukona/Grapevine](https://github.com/sukona/Grapevine) for motion moving with hardware


## ACR

[ACR (Active Camera Relocalization)](https://github.com/MiaoDX/ACR) is the most insteresting part and our truly contribution. 

The HOWTOs are pretty clear in README of that project.

## (Various) BUILD

NOTE, please change install path of all libraries (openMVG here) into `C:\tools\cmake_install_libs`, since all my C++ code with cmake on windows will refer to this path for libraries. And chances are that some libraries can not deal with both Release and Debug at the same directory, so we may need two install paths, one for Debug and one for Release. For example, the OpenMVG can have two install paths: `C:\tools\cmake_install_libs\openMVG\debug` and `C:\tools\cmake_install_libs\openMVG\release`.

And if all you want is runing the example, the release mode is enough.

### Relative Pose Estimation (OpenMVG)

First of all, install openMVG, the develop version

``` vi
git clone https://github.com/openMVG/openMVG.git
mv openMVG openMVG_develop
cd openMVG_develop

git submodule init
git submodule update

git checkout develop # note, we are using develop branch, at least for now

# cmake and build

... # install path please set to `C:\tools\cmake_install_libs\openMVG_DEVELOP\debug`

```


The pose estimation thanks to openMVG

``` vi
git clone https://github.com/MiaoDX/openMVG_Pose_Estimation.git
cd openMVG_Pose_Estimation

# cmake and build

...

# SfM based `openMVG_Pose_Estimation/SfM_Aided`

...
```

### Depth Camera (ZED only at present)

We are using ZED (**Version 2.1.2**) with python 3, instrucions on how to please refer [stereolabs/zed-python](https://github.com/stereolabs/zed-python). As usual, plese use `conda` virtual environments for this.

The ZED SDK will overwrite some path variables like `OpenCV_DIR` which can be a problem. ~~So after install the SDK (and reboot as required), delete all the added variables (the new OpenCV_DIR, ), and combine them into one `bat` file, as [depth_camera/zed.bat](https://github.com/MiaoDX/depth_camera/blob/master/zed.bat).

All that said, each and eveytime we want to use ZED camera, we should `activate` the bat file first (just run it in command line window), and launch the applications from that command window, even the `pycharm` case.~~

``` vi
# python libraries

# conda way
numpy
cython
flask # Restful API

conda install -c menpo opencv3 # to avoid building opencv3 from scratch, contrib modules (like SIFT) not included

# pip way
unrealcv v0.3.9
json_tricks

# build way
zed python binding, reboot will be necessary for using
```

``` vi
git clone https://github.com/MiaoDX/depth_camera.git
```















TODO:

* The `Restful Kinect` (maybe can embrace other porjects)

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






In this project, we provide:

* one virtual environemnt build upon [unrealcv](https://github.com/unrealcv/unrealcv)
* one use ZED camera for RGB+Depth images and our platform for motion moving

The virtual one is a good example aiming at `proof-of-concept` and get you familiar with the concept and way of doing ACR, it is good for quantitative evaluation since the Camera pose can retreive from the Unreal Engine and are higly reliable. And moving camra in the virtaul environment is trival and precious. However, the precision is one double-edged sword, one the one hand, we can calculate the relative pose more preciously (especially when using Depth information) and move more accurately. On the other hand, the results and findings can not just apply into real world. Since in reality:

* Depth images (measures) from sensors are less constant and precious
* Motion moving with hardware are proven to have precision limitation







``` vi
```




## (Various) BUILD

NOTE, please change install path of all libraries (only openMVG here) into `C:\tools\cmake_install_libs`, since all my code on windows will have this path for libraries.

### Relative Pose Estimation (OpenMVG)


First of all, install openMVG, the develop version

``` vi
git clone https://github.com/openMVG/openMVG.git
mv openMVG openMVG_develop
cd openMVG_develop
git checkout develop # note, we are using develop branch, at least for now

# cmake and build

... # install path

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

We are using ZED with python 3, instrucions on how to please refer to [stereolabs/zed-python](https://github.com/stereolabs/zed-python). As usual, plese use `conda` virtual environments for this. And the ZED SDK will overwrite some path variables like `OpenCV_DIR` which can be a problem. So after install the SDK (and reboot as required), delete all the added variables (the new OpenCV_DIR, ), and combine them into one `bat` file, as [depth_camera/zed.bat](https://github.com/MiaoDX/depth_camera/blob/master/zed.bat).

All that said, each and eveytime we want to use ZED camera, we should `activate` the bat file first (just run it in command line window), and launch the applications from that command window, even the `pycharm` case.

``` vi
# python libraries

# conda way
numpy

conda install -c menpo opencv3 # to avoid building opencv3 from scratch

# pip way


# build way
zed python binding
```

``` vi
git clone https://github.com/MiaoDX/depth_camera.git
```















TODO:

* The `Restful Kinect` (maybe can embrace other porjects)

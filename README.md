# opencv-testing

Testing opencv on Python

All based on [Python Programming Tutorials](https://pythonprogramming.net/loading-images-python-opencv-tutorial/)

## Requirements

```shell
pip3 install numpy
pip3 install matplotlib
```

Using your favorite package manager install `openCV` in my case

```shell
sudo zypper in python3-opencv opencv
```

Also make sure you have the necessary python - qt libraries

```shell
sudo zypper in python3-qt4
```

## To run

Just execute

`python3 <name-of-file>.py`

Example:

`python3 12-feature_matching.py`

## Movement detection

To get the current movement value I used this method:

- Getting the MOG background substractor frame.
- Creating a mask of that frame.
- Did an `AND` operation between the masks, this results in a matrix.
  - In this matrix all white pixel are of value 255 and black pixels are 0.
- The sum of all those values is my `current_movement`.

The [Example](14-mog_back_ground_reduction_movement_detection.py) for movement detection assumes this:

- The webcam you are using has a resolution of 640*480.
- Using this I assumed a Treshhold of 2.5 to set a movement flag.
- This needs to be repeated for at least 10 Frames to activate the movement flag.

If you want to use the example video, you need to change to this value:

- `Treshhold = 0.2`

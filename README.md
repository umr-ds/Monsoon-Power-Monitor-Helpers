# Monsoon HV Power Monitor Helpers

This repo contains two simple python scripts for utilizing the Monsoon High Voltage Power Monitor.
Furthermore, this README provides some additional info for setting up everything.

## Installing dependencies
For using the the power monitor, you have to fulfill some requirements. You can use it with the python scripts or a GUI.

### Python
First, you will need the PyMonsoon module. This can be either installed via pip or directly from the Github repo. I prefer the repo because is the pip module is outdated and rarely updated.
Furthermore, you can install the package system wide or not. I prefer using the package locally, because you have to make changes here and there, since this is still alpha.

```
git clone https://github.com/msoon/PyMonsoon.git monsoon
cd monsoon
git checkout 0f14c064e4b378ba75fa94fe7bf6d4f8b078abdb
touch __init__.py
cd Monsoon
touch __init__.py
```

After that you have to change the import paths for two files:

First:
```diff
diff --git a/monsoon/Monsoon/HVPM.py b/monsoon/Monsoon/HVPM.py
index 1b6b217..b907123 100644
--- a/monsoon/Monsoon/HVPM.py
+++ b/monsoon/Monsoon/HVPM.py
@@ -4,11 +4,11 @@ import math
 import usb.core
 import usb.util
 import struct
-from Monsoon import Operations as op
+from monsoon.Monsoon import Operations as op

 import numpy as np

-from Monsoon import pmapi
+from monsoon.Monsoon import pmapi

 class Monsoon(object):
```

Second:
```
diff --git a/monsoon/Monsoon/pmapi.py b/monsoon/Monsoon/pmapi.py
index 394e851..4a28d9d 100644
--- a/monsoon/Monsoon/pmapi.py
+++ b/monsoon/Monsoon/pmapi.py
@@ -1,5 +1,5 @@
 import struct
-from Monsoon import Operations as op
+from monsoon.Monsoon import Operations as op
 import ctypes
 import platform
 import usb.core
```

Additionally, you need the `gflags` module

```
git clone git@github.com:google/python-gflags.git
cd python-gflags
python ./setup.py install --user
```

Now you are ready to use the python scripts from this repo.


## Setting up the Power Monitor
For using the Power Monitor, connect the power cable to the power input on the back of the device. Additionally, plug the USB A - USB B cable into the back of the power monitor and connect it with your computer.
At this point, turn on the power monitor device and enable the Vout of the power monitor with the `hvpm.py` script.

## Usage
**Note:** The scripts require root priviliges!
### `hvmp.py`
The `hvpm.py` script just enables and disables the output voltage.

```
sudo python hvpm.py -v <voltage>
```

The only parameter here is `-v`. The voltage can be `0 < v < 13`. If `-v` is 0, the output will be disabled.

### `measure.py`
The measure script starts the measurement.

```
sudo python measure.py -o <csv/path> -t <seconds> -n <#samples> -s
```

- `-o`: The path to the output CSV file. Default is disabled.
- `-t`: Time the measurement will be executed in seconds (has to be `int`). Default is infinite.
- `-n`: Number of samples (has to be `int`). Default is infinite.
- `-s`: Weather the measurements should be printed to `stdout`. Default is `False`

If both the `-t` and `-n` options are given the first condition will stop the measurement.

All  arguments are optional. If no option is given, the measurement will be executed infinitly and you won't see any output.


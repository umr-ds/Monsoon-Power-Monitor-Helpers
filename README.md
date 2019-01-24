# HVMP

This repo contains two simple scripts to measure energy either using the main channel or the USB channel.

**Note:** The scripts require root priviliges!

## Installation

First, you will need the PyMonsoon module.

```
pip install Monsoon
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

Now, either connect a device to the main channel (red and black wires) or use the USB A port on the front. If you want USB passthrough, you also have to connect a second USB A - USB B cable from the front of the power monitor to your computer.

## Main Channel

This folder is used to measure energy using the main channel (red and black wires).

### `voltage.py`
The `voltage.py` script just enables and disables the output voltage.

```
sudo python voltage.py -v <voltage>
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

## USB Channel

Here, there is only the `measure.py` script, which starts the measurement. The voltage is always 5V over USB.

```
sudo python measure.py -o <csv/path> -t <seconds> -n <#samples> -s -u
```

- `-o`: The path to the output CSV file. Default is disabled.
- `-t`: Time the measurement will be executed in seconds (has to be `int`). Default is infinite.
- `-n`: Number of samples (has to be `int`). Default is infinite.
- `-s`: Weather the measurements should be printed to `stdout`. Default is `False`
- `-u`: Weather the USB passthrough is enabled or not. Default is `True`

If both the `-t` and `-n` options are given the first condition will stop the measurement.

All  arguments are optional. If no option is given, the measurement will be executed infinitly and you won't see any output and USB passthrough is enabled.

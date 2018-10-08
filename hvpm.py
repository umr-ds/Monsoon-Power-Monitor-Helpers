import sys
import monsoon.Monsoon.HVPM as HVPM
import gflags as flags

FLAGS = flags.FLAGS

def main():
    if FLAGS.v is not None:
        # Setup the Power Monitor.
        power_monitor_device = HVPM.Monsoon()
        power_monitor_device.setup_usb()

        # Set the out voltage to the given number.
        # Set 0 for disabling the output voltage
        power_monitor_device.setVout(FLAGS.v)

if __name__ == "__main__":
    flags.DEFINE_float("v", None, "Set output voltage (0 for off)")

    FLAGS(sys.argv)
    main()

import sys
import signal

import Monsoon.HVPM as HVPM
import Monsoon.sampleEngine as sampleEngine

import gflags as flags


FLAGS = flags.FLAGS
engine = None

def stopMeasurement():
    engine.setStopTrigger(sampleEngine.triggers.GREATER_THAN, 0.1)

def main():
    global engine

    # Setup the Power Monitor.
    power_monitor_device = HVPM.Monsoon()
    power_monitor_device.setup_usb()
    power_monitor_device.setDefaultScaleValues()
    # Create a sampling engine
    engine = sampleEngine.SampleEngine(power_monitor_device)

    # Set output to stdout depending on the CLI option -s. Default is False
    engine.ConsoleOutput(FLAGS.s)
    # Set the filename for the output CSV file. Default is sample.csv in pwd.
    if FLAGS.o:
        engine.enableCSVOutput(FLAGS.o)

    # We can define two different termination conditions.
    # First: time, second: number of samples.
    # Therefore, we have to define the timestamp as the channel for the time condition.
    # Than, start the measurement immediately and set the stop trigger to 30,
    # which will terminate the measurement after 30 seconds per default.
    # Finally, do not terminate the measurement after a number of samples.
    engine.setTriggerChannel(sampleEngine.channels.timeStamp)
    engine.setStartTrigger(sampleEngine.triggers.GREATER_THAN, 0)
    engine.setStopTrigger(sampleEngine.triggers.GREATER_THAN, sampleEngine.triggers.SAMPLECOUNT_INFINITE)
    num_samples = sampleEngine.triggers.SAMPLECOUNT_INFINITE

    # If the -t parameter is set, set the stop trigger to the given seconds.
    if FLAGS.t:
        engine.setStopTrigger(sampleEngine.triggers.GREATER_THAN, FLAGS.t)
    # If the -n parameter is set, set the maximum sample number to the given numnber.
    if FLAGS.n:
        num_samples = FLAGS.n

    # Finally, start the measuremen.
    engine.startSampling(num_samples)

if __name__ == "__main__":
    flags.DEFINE_string("o", None, "Output path for measurements (default samples.csv)")
    flags.DEFINE_integer("t", None, "Timout in seconds for stopping sampling (default 30 seconds)")
    flags.DEFINE_integer("n", None, "Number of samples (default INFINITE)")
    flags.DEFINE_boolean("s", False, "Print to stdout (default False)")

    FLAGS(sys.argv)
    main()

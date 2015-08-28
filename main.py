#!/usr/bin/env python3

# Often bandwidth is given in megabits (Mb) per second whereas file size is given in megabytes (MB).

import argparse

def convert_seconds(sec):
    hourstring, minutestring, secondstring = "hour", "minute", "second" 
    hour1, minute1, second1 = "hour", "minute", "second"
    hour, minute, second = int( sec / 3600 ), int( (sec / 60) % 60 ), sec % 60
    
    if hour != 1:
        hourstring = hourstring + 's' 
    if minute != 1:
        minutestring = minutestring +'s'        
    if second != 1:
        secondstring = secondstring + 's'
    
    return ("{0} {1}, {2} {3}, {4} {5}").format (hour, hourstring, minute, minutestring, second, secondstring)

def convert_bits(size, units):
    kilobits = float(size)
    
    if units == 'kb':
        return kilobits
    elif units == 'kB':
        return kilobits * 8
    elif units == 'MB':
        return kilobits * (2 ** 10) * 8
    elif units == 'Mb':
        return kilobits * (2 ** 10)
    elif units == 'GB':
        return kilobits * (2 ** 20) * 8
    elif units == 'Gb':
        return kilobits * (2 ** 20)
    elif units == 'TB':
        return kilobits * (2 ** 30) * 8
    elif units == 'Tb':
        return kilobits * (2 ** 30)
    else:
        return 0.0

def download_time(file_size, file_units, bandwidth, bandwidth_units):
    file_size = convert_bits(file_size, file_units)
    bandwidth = convert_bits(bandwidth, bandwidth_units)
    
    time_taken = file_size / bandwidth
    return convert_seconds(time_taken)

def main():
    parser = argparse.ArgumentParser(description = "Estimator-Download-time")
    parser.add_argument("fsize", help = "File Size", type = int)
    parser.add_argument("funit", nargs = "?", default = "MB", help = "File Units")
    parser.add_argument("bwidth", help = "Bandwith", type = int)
    parser.add_argument("bunit", nargs = "?", default = "Mb", help = "Bandwith Units")

    args = parser.parse_args()

    print ("{}".format(download_time(args.fsize, args.funit, args.bwidth, args.bunit)))

if __name__ == '__main__':
    #print (download_time(1,'GB', 2, 'Mb'))
    #>>> 1 hour, 8 minutes, 16.0 seconds
    main()

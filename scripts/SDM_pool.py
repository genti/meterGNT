#!/usr/bin/env python
import settings
import os


def main(file):
    i=1
    for i in sdm_device:
        sdm_cmd="sdm120c -a %s -b %s -z 10 -i -p -v -c -f -g -P N -q %s" % (sdm_device,sdm_baudRate,sdm_usbSerial)
        output=os.system(sdm_cmd)
        e.write(output)
    file.close()

if __name__ == '__main__':
    while True:
        file = open(sdm_poolerLogFullPath, "w")
        main(file)
        time.sleep(sdm_poolRate)
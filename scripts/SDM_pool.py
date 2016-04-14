#!/usr/bin/env python
import settings
import subprocess,time


def main(file):
    i=1
    while i <= settings.sdm_device:
        sdm_cmd="sdm120c -a %s -b %s -z 10 -i -p -v -c -f -g -P N -q -w2 %s" % (settings.sdm_device,settings.sdm_baudRate,settings.sdm_usbSerial)
        proc = subprocess.Popen(sdm_cmd, stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        # print sdm_cmd;
        file.write(out)
        
        i=i+1
    file.close()

if __name__ == '__main__':
    while True:
        file = open(settings.sdm_poolerLogFullPath, "w")
        main(file)
        time.sleep(settings.sdm_poolRate) 
#!/usr/bin/env python
from __future__ import division
from subprocess import PIPE, Popen
import psutil,sys,time
import settings

def get_cpu_temperature():
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
    output, _error = process.communicate()
    return float(output[output.index('=') + 1:output.rindex("'")])


def main(file):
    cpu_temperature = get_cpu_temperature()
    cpu_usage = psutil.cpu_percent()

    ram = psutil.phymem_usage()
    ram_total = ram.total / 2**20       # MiB.
    ram_used = ram.used / 2**20
    ram_free = ram.free / 2**20
    ram_percent_used = ram.percent

    disk = psutil.disk_usage('/')
    disk_total = disk.total / 2**30     # GiB.
    disk_used = disk.used / 2**30
    disk_free = disk.free / 2**30
    disk_percent_used = disk.percent

    file.write('cpu_t(%s*C)\n' % cpu_temperature)

    file.write('cpu_u(%s*%%)\n' % cpu_usage)
    file.write('ram_u_p(%s*%%)\n' % ram_percent_used)

    file.close()



if __name__ == '__main__':
    while True:
        file = open("/run/shm/raspInfo.txt", "w")
        main(file)
        time.sleep(10)
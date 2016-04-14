#!/usr/bin/env python
import settings
import subprocess,time


def main(file):
    i=1
    while i <= settings.sdm_device: #per ogni sdm dichiarato in settigns
        sdm_cmd="sdm120c -a %s -b %s -z 10 -i -p -v -c -f -g -P N -q -w2 %s" % (settings.sdm_device,settings.sdm_baudRate,settings.sdm_usbSerial)
        proc = subprocess.Popen(sdm_cmd, stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate() #leggo i valori 
        out=out.split( ) #splitto per spazio
        
        new_out=''
        
        
        #brigo l'output per creare la sintassi che mi serve
        for index,val in enumerate(out): 
            if val != "OK": #rinuovo la stringa OK al fondo
                if ("%sx" % val) != "x":
                    new_out='%s%s(%s%s)\n' % (new_out,settings.sdm_device,val,settings.sdm_label[index])
        file.write(new_out)
        
        i=i+1
    file.close()

if __name__ == '__main__':
    while True:
        file = open(settings.sdm_poolerLogFullPath, "w") #apro in scrittura il file, s enon c'è lo creo
        main(file)
        time.sleep(settings.sdm_poolRate) #delay per la lettura successiva
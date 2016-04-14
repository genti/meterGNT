# meterGNT
# settings.py
# modificare i parametri secondo le proprie esigenze 

ramDiskPath='/run/shm/' #path di salvataggio dei log del pooler, usare il ramdisk per evitare corruzione sdcard


#IMPOSTAZIONI SDM120
sdm_logs_extension='.log' #seghe

sdm_poolRate=5 #secondi di intervallo tra le letture
sdm_parserRate=5 * 60 #secondi di intervallo per l'aggiornamento dello storico

sdm_label = ["*V","*A","*W","*F","*Hz","*Wh"]

sdm_device=1 #numero di device SDM120 da leggere
sdm_baudRate=2400 # baud rate SDM120

sdm_usbSerial='/dev/ttyUSB0' #path seriale
sdm_poolerLogFullPath='%s/sdmPool%s' % (ramDiskPath,sdm_logs_extension)
#!/usr/bin/env python
import settings
import subprocess,time

#splitta e ripulisce la stringa
def splitRow(row):
    split=row.replace(")","").split('(')
    sdm_id=int(split[0])
    val=split[1].split('*')[0]
    return sdm_id,val  
    
    

#monta il nuovo output 
def main(pooler_text,parsed_file):
    new_row=''
    sdm_id=0
    value_list=[]
    for row in pooler_text:
        id,val=splitRow(row)
        sdm_id=id
        value_list.append(val)
        new_row = '%s(%s)\n' % (sdm_id,','.join(value_list))
    parsed_file.write(new_row)
    parsed_file.close()
        
        
        
        
    

if __name__ == '__main__':
    while True:
        today = time.strftime("%Y%m%d") #data del file per i log odierni
        pooler_file = open(settings.sdm_poolerLogFullPath, "r") #apro in lettura il file creato da SDM_pooler.py
        parsed_file = open("%s/%s%s" % (settings.ramDiskPath,today,settings.sdm_logs_extension), "a") #apro il file dei log odierni 
        
        pooler_text= pooler_file.readlines()
        main(pooler_text,parsed_file) #parso le righe del file 
        time.sleep(settings.sdm_parserRate)  #delay
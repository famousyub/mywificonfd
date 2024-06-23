

from AppFIleSap import * 


import  sys 
import os 






if __name__  =='__main__':
    
    #filename = open("C:\Users\g702306\Desktop\ApplicSapMe\log5g\R2326303398-27092023153407_5G_PASS.txt","r")
    with open(f"C:\\Users\\g702306\\Desktop\\ApplicSapMe\\log5g\\R2326303398-27092023153407_5G_PASS.txt",'r+') as f:
            realine = f.readline()
            while realine :
                process_line(realine, "", "__", "__hj")
                if realine.find( "RUN_DUT_COMMAND" ) != -1:  
                    realine = f.readline()
                
                    print(realine)
                    Status_Failed=find_pattern (realine, "--- [Failed]", 0, 0)
                    if Status_Failed == 0:
                        print(Status_Failed)
                else :
                    pass
                
                
                
                
                
    
    
    
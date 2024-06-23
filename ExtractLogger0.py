

from  finalApplic import * 



def one()  :
    pass 
def two() :
    pass






if __name__ =='__main__':
    app1 =Application()
    app1.startextract()
    appl=AppliNom()
    appl.extract_time("R2326905450-27092023161006_2G_PASS.txt")
    res = app1.affiche_dict()
    x = datetime.datetime.now()
    date_time = x.strftime("%m_%d_%Y_%H_%M_%S")
    app1.write_to_text(f"result2G6fg.txt")
    
    with open("result2G6fg.txt","r") as g:
        with open("resultfinale1.txt" , "w+") as f:
            
            line  = g.readline()
            
            while line  :
                if  line.startswith('min') or 'min' in line:
                    break 
                elif line.startswith('Nom') or 'Nom' in line:
                    line = g.readline()
                    pass 
                else :
                    f.write(line)
                    line = g.readline()
                
    import os 
    os.remove("result2G6fg.txt")
                
                
                
        
        
        
    
    
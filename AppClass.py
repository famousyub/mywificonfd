

import os
import  sys 


import  time 


__version__ = '0.0.1'

def sorted_directory_listing_by_creation_time_with_os_listdir(directory):
    def get_creation_time(item):
        item_path = os.path.join(directory, item)
        return os.path.getctime(item_path)

    items = os.listdir(directory)
    sorted_items = sorted(items, key=get_creation_time)
    return sorted_items













    

















class  AppClass  : 
    
    
    def __init__(self,dir_ , file , data, pattern):
        
        
        self.dir_name =   sys.argv
        
        self.file =file 
        self.data  = data 
        self.pattern  = pattern
        self.listfiles = []
        self.sorted_list = []
    def  listDirs(self):
        
        if  len(self.dir_name) <= 1:
            self.list_files  = [file  for file  in  os.listdir(os.getcwd())]

        else :
            self.list_files  = [file  for file  in  os.listdir(self.dir_name)]
        
        return self.list_files 
    
    def sortedlist(self):
        
        _strtime = lambda file_path : time.strftime('%m/%d/%Y :: %H:%M:%S',
                                time.gmtime(os.path.getmtime(file_path)))
        self.sorted_list = [_strtime(file) for file in self.list_files]
        return self.sorted_list
    
    def  firstFiles(self):
        
        sorted_file = sorted(self.sorted_list, key=os.path.getmtime)[::-1]
        return sorted_file
    




        
        
        
        
        
        
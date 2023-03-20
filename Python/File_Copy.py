# copyfile()    =       copies contents of a file
# copy()        =       copyfile() + permission mode + destination can be a directory
# copy2()       =       copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile('Hola','/home/smile34/Documentos/copy')   # source and destination
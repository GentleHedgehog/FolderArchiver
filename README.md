# FolderArchiver
Creates an archive of any folder on Windows

This python script was created to automate the routine operation of archiving a gitblit data folder. 
The script is run by Windows scheduler every day (by Run_backup_folder.bat). 
The preparation of the scheduler is described in the file 'how to set scheduler.txt'.

The script was tested on Windows 7 x64, Python 3.6 x64

------------
TODO: 

It is need to reduce unnecessary operations in the script, such as: 
- creation of a duplicate folder (create a zip file from a source folder)
- deletion of a duplicate folder
- deletion of a temp zip file (move this zip file instead of copying)

FIXME: 
- check the access right problems

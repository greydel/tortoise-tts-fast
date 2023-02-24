import os
import pydub
import sys

from os import path
from pydub import AudioSegment

# show error if no command line argument is provided
if len(sys.argv) == 1:
    print("Please provide the path to the directory containing the files to convert.")
    sys.exit(1) 
    
# get the first command line argument (the path to the directory containing the files to convert)
directory = sys.argv[1]

# iterate over all files in current directory
def convert_to_wav():
    for file in os.listdir(directory):        
        if file.endswith(".mp3"):
            fullpath=os.path.join(directory, file)  
            exportpath=os.path.join(directory, file[:-4] + ".wav")
            # print fullpath and exportpath to console using string interpolation
            print(f"Converting {fullpath} to wav at {exportpath}...")            
            # convert mp3 to wav
            sound = AudioSegment.from_mp3(fullpath)
            sound.export(exportpath, format="wav")
            
convert_to_wav()            

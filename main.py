import argparse
import subprocess
import os 
import datetime
from time import sleep as wait 







#Function to get the current date time u at right now 
def get_env_time(now=datetime.datetime.now()):
    year = now.year
    hour = now.hour

    return year,hour


#Function to read the previous notes 
def read_file_save(filepath:str) -> str:
    path  = os.path.join(filepath)
    with open(filepath,"r+") as file_read:
        reading  = file_read.read()
        return reading

# Main function to create a note
def __create_note__(filepath:str,tag:str,note:str):
    path = os.path.join(filepath)
    file_saves = read_file_save(filepath)
    with open(path,"w") as writing_file:
        writing_file.write(file_saves + "\n")
        writing_file.write(note + ", @" + tag + " written at: " + str(get_env_time()))
        writing_file.close()
        print("Note has been added")


def __delete_note__(filepath:str,tag:str):
    #TODO
    # Check the tag from file with splitting by index 
    with open(filepath,"r") as file_reading:
        d = file_reading.read()
        for line in d :
            print(line)


def current_filepath():
    import json
    with open("current_path.json") as path:
        data = json.load(path)
        value = data["File_path"]
        return str(value)

def __update__file_path__():
    path = current_filepath()



d = current_filepath()
print(d)



#__create_note__("/Users/?/Desktop/LeafEditor/note.txt","test","This is a test also but yeah")


#__delete_note__("/Users/?/Desktop/LeafEditor/note.txt")



#parser = argparse.ArgumentParser()
#parser.add_argument('filename')
#args = parser.parse_args()
#if args.filename:
 #   print(args.firename)ls 

#if args.filename:
  #  path = os.path.join(args.filename)
    #print("hello")


l = "10"



def something(string="Hello",l=3):
    print(string)




# For later use 
__dic = {



    "Word":"Something"
}




for item,value  in __dic.items():
    print(item,value)
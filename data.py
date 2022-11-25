from pathlib import Path
from scipy.io import wavfile
from random import choice
import glob
import json


class entry:
    def __init__(self):
        self.name = ''
        self.type = ''
        self.filename = ''
        self.soundData = ''
        self.imgData = ''

    def __str__(self):
        return f'Object: {self.getName()}, Type: {self.getType()}'

    def __repr__(self):
        return f'Object: {self.getName()}, Type: {self.getType()} located at {self.getFilename()}'
        
    def setName(self, name):
        self.name = name

    def setType(self, typ):
        self.type = typ

    def setFilename(self, filename):
        self.filename = filename

    def setSoundData(self, sound_location):
        self.soundData = sound_location

    def setImageData(self, image_location):
        self.imgData = image_location

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getFilename(self):
        return self.filename

    def getSoundFilename(self):
        return self.soundData

    def getImageFilename(self):
        return self.imgData

    #def getSound(self):


    
class example:
    def __init__(self, random = False, n = 0, type='', debug=False):
        self.project_path  = Path(__file__).parent
        self.entries = []
        self.debug = debug
        #self.library
        self.discoverLib()

    def discoverLib(self):
        path_to_look = self.project_path/'Data'/'Database'
        #Look in the Database folder and find all json entries
        entries_path = glob.glob(glob.escape(path_to_look) + '/*.json')
        self.entries = []

        for entry in entries_path:
            self.entries.append(self.readEntry(entry))
        self.saveLib()
        
    def readEntry(self, entry_path):
        with open(entry_path, 'r') as json_file:
            entry_data = json.load(json_file)
            candidate_entry = entry()
            if 'name' in entry_data:
                candidate_entry.setName(entry_data['name'])
            if 'type' in entry_data:
                candidate_entry.setType(entry_data['type'])
            if 'sound' in entry_data:
                candidate_entry.setSoundData(entry_data['sound'])
            if 'image' in entry_data:
                candidate_entry.setImageData(entry_data['image'])
            candidate_entry.setFilename(Path(entry_path).name)
        return candidate_entry

    def saveLib(self, name='data.json'):
        if not self.entries:
            print("PREVENTING OVERWIRITING DATABASE WITH EMPTY DATA, PLEASE PERFORM A NEW DISCOVERY FIRST!")

        else:
            database_template = {
                "data_entry" : []
            }

            def entry_template():
                return {
                    "index" : "",
                    "name" : "",
                    "type" : "",
                    "source" : "",
                    "colorspace" : "",
                    "filename" : ""
                }

            entries_to_save = []
            for index, data in enumerate(self.entries):
                ent = entry_template()
                ent["index"] = index
                ent["name"] = data.getName()
                ent["type"] = data.getType()
                ent["filename"] = data.getFilename()
                entries_to_save.append(ent)
            
            database_template["data_entry"] = entries_to_save

            json_data = json.dumps(database_template, indent=4)
            json_filename = self.project_path/'Data'/name

            with open(json_filename, 'w') as file:
                file.write(json_data)

    def getType(self, obj_type, random = False, n = 0):
        database_location = self.project_path/'Data'/'data.json'
        with open(database_location, 'r') as database:
            database_data = json.load(database)
            entries_type = []
            for entry in database_data['data_entry']:
                if entry['type'] == obj_type:
                    entries_type.append(entry['filename'])
            if random:
                file_location = self.project_path/'Data'/'Database'/choice(entries_type)
                return self.readEntry(file_location)
            #If random element option wasn't choosen return the n one
            
            if n < len(entries_type):
                file_location = self.project_path/'Data'/'Database'/entries_type[n]
                return self.readEntry(file_location)
            else:
                raise Exception(f'There are only {len(entries_type)} exemples available for {obj_type} type!')
            
            



#How the database works?
#The main file is data.json which stores all the entries and is automatic updated aka should not be touched. Then in /Database the enties file can be found and modified/added.
#In priciple you add the new data (sound in sound folder, image in image folder) and then create a new entry in /Database with the requierd info.
#The code shoud perform a discovery and update the database each time you initiate a new object


if __name__=='__main__':
    #test = example()
    #print(test.getType('galaxy'))
    print('You are not supposed to run this file, did something went wrong?')
from pathlib import Path
from scipy.io import wavfile
from random import choice
import glob
import json

class example:
    def __init__(self, random = False, n = 0, type='', ):
        self.project_path  = Path(__file__).parent

    def setEs(self):
        pass

    def loadLib(self, name='data.json'):
        pass

    def discoverLib(self):
        path_to_look = self.project_path/'Data'/'Database'
        #Look in the Database folder and find all json entries
        entries = glob.glob(glob.escape(path_to_look) + '/*.json')

        for entry in entries:
            with open(entry, 'r') as json_file:
                entry_data = json.load(json_file)

    def saveLib(self, name='data.json'):
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

        entries = []
        for index, data in enumerate(range(10)):
            ent = entry_template()
            ent["index"] = index
            ent["name"] = 'M31'
            ent["type"] = 'galaxy'
            ent["filename"] = 'm31.json'
            entries.append(ent)
        
        database_template["data_entry"] = entries

        json_data = json.dumps(database_template)
        json_filename = self.project_path/'Data'/name

        with open(json_filename, 'w') as file:
            file.write(json_data)

            
"""
def example(random = False, n = 0):
    files = glob.glob(glob.escape(project_path) + "/Data/*.wav")
    if random:
        file = choice(files)
    elif n < len(files):
        file = files[n]
    else:
        raise Exception(f'There are only {len(files)} exemples available!')
    print(f'Example is {file}')
    return wavfile.read(file)

"""

if __name__=='__main__':
    test = example()
    test.discoverLib()
    print('You are not supposed to run this file, did something went wrong?')
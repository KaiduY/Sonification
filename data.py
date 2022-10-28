from pathlib import Path
from scipy.io import wavfile
from random import choice
import glob

project_path  = Path(__file__).parent

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


if __name__=='__main__':
    print('You are not supposed to run this file, did something went wrong?')
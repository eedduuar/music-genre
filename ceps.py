# This code is supporting material for the book
# Building Machine Learning Systems with Python
# by Willi Richert and Luis Pedro Coelho
# published by PACKT Publishing
#
# It is made available under the MIT License

# Convert to wav :
# find pop/ -iname "*.au" -exec sox -V3 {} {}.SOX.wav \;
#http://stefaanlippens.net/audio_conversion_cheat_sheet
#sox reggae.mp3 reggae.wav rate 22050 trim 0 30 channels 1

import os
import glob
import sys

import numpy as np
import scipy
import scipy.io.wavfile
from scikits.talkbox.features import mfcc

from utils import GENRE_DIR


def write_ceps(ceps, fn):
    """
    Write the MFCC to separate files to speed up processing.
    """
    base_fn, ext = os.path.splitext(fn)
    data_fn = base_fn + ".ceps"
    np.save(data_fn, ceps)
    print("Written %s"%data_fn)


def create_ceps(fn):
    sample_rate, X = scipy.io.wavfile.read(fn)

    ceps, mspec, spec = mfcc(X)
    write_ceps(ceps, fn)


def read_ceps(genre_list, base_dir=GENRE_DIR):
    X = []
    y = []
    for label, genre in enumerate(genre_list):
        print str(label)+genre
        for fn in glob.glob(os.path.join(base_dir, genre, "*.ceps.npy")):
            ceps = np.load(fn)
            num_ceps = len(ceps)
            X.append(
                np.mean(ceps[int(num_ceps / 10):int(num_ceps * 9 / 10)], axis=0))
            y.append(label)

    return np.array(X), np.array(y)


def read_ceps_test(test_file):
    """
        Reads the MFCC features from disk and
        returns them in a numpy array.
    """
    X = []
    y = []
    ceps = np.load(test_file)
    num_ceps = len(ceps)
    X.append(np.mean(ceps[int(num_ceps / 10):int(num_ceps * 9 / 10)], axis=0))
    return np.array(X), np.array(y)






if __name__ == "__main__":
    os.chdir(GENRE_DIR)
    glob_wav = os.path.join(GENRE_DIR+"/"+sys.argv[1], "*.wav")
    print(glob_wav)
    for fn in glob.glob(glob_wav):
        create_ceps(fn)

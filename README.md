# README #

Librerías para clasificar canciones en base a archivos .wav

### What is this repository for? ###

* Version 0.01
* Basado en  [Building Machine Learning Systems With Python](https://github.com/luispedro/BuildingMachineLearningSystemsWithPython/tree/master/ch09)

### Setup ###

* Dependencies: librerias de python :
* * sudo apt-get install libatlas-base-dev gfortran
* * sudo apt-get install libav-tools
* * sudo pip install requirements.txt

* MP3 to Wav convertion

* * sudo apt-get install sox
* * sudo apt-get install libsox-fmt-mp3

### Run ###

* Download training Set : http://opihi.cs.uvic.ca/sound/genres.tar.gz
* Format convertion (training set): find pop/ -iname "*.au" -exec sox -V3 {} {}.SOX.wav \;
* Format convertion (test set) : sox reggae.mp3 reggae.wav rate 22050 trim 0 30 channels 1
* Format convertion (for all test set): find . -iname "*.mp3" -exec sox {} {}.wav rate 22050 trim 0 30 channels 1 \;

* python ceps.py <folder name> (generate ceps for genre folder)
* * generate for each folder:  find ../genres/ -type d -exec python ceps.py {} \;
* python 02_ceps_based_classifier.py  (generate model)
* python tester.py <test file> (test model)
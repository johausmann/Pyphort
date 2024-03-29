#!/usr/bin/env python3
import os
import sys
import subprocess

usage='''
Usage: copyright.py [input dir] [output dir] [watermark string] 
'''

try:
    subprocess.check_call(['convert','-version'])

except subprocess.CalledProcessError:
    print("Please install the GraphicsMagic tool")

if len(sys.argv) < 4:
    print(usage)
    quit()

if not os.path.isdir(sys.argv[2]):
    os.makedirs(sys.argv[2])
    
files =[]
inputdir=os.path.realpath(sys.argv[1])
outputdir=os.path.realpath(sys.argv[2])

with os.scandir(inputdir) as dir:
    for entry in dir:
        if entry.is_file():
            files.append(os.path.join(inputdir,entry))

for pic in files:
    
    # generate output name
    basename = os.path.splitext(os.path.basename(pic))[0]
    extension = os.path.splitext(os.path.basename(pic))[1]
    output = os.path.join(outputdir,basename+"_watermarked"+extension)
    
    # create commmand
    command='convert'
    options= ' '.join([
        '-font', '/usr/share/fonts/TTF/Cascadia.ttf',
        '-pointsize', '50', 
        '-draw', '\"gravity south fill black text 0,12', '\'', sys.argv[3], '\'',
        'fill white text 1,11', '\'' , sys.argv[3], '\'' , '\"',
        pic, output
        ])
    process=(' '.join([command,options]))
    
    # call subprocess
    print(process)
    print('-----' *4)
    subprocess.call([process], shell=True)

#   306 	 2017:06:04 14:18:20 	 DateTime
# 36867 	 2017:06:04 14:18:20 	 DateTimeOriginal
# 36868 	 2017:06:04 14:18:20 	 DateTimeDigitized

import os
import datetime
import piexif
import struct
from datetime import timedelta
from PIL import Image
from PIL.ExifTags import TAGS
CONST_ChangeName ="n"#n /y
CONST_movetime = 239
CONST_path = "C:\\Aneta_2\\EDU\\RadaRodzicow\\tmp\\"

def get_date_taken(path):
    return Image.open(path)._getexif()[36867]


def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
        print(tag,"<<\t", value,"\t", decoded, ">>\n")

    return ret




def moveDate (path) :
#    path2 = 'DSC_0659.JPG'
    im = Image.open(path)
    exifBin= piexif.load(im.info["exif"])

    date1 = datetime.datetime.strptime(exifBin['0th'][306].decode('utf-8'), "%Y:%m:%d %H:%M:%S")
    date2= date1-timedelta(seconds=CONST_movetime )

#    print(date1,"***", date2, "<><>",get_date_taken(path))
    date_bytes = bytes(date2.strftime("%Y:%m:%d %H:%M:%S"), "utf-8")
    exifBin['0th'][306]=date_bytes
    exifBin['Exif'][36867]=  date_bytes
    exifBin['Exif'][36868] =  date_bytes

    exif2 =  piexif.dump(exifBin)

    pos = path.find(".", len(path)-4)
    if (CONST_ChangeName =='Y') |(CONST_ChangeName=="y") :
        newPath = path[0:pos]+"_m.jpg"
    else :
        newPath =path

    im.save(newPath, "jpeg",  exif=exif2,  quality='keep' )



import os, sys
path = CONST_path
dirs = os.listdir( path )

for file in dirs:
    if file.endswith(".JPG") |  file.endswith(".jpg"):
        pathM= path+file
        print(file, "\t", pathM)
        moveDate(pathM)


#!/bin/bash

IMGS=./src/*.png
IMGS=./images/*.png
for i in ${IMGS} ; do
    src=${i}
    dest=${i%.*}.jpg
    echo "Convert <${src}> to <${dest}>"
    convert "$i" "${i%.*}.jpg" ;
done

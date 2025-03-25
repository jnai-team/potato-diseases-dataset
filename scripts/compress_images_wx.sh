#! /bin/bash 
###########################################
# 压缩图片，减少存储空间
# https://legacy.imagemagick.org/Usage/resize/#resize
# depend on 
# Version: ImageMagick 7.1.0-30 Q16-HDRI x64 c8ecfc4:20220416 https://imagemagick.org
###########################################

# constants
baseDir=$(cd `dirname "$0"`;pwd)
cwdDir=$PWD
export PYTHONUNBUFFERED=1
export PATH=/opt/miniconda3/envs/venv-py3/bin:$PATH
export TS=$(date +%Y%m%d%H%M%S)
export DATE=`date "+%Y%m%d"`
export DATE_WITH_TIME=`date "+%Y%m%d-%H%M%S"` #add %3N as we want millisecond too

# functions

# main 
[ -z "${BASH_SOURCE[0]}" -o "${BASH_SOURCE[0]}" = "$0" ] || return
cd $baseDir/..

if [ ! -d tmp ]; then
    mkdir tmp
fi

TMP_DIR=$baseDir/../tmp

for x in `find . -name "微信图片*"`; do 
    echo $x
    filename=`basename $x`
    cp $x $TMP_DIR/$filename
    convert $TMP_DIR/$filename -resize 256x256\! $x
done
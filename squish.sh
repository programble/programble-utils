#!/bin/bash
# Licensed under the WTFPL

if [ ! $1 ]; then
    echo "HALP"
    exit 1
fi

# Does the first argument specify an action?
if [[ ${1:0:1} == "-" ]]; then
    ACTION=${1:1}
    TARGET=$2
else
    TARGET=$1
fi

# Auto-detect action
if [ ! $ACTION ]; then
    if [[ ${TARGET:0:7} == "http://" ]] || [[ ${TARGET:0:4} == "www." ]]; then
        ACTION=isgd
    fi
    if [ -f $TARGET ]; then
        if [[ ${TARGET##*.} == "png" ]] || [[ ${TARGET##*.} == "jpg" ]]; then
            ACTION=thumb
        else
            ACTION=gzip
        fi
    fi
    if [ -d $TARGET ]; then
        ACTION=targzip
    fi
fi

# If we still don't know what to do
if [ ! $ACTION ]; then
    echo "I do not know what to do with $TARGET"
    exit 2
fi

# If we have nothing to do it to
if [ ! $TARGET ]; then
    echo "I do not know what to $ACTION"
    exit 3
fi

case $ACTION in
    isgd)
        curl http://is.gd/api.php?longurl=$TARGET 2> /dev/null
        echo
    ;;
    thumb)
        convert $TARGET -thumbnail x128 ${TARGET/./_thumb.}
        echo ${TARGET/./_thumb.}
    ;;
    gzip)
        gzip $TARGET
        echo ${TARGET}.gz
    ;;
    bzip2)
        bzip2 $TARGET
        echo ${TARGET}.bz2
    ;;
    targzip)
        tar caf ${TARGET%/}.tar.gz $TARGET
        echo ${TARGET%/}.tar.gz
    ;;
    tarbzip2)
        tar caf ${TARGET%/}.tar.bz2 $TARGET
        echo ${TARGET%/}.tar.bz2
    ;;
    install)
        if [ $EUID -eq 0 ]; then
            cp $TARGET /usr/bin/sq
            echo /usr/bin/sq
        else
            cp $TARGET ~/bin/sq
            echo ~/bin/sq
        fi
    ;;
    *)
        echo "I do not know how to $ACTION $TARGET"
        exit 4
    ;;
esac

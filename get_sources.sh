#!/bin/bash

if [ -e "qutim" ]
then
    cd qutim
    git pull
    git submodule update --init --recursive
else
    git clone git://github.com/euroelessar/qutim.git
    cd qutim
fi

git submodule update --init --recursive
GITCOMMIT=`git rev-parse --short HEAD`
echo $GITCOMMIT
cd ..

if [ -e qutim-0.3-git$GITCOMMIT.tar.xz ]
then
    echo "Sources already exist"
else
    tar c qutim | xz --best > qutim-0.3-git$GITCOMMIT.tar.xz
fi
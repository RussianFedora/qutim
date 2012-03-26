#!/bin/bash

ORIGNAME=qutim
VERSION=0.3
GIT_REVISION=ed0e703
NAME=${ORIGNAME}-${VERSION}.git

rm -rf ${ORIGNAME}
git clone git://github.com/euroelessar/qutim.git &>/dev/null
cd $ORIGNAME
git submodule update --init --recursive
cd ..
mv ${ORIGNAME} ${NAME}
find ${NAME} -name ".git" -exec rm -rf {} \; 2>/dev/null

tar cfJ ${NAME}.tar.xz ${NAME}
rm -rf ${NAME}

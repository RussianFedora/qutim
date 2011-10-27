#!/bin/bash

ORIGNAME=qutim
VERSION=0.3
GIT_REVISION=b2dfec3
NAME=${ORIGNAME}-${VERSION}.git

rm -rf ${ORIGNAME}
git clone git://github.com/euroelessar/qutim.git &>/dev/null
cd $ORIGNAME
git submodule update --init --recursive
cd ..
mv ${ORIGNAME} ${NAME}

tar cfJ ${NAME}.tar.xz ${NAME}
rm -rf ${NAME}

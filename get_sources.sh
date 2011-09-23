#!/bin/bash

ORIGNAME=qutim
VERSION=0.3
GIT_REVISION=a4487a5ae6
NAME=${ORIGNAME}-${VERSION}.git

rm -rf ${ORIGNAME}
git clone git://github.com/euroelessar/qutim.git &>/dev/null
git submodule update --init --recursive
mv ${ORIGNAME} ${NAME}

tar cfJ ${NAME}.tar.xz ${NAME}
rm -rf ${NAME}

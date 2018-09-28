#!/bin/bash

if [ -e a.out ]
then
  rm a.out
fi


g++ $1
./a.out

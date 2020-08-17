#!/bin/bash
#Str="Ada file .java pada "
#find .. / -name '*.java'

function cari (){

search=$(find ../ -name '*.java')
str="Ada file java pada $Search"
echo $str
}

val=$(cari)
echo "$val"


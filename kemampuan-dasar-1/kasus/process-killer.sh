#!/bin/bash
echo "Masukkan nama program yang akan di stop: "
read app
PID=`ps -eaf | grep $app | awk '{print$2}'`
if [[ "" != "$PID" ]]; then
	echo "killing $PID"
	kill -9 $PID
fi


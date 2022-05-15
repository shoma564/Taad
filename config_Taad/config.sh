#!/bin/bash

cp -fR ../key/ /etc/

pp=/key/auth.sh
mozi=$1$pp
echo $mozi

sed -i "s|chikan|${mozi}|g" /etc/key/auth.service
sed -i "s|chikan|${1}/key/|g" /etc/key/auth.sh

cp -f /etc/key/auth.service /etc/systemd/system/
#mv /etc/systemd/system/auth.service.cp /etc/systemd/system/auth.service

cp -fR /etc/key/ $1

systemctl daemon-reload
systemctl enable auth.service
systemctl start auth.service
systemctl restart auth.service

clear && rm -fR ../../Taad

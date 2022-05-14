#!/bin/bash

cp -fR  ../key/ /etc/

pp=/key/auth.sh
mozi=$1$pp
echo $mozi

sed 's/chikan/"$mozi"/g' /etc/key/auth.service > /etc/key/auth.service



cp -f /etc/key/auth.service /etc/systemd/system/
#mv /etc/systemd/system/auth.service.cp /etc/systemd/system/auth.service

mv /etc/key/ $1

systemctl daemon-reload
systemctl enable auth.service
systemctl start auth.service


#clear && rm -f ./config.sh

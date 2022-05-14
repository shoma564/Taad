#!/bin/bash
pp=/keys/auth.service
mozi=$1pp
sed 's/chikan/$mozi/g' /etc/keys/auth.service
cp /etc/keys/auth.service /etc/system/systemd/
systemctl daemon-reload
systemctl enable auth.service

mv /etc/keys/ $mozi
rm ./config.sh

systemctl daemon-reload
systemctl enable auth.service
systemctl start auth.service
 


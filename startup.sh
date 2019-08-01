#!/bin/bash
echo "root:mar" | chpasswd
/etc/init.d/ssh restart
cd /app
python3 app.py
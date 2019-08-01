#!/bin/bash
/etc/init.d/ssh restart
cd /app
python3 app.py
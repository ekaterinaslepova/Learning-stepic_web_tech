sudo ﻿ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#sudo ln -s /home/box/web/etc/hello.py   /etc/gunicorn.d/hello.py
#sudo /etc/init.d/gunicorn /home/box/web/hello:application --bind 0.0.0.0:8080
sudo /etc/init.d/gunicorn ask.wsgi:application --bind 0.0.0.0:8000

mysql -uroot -e "create database db_qa"
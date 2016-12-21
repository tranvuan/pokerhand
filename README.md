Pokerhand python webapp with: Webpy + Nginx + FastCgi

1. You need to download and install:

web.py-0.38.tar.gz
+ webpy package: sudo python setup.py install

flup-1.0.2.tar.gz
+ flup package: sudo python setup.py install

spawn-fcgi-1.6.4.tar.gz
+ spawn-fcgi: ./configure & make & sudo make install

2. Then add nginx config to site-available, and ln -s to site-enabled
The nginx virtual host file is in `nginx` folder

3. Start & stop nginx: 
   $ sudo nginx
   $ sudo nginx -s stop

4. Start & stop webpy with nginx and fastcgi:
   $ ./start.sh (please refer to start-template.sh)
   $ ./stop.sh (please refer to stop-template.sh)
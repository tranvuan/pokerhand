# Pokerhand python webapp with: Webpy + Nginx + FastCgi

## Description: Pokerhand takes two inputs: list of pot cards (3 to 5 cards) and list of hand cards (2 cards). Note: there is no input validation right now.

## Demonstration
#### This webapp is host online. So it can be viewed by setting host:
####      130.211.246.221    pokerhand.com
#### and visit http://pokerhand.com


#####[1] You need to download and install:

+ webpy package: web.py-0.38.tar.gz

    $sudo python setup.py install
    
+ flup package: flup-1.0.2.tar.gz

    $ sudo python setup.py install

+ spawn-fcgi: spawn-fcgi-1.6.4.tar.gz

    $ ./configure & make & sudo make install

#####[2] Then add nginx config to site-available, and ln -s to site-enabled

The nginx virtual host file is in `nginx` folder

#####[3] Start & stop nginx: 

    $ sudo nginx

    $ sudo nginx -s stop

#####[4] Start & stop webpy with nginx and fastcgi:

    $ ./start.sh (please refer to start-template.sh)

    $ ./stop.sh (please refer to stop-template.sh)

#!/bin/bash

echo "configuring modules"
echo "fbtft_device" >> /etc/modules-load.d/modules.conf
echo "options fbtft_device custom name=adafruit18 gpios=reset:1,dc:0,led:3 width=128 height=128 busnum=1" > /etc/modprobe.d/fbtft.conf
echo "blacklist bmp085" > /etc/modprobe.d/blacklist.conf

echo "installing required packages"
export DEBIAN_FRONTEND=noninteractive
apt-get install python-pygame python-netifaces build-essential libi2c-dev i2c-tools python-dev libffi-dev mariadb-client mariadb-server python-pymysql apache2 php5 php-pear php5-mysql -y
pip install smbus-cffi==0.5.1

echo "configuring database"
echo -n "mysql root password: "
read rootpass
echo -n "meteo mysql user name: "
read meteouser
echo -n "meteo mysql user password: "
read meteouserpassword
echo -n "meteo database name: "
read meteobasename
datagettime='none'
while [[ ! $datagettime =~ ^[0-9]+$ ]]
do
 echo -n "Sensors data receiving frequency (seconds): "
 read datagettime
 if [[ ! $datagettime =~ ^[0-9]+$ ]]; then
  echo "!!!Must be a number!!!"
 fi
done
{
 echo "SET @rootpass='${rootpass}';"
 cat mysqlinit.sql
} | mysql -u root
mysql --user=root --password=${rootpass} -e "CREATE USER ${meteouser}@'localhost' IDENTIFIED BY '${meteouserpassword}'; \
CREATE DATABASE ${meteobasename}; \
GRANT USAGE ON *.* TO ${meteouser}@localhost IDENTIFIED BY '${meteouserpassword}'; \
GRANT all privileges ON ${meteobasename}.* TO ${meteouser}@localhost; \
FLUSH PRIVILEGES;"

echo "Generating config files"
mkdir /etc/optimeteo
echo "meteouser = \"$meteouser\"\nmeteouserpassword = \"$meteouserpassword\"\nmeteobasename = \"$meteobasename\"\ndatagettime = \"$datagettime\"\n" > /etc/optimeteo/config.py

echo "configuring autostart"
SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
sed -e s/exit\ 0//g -i /etc/rc.local
sed -e s/will\ \"\"\ on\ success/will\ \"\exit\ 0\"\ on\ success/g -i /etc/rc.local
echo "python $SCRIPTPATH/main.py &" >> /etc/rc.local
echo "sleep 30 && python & $SCRIPTPATH/bme280.py -b 0 -a 76 &" >> /etc/rc.local
echo "sleep 60 && python & $SCRIPTPATH/bme280.py -b 0 -a 77 &" >> /etc/rc.local
echo "exit 0" >> /etc/rc.local

echo "Web app magic"
rm -f /var/www/html/index.html
cp ./webapp/index.php /var/www/html/index.php
cp ./webapp/pyconfpars.php /var/www/html/pyconfpars.php
cp ./webapp/dbconnector.php /var/www/html/dbconnector.php
mkdir /var/www/html/js
cp ./webapp/js/index.js /var/www/html/js/index.js

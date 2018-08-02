import pymysql.cursors
import sys
sys.path.insert(0, '/etc/optimeteo')
import config

def tablecheck (tablename):
 connection = pymysql.connect(host='localhost',
                              user=config.meteouser,
                              password=config.meteouserpassword,
                              db=config.meteobasename,
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor)
 cursor = connection.cursor()
 cursor.execute("SHOW TABLES like '%s'" % (tablename))
 result = cursor.fetchall()
 if not result:
  cursor.execute("CREATE TABLE `%s` (`id` INT(11) NOT NULL AUTO_INCREMENT, `datetime` DATETIME(0) NOT NULL, `temp` DOUBLE(3,1) NOT NULL, `pres` DOUBLE(12,8) NOT NULL, `humi` DOUBLE(12,10) NOT NULL, PRIMARY KEY(`id`))" % (tablename))
 

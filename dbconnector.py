import pymysql.cursors

def tablecheck (tablename,dbuser,dbpassword,dbname):
 connection = pymysql.connect(host='localhost',
                              user=dbuser,
                              password=dbpassword,
                              db=dbname,
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor)
 cursor = connection.cursor()
 cursor.execute("SHOW TABLES like '%s'" % (tablename))
 result = cursor.fetchall()
 if not result:
  cursor.execute("CREATE TABLE `%s` (`id` INT(11) NOT NULL AUTO_INCREMENT, `datetime` DATETIME(0) NOT NULL, `temp` DOUBLE(3,1) NOT NULL, `pres` DOUBLE(12,8) NOT NULL, `humi` DOUBLE(12,10) NOT NULL, PRIMARY KEY(`id`))" % (tablename))
 connection.close()
 

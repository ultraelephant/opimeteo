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
  print ('Creating ' +tablename+ ' table')
  cursor.execute("CREATE TABLE `%s` (`id` INT(11) NOT NULL AUTO_INCREMENT, `datetime` DATETIME(0) NOT NULL, `temp` DOUBLE(4,2) NOT NULL, `pres` DOUBLE(12,8) NOT NULL, `humi` DOUBLE(12,10) NOT NULL, PRIMARY KEY(`id`))" % (tablename))
 connection.close()
 
def commitdata (tablename,dbuser,dbpassword,dbname,temp,pres,humi):
 try:
  connection = pymysql.connect(host='localhost',
                               user=dbuser,
                               password=dbpassword,
                               db=dbname,
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
  cursor = connection.cursor()
  cursor.execute ("INSERT INTO %s (datetime,temp,pres,humi) VALUES(CURRENT_TIMESTAMP(),'%s','%s','%s')" % (tablename,temp,pres,humi))
  connection.commit()
  connection.close()
 except pymysql.err.ProgrammingError:
  tablecheck (tablename,dbuser,dbpassword,dbname)
  commitdata (tablename,dbuser,dbpassword,dbname,temp,pres,humi)

def getdata (dbuser,dbpassword,dbname):
 connection = pymysql.connect(host='localhost',
                              user=dbuser,
                              password=dbpassword,
                              db=dbname,
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor)
 cursor = connection.cursor()
 cursor.execute ("SHOW TABLES like 'bme280_%'")
 tables = cursor.fetchall()
 result = []
 for table in tables:
  cursor.execute ("SELECT temp, pres, humi FROM " + table.values()[0] + " ORDER BY id DESC LIMIT 1;")
  bufresult = cursor.fetchall()
  bufresult[0]["tablename"]=(table.values()[0])
  result.extend(bufresult)
 connection.close()
 return result

import sys
sys.path.insert(0, '/etc/optimeteo')
import config
import dbconnector

dbconnector.houskeeping (config.meteouser,config.meteouserpassword,config.meteobasename,config.keeptime)

<?php 

include "pyconfpars.php";

$getvalue_dbname = isset($_POST['getvalue_dbname']) ? $_POST['getvalue_dbname'] : false;
if ($getvalue_dbname)
{
 $config = pyconfpars('/etc/optimeteo/config.py');
 $link = mysql_connect('localhost', $config['meteouser'], $config['meteouserpassword']) or die('Unable to connect: ' . mysql_error());
 $query = "SELECT datetime, temp, pres, humi FROM " . $getvalue_dbname . " ORDER BY id DESC LIMIT 1;";
 mysql_select_db($config['meteobasename']) or die('Unable to select DB');
 $result = mysql_query($query) or die('Unable to process query: ' . mysql_error());
 while ($lastrow = mysql_fetch_array($result))
 {
  $results[] = $lastrow;
 }
 echo "Temperature: " . $results[0]['temp'] . "</br>";
 echo "Humidity: " . $results[0]['humi'] . "</br>";
 echo "Pressure: " . $results[0]['pres'] . "</br>";
 echo "Timestamp: " . $results[0]['datetime'] . "</br>";
}

?>

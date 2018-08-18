<?php 

function getdatatables($dbusername,$dbpassword,$dbname)
{
 $link = mysql_connect('localhost', $dbusername, $dbpassword) or die('Unable to connect: ' . mysql_error());
 $query = "SHOW TABLES like 'bme280_%'";
 mysql_select_db($dbname) or die('Unable to select DB');
 $result = mysql_query($query) or die('Unable to process query: ' . mysql_error());
 $results = array();
 while ($table = mysql_fetch_array($result))
 {
  array_push($results, $table[0]);
 }
 return $results;
}

?>

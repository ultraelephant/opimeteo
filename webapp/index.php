<?php 

include "pyconfpars.php";
include "dbconnector.php";

$config = pyconfpars('/etc/optimeteo/config.py');

echo "<script src='js/index.js'></script>";

echo "<select id='getvalue_dbname' onchange='posttogetvalues(this.value);'>";
foreach (getdatatables($config['meteouser'],$config['meteouserpassword'],$config['meteobasename']) as $table) 
{
 echo "<option value='" . $table . "'>" . $table . "</option>";
}
echo "</select></br>";
echo "</br><span id='values'></span>"

?>

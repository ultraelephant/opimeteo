<?php 

include "pyconfpars.php";
include "dbconnector.php";

$config = pyconfpars('/etc/optimeteo/config.py');

echo "<select>";
foreach (getdatatables($config['meteouser'],$config['meteouserpassword'],$config['meteobasename']) as $table) 
{
 echo "<option value='" . $table . "'>" . $table . "</option>"; 
}
echo "</select>";

?>

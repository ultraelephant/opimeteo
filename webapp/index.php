<?php 

include "pyconfpars.php";
include "dbconnector.php";

$config = pyconfpars('/etc/optimeteo/config.py');

echo "<script src='js/jquery-3.3.1.min.js'></script>";
echo "<script src='js/index.js'></script>";

echo "<form method='post' action='getvalues.php'>";
//echo "<select id='getvalue_dbname' name='getvalue_dbname' onchange='this.form.submit()'>";
echo "<select id='getvalue_dbname'>";
foreach (getdatatables($config['meteouser'],$config['meteouserpassword'],$config['meteobasename']) as $table) 
{
 echo "<option value='" . $table . "'>" . $table . "</option>";
}
echo "</select>";
echo "</form>";
echo "<span id='values'></span>"

?>

<?php 

function pyconfpars($conf_path)
{
 $python_config = file_get_contents($conf_path);
 $python_config_rows = explode("\n", $python_config);

 array_pop($python_config_rows);

 $configpy = array();

 foreach($python_config_rows as $row => $data)
 {
  $row_data = explode(' = ', $data);
  $row_data[1] = str_replace('"', '', $row_data[1]);
  $configpy[$row_data[0]] = $row_data[1];
 }

 return $configpy;
}

?>

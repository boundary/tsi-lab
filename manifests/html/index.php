<!DOCTYPE html>
<html>
 <head>
  <title>PHP Test</title>
 </head>
 <body>
 <?php echo '<p>Hello World</p>'; ?> 
 <?php
  $codes = array(200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 401, 404, 404, 404, 404, 500);
  $key = array_rand($codes, 1);
  $http_status = $codes[$key];
  echo "<p>Sending result code: $http_status</p>";
  http_response_code($codes[$key]);
  ?> 
 </body>
</html>

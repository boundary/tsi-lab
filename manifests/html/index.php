<!DOCTYPE html>
<html>
 <head>
  <title>PHP Test</title>
 </head>
 <body>
 <?php echo '<p>Hello World</p>'; ?> 
 <?php
  $codes = array(200, 201, 202, 400, 401, 404, 422, 500, 503, 504);
  $key = array_rand($codes, 1);
  echo "<p>$codes[$key]</p>";
  ?> 
 </body>
</html>

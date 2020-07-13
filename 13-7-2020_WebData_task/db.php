<?php
$con=mysqli_connect('localhost','root','','student');
if(!$con)
{
    echo "Connection error".mysqli_connect_error();
}
else
   echo "<h3>Database connection success</h3>";


?>
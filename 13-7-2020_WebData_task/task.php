<?php
include 'db.php';
if(isset($_POST['submit']))
{
  $studentid=$_POST['studentid'];
  $query="SELECT * FROM `users` WHERE `stud_id`='$studentid'";
  $run=mysqli_query($con,$query);
  $row=mysqli_num_rows($run);
  if($row==1)
  {
    echo "Data Found successfully". "<br>";
    $data=mysqli_fetch_assoc($run);
    
    echo "Student id:". $data['stud_id'] . "<br>" ;
    echo "Student Name:". $data['stud_name'] . "<br>";
    echo "Branch:". $data['branch'] . "<br>";
    echo "CGPA:" . $data['cgpa'];
  }
  else{
     echo "No entered id found";
   }

}


  
?>
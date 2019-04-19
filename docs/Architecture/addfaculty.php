<?php
include_once 'dbconnect.php';
	session_start();
  if(!isset($_SESSION['logintype'])){
header("location:login.php");
}
elseif($_SESSION['logintype']==2){
  header('Location: studentpage.php');}
elseif($_SESSION['logintype']==3){
  header('Location: facultypage.php');}
if (!empty($_POST['action'])) {
	if (!empty($_POST['name'])&&!empty($_POST['pass'])&&!empty($_POST['department'])&&!empty($_POST['f_id'])&&!empty($_POST['email'])){
  if (isset($_POST['name'])) { $name = $_POST['name']; }
	if (isset($_POST['pass'])) { $pass = $_POST['pass']; }
  if (isset($_POST['department'])) { $department = $_POST['department']; }
  if (isset($_POST['f_id'])) { $f_id = $_POST['f_id']; }
  if (isset($_POST['email'])) { $email = $_POST['email']; }
	if (isset($_POST['type'])) { $type = $_POST['type']; }

		//Inserting values into faculty Table
		if($name!='' || $pass!=''||$email!=''){
			$result = mysql_query("INSERT INTO faculty VALUES ('$f_id', '$name','$department', '$email','$pass','$type')");
		}
	}else{
		// echo '<script type="text/javascript">
		// alert("please enter all the credentials...");
		// </script>';
	}
  }
?>
<!DOCTYPE html>
	<head>
		<title>Add Faculty - Admin</title>
		<link rel="stylesheet" type="text/css" href="admin.css">
    <link rel="stylesheet" type="text/css" href="w3.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Tangerine">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <style>
html, body, h1, h2, h3, h4, h5, h6 {
  font-family: "Comic Sans MS", cursive, sans-serif;
}
.w3-tangerine {
    font-family: "Tangerine", serif;
}
</style>
	</head>
	<body class="w3-container w3-cyan">
		<header>
      <div class="w3-panel w3-card-4 w3-sand w3-xxxlarge  w3-tangerine w3-serif w3-padding-16 w3-center">
        <i>Add a Faculty:</i>
      </div>
			<a href="logout.php">
				<button class="w3-display-topright w3-btn w3-hover-shadow w3-tangerine w3-xxxlarge w3-serif w3-padding-16  w3-margin-right">
					Logout</button>
				</a>
		</header>
		<article class="w3-card-4 ">

  <div class ="input">
<form class="w3-container w3-cyan w3-hover-shadow  w3-margin" action=addfaculty.php method="POST" >
  <div class="w3-row w3-section">
  <div class="w3-col" style="width:50px"><i class="w3-xxlarge fa fa-user"></i></div>
    <div class="w3-rest">
      <input class="w3-input w3-border" name="f_id" type="text" placeholder="Faculty unique id">
    </div>
</div>

<div class="w3-row w3-section">
  <div class="w3-col" style="width:50px"><i class="w3-xxlarge fa fa-user"></i></div>
    <div class="w3-rest">
      <input class="w3-input w3-border" name="name" type="text" placeholder="Faculty Name">
    </div>
</div>

<div class="w3-row w3-section">
  <div class="w3-col" style="width:50px"><i class="w3-xxlarge fa fa-user"></i></div>
    <div class="w3-rest">
      <input class="w3-input w3-border" name="department" type="text" placeholder="Department">
    </div>
</div>

<div class="w3-row w3-section">
  <div class="w3-col" style="width:50px"><i class="w3-xxlarge fa fa-envelope-o"></i></div>
    <div class="w3-rest">
      <input class="w3-input w3-border" name="email" type="text" placeholder="Email">
    </div>
</div>


<div class="w3-row w3-section">
  <div class="w3-col" style="width:50px"><i class="w3-xxlarge fa fa-pencil"></i></div>
    <div class="w3-rest">
      <input class="w3-input w3-border" name="pass" type="text" placeholder="Password">
    </div>
</div>

<div class="w3-row w3-section">
	<div class="w3-rest">
<input class="w3-radio" type="radio" name="type" value="0" checked>
<label>Instructor</label>

<input class="w3-radio" type="radio" name="type" value="1">
<label>Lab Assistant</label>
</div>
</div>


<button class="w3-button w3-block w3-section w3-black w3-ripple w3-padding" type="submit" name="action" value="submit">Add</button>
          </form>
        </div>

		</article>
    <div class=" w3-card-4">

        <?php
        $result = mysql_query("Select * from faculty order by f_id asc");
        echo "<table class=w3-table>";
        echo "<tr>";
        echo 	"<th>Faculty ID</td>";
        echo 	"<th>Name</td>";
        echo "<th>Email</td>";
        echo "<th>Department</td>";
        echo 	"<th>Password</td>";
				echo "<th>Type</td>";
        echo "</tr>";
          while ($row = mysql_fetch_assoc($result)){
            echo "<tr>";
            echo 	"<td>" . $row["f_id"] . "</td>";
            echo 	"<td>" . $row["name"] . "</td>";
            echo 	"<td>" . $row["email"] . "</td>";
            echo 	"<td>" . $row["department"] . "</td>";
            echo 	"<td>" . $row["password"] . "</td>";
						if ($row["type"]==0){
							echo "<td>Instructor</td>";
						}else{
							echo "<td>Lab Assistant</td>";
						}
						echo "<td></td>";
            echo "</tr>";
          }
          echo "</table>";

        ?>
      </div>
	</body>
	<a href="adminpage.php" class=" btn btn-secondary btn-lg active fixed-bottom ">
		<span class="glyphicon glyphicon-circle-arrow-left"></span>back
		</a>
</html>

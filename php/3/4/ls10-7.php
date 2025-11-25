<html> <head>
<title> Task 3.4.5 </title> </head>
<body>

    <?php
        $PARAMS = (isset($_POST))? $_POST : $_GET;
        $user = $PARAMS["user"];
        print "<p>$user, you prefer";
        print "<ul>\n";
        foreach ($PARAMS as $key=>$value){
            if (gettype($value) == "array"){
                print "$key = <br>\n";
                foreach ($value as $v)
                print "$v<br>";
            }
            else{
                print "$key = $value<br>\n";
            }
        }
        print "</ul>\n";
    ?>
 </body> </html>
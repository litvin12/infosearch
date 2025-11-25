<html> <head>
<title> Task 3.4.5 </title> </head>
<body>

    <?php
        $user = $_POST["user"];
        print "<p>$user, you prefer";
        print "<ul>\n";
        foreach ($_POST['hobby'] as $key=>$value) {
            print "<li>$key = $value\n";
        }
        print "</ul>\n";
    ?>
 </body> </html>
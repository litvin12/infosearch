<?php
    $host = "127.0.0.1";
    $user = "root";
    $pass = "rootpass";
    $db   = "sample_database"; 

    $conn = mysqli_connect($host, $user, $pass, $db);

    if (!$conn) {
        die("Нет соединения с MySQL: " . mysqli_connect_error());
    }

    return $conn;
?>

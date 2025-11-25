<?php
    $user = "root";
    $pass = ""; 
    $db = "sample";
    $conn = mysqli_connect("localhost", $user, $pass, $db);
    $table = "domains_brNN";
    if (!$conn) die("Нет соединения с MySQL");
        
    mysqli_select_db($conn, $db) or die ("Нельзя открыть $db: " . mysqli_error($conn));
    return $conn;
?> 
<?php
// z10-4.inc: подключение к базе данных sample_database

$DB_HOST = getenv('DB_HOST') ? getenv('DB_HOST') : '127.0.0.1';
$DB_USER = getenv('DB_USER') ? getenv('DB_USER') : 'root';
$DB_PASS = getenv('DB_PASS') ? getenv('DB_PASS') : 'rootpass';
$DB_NAME = 'sample_database';

$mysqli = new mysqli($DB_HOST, $DB_USER, $DB_PASS, $DB_NAME);

if ($mysqli->connect_errno) {
    echo "<p>Не удалось подключиться к MySQL: (" .
         $mysqli->connect_errno . ") " .
         htmlspecialchars($mysqli->connect_error) . "</p>";
    exit;
}

$mysqli->set_charset('utf8mb4');
?>

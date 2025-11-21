<?php
// ex1.php — создание таблицы notebook в базе sample
$DB_HOST = getenv('DB_HOST') ? getenv('DB_HOST') : '127.0.0.1';
$DB_USER = getenv('DB_USER') ? getenv('DB_USER') : 'root';
$DB_PASS = getenv('DB_PASS') ? getenv('DB_PASS') : 'rootpass';
$DB_NAME = 'sample';

$mysqli = new mysqli($DB_HOST, $DB_USER, $DB_PASS, $DB_NAME);
if ($mysqli->connect_errno) {
    echo "Не удалось подключиться к MySQL: (".$mysqli->connect_errno.")".htmlspecialchars($mysqli->connect_error);
    exit;
}
$mysqli->set_charset('utf8mb4');

$sql_drop = "DROP TABLE IF EXISTS notebook";
$mysqli->query($sql_drop);

$sql_create = "CREATE TABLE notebook (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50),
  city VARCHAR(50),
  address VARCHAR(50),
  birthday DATE,
  mail VARCHAR(20)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4";

if (!$mysqli->query($sql_create)) {
    echo "Нельзя создать таблицу notebook: " . htmlspecialchars($mysqli->error);
} else {
    echo "Таблица notebook успешно создана.";
}

$mysqli->close();
?>
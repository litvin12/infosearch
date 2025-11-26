<?php
// ex5.php — вставляет три записи в notebook (данные захардкожены)
$DB_HOST = getenv('DB_HOST') ? getenv('DB_HOST') : '127.0.0.1';
$DB_USER = getenv('DB_USER') ? getenv('DB_USER') : 'root';
$DB_PASS = getenv('DB_PASS') ? getenv('DB_PASS') : 'rootpass';
$DB_NAME = 'sample_database';

$mysqli = new mysqli($DB_HOST, $DB_USER, $DB_PASS, $DB_NAME);
if ($mysqli->connect_errno) {
    echo "Не удалось подключиться к MySQL: (".$mysqli->connect_errno.")".htmlspecialchars($mysqli->connect_error);
    exit;
}
$mysqli->set_charset('utf8mb4');

$inserts = array(
    "INSERT INTO notebook (name,city,address,birthday,mail) VALUES ('Анна Смирнова','Москва','ул. Ленина, 1','1990-05-12','anna@example.com')",
    "INSERT INTO notebook (name,city,address,birthday,mail) VALUES ('Борис Кузнецов','Санкт-Петербург','пр. Невский, 10','1985-11-30','boris@example.com')",
    "INSERT INTO notebook (name,city,address,birthday,mail) VALUES ('Елена Морозова','Казань','ул. Пушкина, 5','1992-07-20','elena@example.com')"
);

foreach ($inserts as $q) {
    $mysqli->query($q);
}

echo "Добавлено 3 записи (при условии, что таблица notebook существует).";

$mysqli->close();
?>
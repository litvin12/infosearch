<?php
// ex3.php — вывод всех записей таблицы notebook
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

$result = $mysqli->query("SELECT * FROM notebook");
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <title>ex3 — Список записей</title>
</head>
<body>
<h3>Записи в notebook</h3>
<?php
if ($result && $result->num_rows > 0) {
    echo "<table border=1>\n<tr><th>id</th><th>name</th><th>city</th><th>address</th><th>birthday</th><th>mail</th></tr>\n";
    while ($row = $result->fetch_assoc()) {
        echo "<tr>";
        echo "<td>".htmlspecialchars($row['id'])."</td>";
        echo "<td>".htmlspecialchars($row['name'])."</td>";
        echo "<td>".htmlspecialchars($row['city'])."</td>";
        echo "<td>".htmlspecialchars($row['address'])."</td>";
        echo "<td>".htmlspecialchars($row['birthday'])."</td>";
        echo "<td>".htmlspecialchars($row['mail'])."</td>";
        echo "</tr>\n";
    }
    echo "</table>\n";
} else {
    echo "<p>Нет записей.</p>";
}
?>
<p><a href="ex2.php">Добавить запись</a></p>
<p><a href="ex4.php">Редактировать запись</a></p>
</body>
</html>
<?php $mysqli->close(); ?>
<?php
// ex2.php — форма для добавления записей в notebook
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

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = trim($_POST['name'] ?? '');
    $city = trim($_POST['city'] ?? '');
    $address = trim($_POST['address'] ?? '');
    $birthday = trim($_POST['birthday'] ?? '');
    $mail = trim($_POST['mail'] ?? '');

    if ($name !== '' && $mail !== '') {
        $stmt = $mysqli->prepare("INSERT INTO notebook (name,city,address,birthday,mail) VALUES (?,?,?,?,?)");
        $stmt->bind_param('sssss', $name, $city, $address, $birthday, $mail);
        $stmt->execute();
        $stmt->close();
        echo "<p>Запись добавлена.</p>";
    } else {
        echo "<p>Поля 'name' и 'mail' обязательны.</p>";
    }
}
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <title>ex2 — Добавление в notebook</title>
</head>
<body>
    <form method="post" action="">
        <label>Имя: <input type="text" name="name"></label><br>
        <label>Город: <input type="text" name="city"></label><br>
        <label>Адрес: <input type="text" name="address"></label><br>
        <label>Дата рождения (YYYY-MM-DD): <input type="text" name="birthday"></label><br>
        <label>E-mail: <input type="text" name="mail"></label><br>
        <button type="submit">Добавить</button>
    </form>
    <p><a href="ex3.php">Посмотреть все записи</a></p>
</body>
</html>
<?php $mysqli->close(); ?>
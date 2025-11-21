<?php
// ex4.php — выбор записи для редактирования и изменение одного поля
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

// Если пришёл запрос на обновление
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['id']) && isset($_POST['field_name'])) {
    $id = intval($_POST['id']);
    $field = $_POST['field_name'];
    $value = $_POST['field_value'];
    // Белый список полей
    $allowed = array('name','city','address','birthday','mail');
    if (in_array($field, $allowed)) {
        $stmt = $mysqli->prepare("UPDATE notebook SET `".$field."` = ? WHERE id = ?");
        $stmt->bind_param('si', $value, $id);
        $stmt->execute();
        $stmt->close();
        echo "<p>Запись обновлена.</p>";
    } else {
        echo "<p>Неверное имя поля.</p>";
    }
}

// Если id задан в GET (выбрана строка), показываем форму редактирования
$id = isset($_GET['id']) ? intval($_GET['id']) : (isset($_POST['id'])?intval($_POST['id']):0);
$current_row = null;
if ($id>0) {
    $res = $mysqli->query("SELECT * FROM notebook WHERE id=".$id);
    if ($res && $res->num_rows>0) $current_row = $res->fetch_assoc();
}

// Получим все записи для выбора
$all = $mysqli->query("SELECT * FROM notebook");
?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <title>ex4 — Редактирование</title>
</head>
<body>
<h3>Выберите запись для редактирования</h3>
<form method="get" action="">
<?php
if ($all && $all->num_rows>0) {
    while ($r = $all->fetch_assoc()) {
        echo '<label><input type="radio" name="id" value="'.htmlspecialchars($r['id']).'"> ' . htmlspecialchars($r['id']). ' - '.htmlspecialchars($r['name']).'</label><br>';
    }
    echo '<button type="submit">Выбрать</button>';
} else {
    echo '<p>Нет записей.</p>';
}
?>
</form>

<?php if ($current_row): ?>
    <h4>Редактирование записи id=<?= htmlspecialchars($current_row['id']) ?></h4>
    <form method="post" action="">
        <label>Поле: 
            <select name="field_name">
                <option value="name">name</option>
                <option value="city">city</option>
                <option value="address">address</option>
                <option value="birthday">birthday</option>
                <option value="mail">mail</option>
            </select>
        </label>
        <br>
        <label>Новое значение: <input type="text" name="field_value" value=""></label>
        <br>
        <input type="hidden" name="id" value="<?= htmlspecialchars($current_row['id']) ?>">
        <button type="submit">Заменить</button>
    </form>
    <p>Текущие значения:</p>
    <ul>
        <li>name: <?= htmlspecialchars($current_row['name']) ?></li>
        <li>city: <?= htmlspecialchars($current_row['city']) ?></li>
        <li>address: <?= htmlspecialchars($current_row['address']) ?></li>
        <li>birthday: <?= htmlspecialchars($current_row['birthday']) ?></li>
        <li>mail: <?= htmlspecialchars($current_row['mail']) ?></li>
    </ul>
<?php endif; ?>

<p><a href="ex3.php">Просмотреть все записи</a></p>
</body>
</html>
<?php $mysqli->close(); ?>
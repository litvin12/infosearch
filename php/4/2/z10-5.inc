<?php
// z10-5.inc: функции vid_structure() и vid_content()
function vid_structure($table) {
    global $mysqli;
    if (!$mysqli) return;
    $safe_table = $mysqli->real_escape_string($table);
    $res = $mysqli->query("DESCRIBE `".$safe_table."`");
    echo "<h4>Структура таблицы &laquo;".htmlspecialchars($table)."&raquo;</h4>\n";
    if (!$res) {
        echo "<p>Ошибка при получении структуры: ".htmlspecialchars($mysqli->error)."</p>\n";
        return;
    }
    echo "<table border=1>\n<tr><th>Field</th><th>Type</th><th>Null</th><th>Key</th><th>Default</th><th>Extra</th></tr>\n";
    while ($row = $res->fetch_assoc()) {
        echo "<tr>";
        echo "<td>".htmlspecialchars($row['Field'])."</td>";
        echo "<td>".htmlspecialchars($row['Type'])."</td>";
        echo "<td>".htmlspecialchars($row['Null'])."</td>";
        echo "<td>".htmlspecialchars($row['Key'])."</td>";
        echo "<td>".htmlspecialchars($row['Default'])."</td>";
        echo "<td>".htmlspecialchars($row['Extra'])."</td>";
        echo "</tr>\n";
    }
    echo "</table>\n";
}

function vid_content($table) {
    global $mysqli;
    if (!$mysqli) return;
    $safe_table = $mysqli->real_escape_string($table);
    $res = $mysqli->query("SELECT * FROM `".$safe_table."` LIMIT 1000");
    echo "<h4>Содержимое таблицы &laquo;".htmlspecialchars($table)."&raquo;</h4>\n";
    if (!$res) {
        echo "<p>Ошибка при получении содержимого: ".htmlspecialchars($mysqli->error)."</p>\n";
        return;
    }
    // Ассоциативный массив русских названий полей (общий для нескольких таблиц)
    $rus_name = array(
        'id' => 'Идентификатор',
        'name' => 'Имя',
        'city' => 'Город',
        'address' => 'Адрес',
        'birthday' => 'Дата рождения',
        'mail' => 'E-mail',
        'university' => 'Университет'
    );

    $fields = $res->fetch_fields();
    echo "<table border=1>\n<tr>\n";
    foreach ($fields as $f) {
        $col = $f->name;
        $rus = isset($rus_name[$col]) ? $rus_name[$col] : '';
        echo "<th>".htmlspecialchars($rus)."<br>".htmlspecialchars($col)."</th>";
    }
    echo "\n</tr>\n";

    // вывод строк
    while ($row = $res->fetch_assoc()) {
        echo "<tr>\n";
        foreach ($fields as $f) {
            $col = $f->name;
            echo "<td>".htmlspecialchars($row[$col])."</td>";
        }
        echo "\n</tr>\n";
    }
    echo "</table>\n";
    // ссылка возврата
    echo '<p><a href="z10-1.htm">Возврат к выбору таблицы</a></p>';
}
?>

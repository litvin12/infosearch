<!--
Обработчик z4-3b.php для теста "Города и памятники".
Формат принят из vopr.txt; в скрипте создается массив $otv с номерами
правильных ответов и делается вывод имени тестируемого и оценки
в зависимости от количества правильных ответов (оператор switch).
-->
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <title>z4-3b — Результат теста</title>
</head>
<body>
<?php
    // Массив правильных ответов по ТЗ
    $otv = array(6,9,4,1,3,2,5,8,7);

    $name = isset($_POST['name']) ? trim($_POST['name']) : 'Без имени';
    $answers = array();
    for ($i = 1; $i <= 9; $i++) {
        $key = 'q' . $i;
        $answers[$i] = isset($_POST[$key]) ? intval($_POST[$key]) : 0;
    }

    $correct = 0;
    for ($i = 1; $i <= 9; $i++) {
        if ($answers[$i] == $otv[$i-1]) $correct++;
    }

    echo "<h3>Результат теста для: " . htmlspecialchars($name) . "</h3>\n";
    echo "<p>Правильных ответов: $correct из 9</p>\n";

    switch ($correct) {
        case 9:
            $msg = 'великолепно знаете географию'; break;
        case 8:
            $msg = 'отлично знаете географию'; break;
        case 7:
            $msg = 'очень хорошо знаете географию'; break;
        case 6:
            $msg = 'хорошо знаете географию'; break;
        case 5:
            $msg = 'удовлетворительно знаете географию'; break;
        case 4:
            $msg = 'терпимо знаете географию'; break;
        case 3:
            $msg = 'плохо знаете географию'; break;
        case 2:
            $msg = 'очень плохо знаете географию'; break;
        default:
            $msg = 'вообще не знаете географию'; break;
    }

    echo "<p>Оценка: <strong>$msg</strong></p>\n";
    echo "<p><a href=\"z4-3a.htm\">Назад</a></p>\n";
?>
</body>
</html>

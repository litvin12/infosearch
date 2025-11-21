<!--
В скрипте z4-1b.php сформировать таблицу, состоящую из одной ячейки
шириной и высотой 100 пикселов, атрибуты ячейки align и valign должны
получить значения, переданные из формы. В ячейку таблицы поместить слово "Текст".
Под таблицей вставить гиперссылку на файл z4-1a.htm ("Назад").
-->
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <title>z4-1b — Результат</title>
</head>
<body>
<?php
    // Получаем align
    $align = isset($_POST['align']) ? $_POST['align'] : 'left';
    // Получаем valign — может придти массив (флажки), поэтому поддерживаем оба варианта
    $valign_raw = isset($_POST['valign']) ? $_POST['valign'] : 'top';
    if (is_array($valign_raw)) {
        $valign = $valign_raw[0];
    } else {
        $valign = $valign_raw;
    }
    // Валидация значений — разрешаем только ожидаемые
    $allowed_align = array('left','center','right');
    $allowed_valign = array('top','middle','bottom');
    if (!in_array($align, $allowed_align)) $align = 'left';
    if (!in_array($valign, $allowed_valign)) $valign = 'top';

    $align_safe = htmlspecialchars($align, ENT_QUOTES);
    $valign_safe = htmlspecialchars($valign, ENT_QUOTES);
?>

<table border="1">
    <tr>
        <td width="100" height="100" align="<?= $align_safe ?>" valign="<?= $valign_safe ?>">Текст</td>
    </tr>
</table>

<p><a href="z4-1a.htm">Назад</a></p>
</body>
</html>

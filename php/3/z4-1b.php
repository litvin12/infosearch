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
    // Получаем данные
    $align = $_POST['align'] ?? 'left';
    $valign = $_POST['valign'] ?? 'top';

    // Разрешённые значения
    $allowed_align = ['left', 'center', 'right'];
    $allowed_valign = ['top', 'middle', 'bottom'];

    // Защита
    if (!in_array($align, $allowed_align))
        $align = 'left';
    if (!in_array($valign, $allowed_valign))
        $valign = 'top';

    $align_safe = htmlspecialchars($align, ENT_QUOTES); // вообще тут наверное не надо но для безопасности
    $valign_safe = htmlspecialchars($valign, ENT_QUOTES);
    ?>

    <table border="1">
        <tr>
            <td width="100" height="100" align="<?= $align_safe ?>" valign="<?= $valign_safe ?>">
                <!-- краткая запись < ? php echo $align_safe; ?> -->
                Текст
            </td>
        </tr>
    </table>

    <p><a href="z4-1a.htm">Назад</a></p>

</body>

</html>
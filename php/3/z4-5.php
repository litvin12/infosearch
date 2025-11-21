<!--
На основе листинга 10-9 создайте скрипт z4-5.php в котором сперва проверяется,
было ли присвоено значение переменной $site. Если присвоено — перенаправление
на сайт поисковой системы, адрес которого - значение переменной $site.
Если же значение не задано — выводится HTML-форма с раскрывющимся списком поисковых сайтов,
который формируется на основе массива $list_sites[] с помощью цикла while и функции count().
-->
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <title>z4-5 — Перенаправление на поисковик</title>
</head>
<body>
<?php
    $list_sites = array(
        'https://www.google.com',
        'https://www.bing.com',
        'https://duckduckgo.com'
    );

    // Если значение передано методом POST
    if (isset($_POST['site']) && strlen(trim($_POST['site']))>0) {
        $site = trim($_POST['site']);
        // Небольшая валидация: если не начинается с http, добавляем https://
        if (!preg_match('#^https?://#i', $site)) {
            $site = 'https://' . $site;
        }
        header('Location: ' . $site);
        exit;
    }

    // Иначе показываем форму. Формируем select с помощью while и count()
    echo '<form method="post" action="'> . htmlspecialchars($_SERVER['PHP_SELF']) . "">\n";
    echo "<label>Выберите поисковый сайт: <select name=\"site\">\n";
    $i = 0;
    while ($i < count($list_sites)) {
        $val = htmlspecialchars($list_sites[$i]);
        echo "<option value=\"$val\">$val</option>\n";
        $i++;
    }
    echo "</select></label>\n";
    echo " <button type=\"submit\">Перейти</button>\n";
    echo "</form>\n";
?>
</body>
</html>

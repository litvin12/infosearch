<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <title>z4-5 — Перенаправление на поисковик</title>
</head>
<body>
<?php
// Список поисковых сайтов
$list_sites = array(
    'https://www.google.com',
    'https://www.bing.com',
    'https://duckduckgo.com'
);


// Возможные источники: POST (форма) или GET (query ?site=...)
$site = '';
if (isset($_POST['site']) && strlen(trim($_POST['site'])) > 0) {
    $site = trim($_POST['site']); // из формы
} elseif (isset($_GET['site']) && strlen(trim($_GET['site'])) > 0) {
    $site = trim($_GET['site']); // из URL
}

// Если значение сайта есть, выполняем редирект
if ($site !== '') {
    // небольшая валидация, пользователь ввёл сайт без http/https, добавляем https://
    if (!preg_match('#^https?://#i', $site)) {
        $site = 'https://' . $site;
    }

    header('Location: ' . $site); // вроде не очень безопасно использовать можно аналог посмотреть
    exit; 
}

// Если POST или GET не пришли — показываем форму выбора сайта
echo '<form method="post" action="' . htmlspecialchars($_SERVER['PHP_SELF']) . "\">\n";
echo "<label>Выберите поисковый сайт: <select name=\"site\">\n";

$i = 0;
while ($i < count($list_sites)) {
    $val = htmlspecialchars($list_sites[$i]); // безопасный вывод
    echo "<option value=\"$val\">$val</option>\n";
    $i++;
}

echo "</select></label>\n";
echo " <button type=\"submit\">Перейти</button>\n";
echo "</form>\n";
?>
</body>
</html>

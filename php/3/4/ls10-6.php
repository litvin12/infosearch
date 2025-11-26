<html>
<head>
    <title>Task 3.4.5 — Результат (способ 2)</title>
</head>
<body>
    <?php
        $user = $_POST["user"];
        print "<h2>Привет, $user!</h2>\n";
        print "<p>Все данные из формы:</p>\n";
        print "<ul>\n";
        // СПОСОБ 2: перебор с проверкой
        foreach ($_POST as $key => $value) {
            // Функция gettype() возвращает тип переменной
            if (gettype($value) == "array") {
                // Если значение — это массив (как hobby[])
                print "<li><strong>$key</strong> (массив):<br>\n"; // strong -- жирный + для индексации вроде полезно
                foreach ($value as $v) {
                    print "  &nbsp;&nbsp;- $v<br>\n";
                }
                print "</li>\n";
            } else {
                print "<li><strong>$key</strong>: $value</li>\n";
            }
        }
        print "</ul>\n";
        
        print "<p><a href='z4-46.php'>← Назад к форме</a></p>\n";
    ?>
</body>
</html>
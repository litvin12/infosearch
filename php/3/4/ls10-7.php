<html>
<head>
    <title>Task 3.4.5 — Результат (способ 3)</title>
</head>
<body>
    <?php
        // данные из $_POST, если они есть, иначе из $_GET
        $PARAMS = (isset($_POST)) ? $_POST : $_GET;
        $user = $PARAMS["user"];
        
        print "<h2>Привет, $user!</h2>\n";
        print "<p>Все данные из формы/URL:</p>\n";
        print "<ul>\n";
        
        // СПОСОБ 3: Универсальный перебор с проверкой типа
        foreach ($PARAMS as $key => $value) {
            if (gettype($value) == "array") {
                print "<li><strong>$key</strong> (массив):<br>\n";
                foreach ($value as $v) {
                    print "  &nbsp;&nbsp;- $v<br>\n"; // &nbsp; -- неразрывный пробел
                }
                print "</li>\n";
            } else {
                print "<li><strong>$key</strong>: $value</li>\n";
            }
        }
        print "</ul>\n";
        
        print "<p><a href='z4-47.php'>← Назад к форме</a></p>\n";
    ?>
</body>
</html>
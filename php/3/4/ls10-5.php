<html>
<head>
    <title>Task 3.4.5 — Результат (способ 1)</title>
</head>
<body>
    <?php
        $user = $_POST["user"];
        print "<h2>Привет, $user!</h2>\n";
        print "<p>Вы выбрали следующие хобби:</p>\n";
        print "<ul>\n";
        // СПОСОБ 1: прямое обращение к массиву
        foreach ($_POST['hobby'] as $key => $value) {
            print "<li>$key = $value</li>\n";
        }
        print "</ul>\n";
        
        print "<p><a href='z4-45.php'>← Назад к форме</a></p>\n";
    ?>
</body>
</html>
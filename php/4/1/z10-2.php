<html>
<head>
    <title>Task 4.1 — Просмотр таблиц БД</title>
</head>
<body>

    <?php
        // Получаем параметры из формы
        $PARAMS = (!empty($_POST)) ? $_POST : $_GET;
        $structure = (!empty($PARAMS["structure"])) ? $PARAMS["structure"] : array();
        $content = (!empty($PARAMS["content"])) ? $PARAMS["content"] : array();

        include("z10-4.inc");
        
        if (!isset($conn) || !$conn) {
            echo "<p style='color: red;'><strong>Ошибка:</strong> Не удалось подключиться к БД</p>";
            exit;
        }

        include("z10-3.inc");
        include("z10-5.inc");
        include("z10-6.inc");
    ?>
    
</body>
</html>
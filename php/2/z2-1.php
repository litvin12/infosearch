<!-- Используя переменные $color и $size сформировать php-скрипт z2-1.php, который выводит на экран строку текста заданным цветом и размером.

(Использовать листинг 1-2). -->

<html>
<head>
    <title> Task 2.1 </title>
</head> 
<body>
    <?php
        $color = $_GET['color'];
        $size = $_GET['size'];
        print "<p><font color=\"$color\" size=\"$size\">PHP works!!</font>";
    ?>
</body> 
</html>
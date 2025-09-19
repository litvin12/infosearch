<!-- Пусть в скрипте z2-5.php переменная $lang может принимать значения "ru", "en", "fr" или "de". Используя операторы if-else-elseif обеспечьте вывод на экран полного названия языка (русский, английский, …) в зависимости от того, что задано в строке вызова скрипта:
z05-5.php?lang=ru [en/fr/de]
Обязательно предусмотреть случай неверного задания значения параметра lang - тогда должна выводиться надпись "язык неизвестен".

(Использовать листинг 6-2). -->

<html> <head>
<title> Task 2.2 </title> </head> <body> 

<?php 
    $lang = $_GET['lang'];

    switch($lang){
        case "ru": 
            print "russian"; 
            break;
        case "en": 
            print "english";
            break;
        case "Fr": 
            print "french";
            break;
        case "De": 
            print "dutch";
            break;
        default: 
            print "unknown language";
            break;
    }
?>
</body> </html>
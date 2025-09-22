<!-- В скрипте z3-3.php создайте 4 функции с именами Ru(), En(), Fr(), De(). Каждая функция выводит на экран приветствие
 на соответствующем языке:
Ru() - "Здравствуйте!",
En() - "Hello!",
Fr() - "Bonjour!" и
De() - "Guten Tag!".

Эти функции имеют аргумент $color, который определяет цвет выводимого текста. Используя функцию-переменную $lang(), отобразить
на экране одно из приветствий, причем какое приветствие будет выведено и каким цветом - задать как параметры в строке вызова скрипта:

z3-3.php?lang=Ru&color=[назв-е цвета]
               En/Fr/De

(Использовать листинг 8-3). -->


<html> <head>
<title> Task 2.5 </title>
</head> <body>

<?php
    function Ru($color) { print "<p><font color=\"$color\">Здравствуйте!</font>"; }
    function En($color) { print "<p><font color=\"$color\">Hello!</font>"; }
    function Fr($color) { print "<p><font color=\"$color\">Bonjour!</font>"; }
    function De($color) { print "<p><font color=\"$color\">Gutten Tag!</font>"; }

    $lang = $_GET["lang"];
    $color = $_GET["color"];
    switch($lang){
        case "ru": 
            Ru($color);
            break;
        case "en": 
            En($color);
            break;
        case "fr": 
            Fr($color);
            break;
        case "de":
            De($color);
            break;
        default:
            print "unknown language";
            break;
    }
?>
</body> </html>
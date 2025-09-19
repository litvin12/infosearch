<!-- Используя вложенные циклы for в скрипте z3-2.php отобразите на экране таблицу сложения чисел от 1 до 10.
 При этом цвет цифр в верхней строке и левом столбце должен быть задан через $color вне циклов, а в левой верхней ячейке
 должен стоять знак "+" красного цвета. Ширина рамки таблицы равна 1, отступ содержимого ячеек от границы равен 5.

+	2	3	...	10
2	4	5	...	12
3	5	6	...	13
...	...	...	...	...
10	12	13	...	20

(Использовать листинг 7-6). -->

<html> <head>
<title> Task 2.4 </title>
</head> 
<body>
    <?php
        print "<table border=1 cellpadding=5>\n";
        $color = 'blue';
        $base_color = "white";
        $plus_color = "red";
        for ($y=1;  $y <= 10;  $y++) {
            print "<tr>\n";
                for ($x=1;  $x <= 10;  $x++) {
                    print "\t<td>";
                    if($x==1 && $y==1) {
                        print "<p><font color=\"$color\">+</font>";
                    } elseif($x==1) {
                        print "<p><font color=\"$color\">$y</font>";
                    } elseif($y==1) {
                        print "<p><font color=\"$color\">$x</font>";
                    } else {
                        print ($x+$y);
                    }
                    print "</td>\n";
                }
                print "</tr>\n";
            }
        print "</table>";
    ?>
</body> </html>
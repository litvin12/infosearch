<!-- В скрипте z3-5.php

Создайте массив $treug[] "треугольных" чисел, т.е. чисел вида n(n+1)/2 (где n=1,2,: 10) и выведите значения этого массива на экран в строку (через 2 пробела).

Создайте массив $kvd[] квадратов натуральных чисел от 1 до 10, выведите значения этого массива на экран в строку.

Объедините эти 2 массива в массив $rez[], выведите результат на экран.

Отсортируйте массив $rez[], выведите результат на экран.

Удалите в массиве $rez[] первый элемент, выведите результат на экран.

С помощью функции array_unique() удалите из массива $rez[] повторяющиеся элементы, результат занесите в массив $rez1[] и выведите его на экран.

(Использовать листинги 9-2 - 9-10). -->

<html> <head>
<title> Task 2.6 </title>
</head> 
<body>

    <?php
        function print_array($arr) {
            foreach ($arr as $a)
                print $a."&nbsp&nbsp";
            print "<hr/>";
        }

        for ($n=1; $n<=10; $n++){
            $treug[$n-1] = $n*($n+1)/2;
        }
        print "treug: ";
        print_array($treug);

        for ($n=1; $n<=10; $n++){
            $kvd[$n-1] = $n*$n;
        }
        print "kvd: ";
        print_array($kvd);

        $res = array_merge($treug, $kvd);
        print "res - treug and kvd merge: ";
        print_array($res);

        sort($res);
        print "sorted res: ";
        print_array($res);

        array_shift($res);
        print "res without first element: ";
        print_array($res);

        $res1=array_unique($res);
        print "res1 - unique res: ";
        print_array($res1);
    ?>
</body> </html>


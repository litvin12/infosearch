<!-- В скрипте z3-6.php

1. Создайте ассоциативный массив $cust[]
с ключами cnum, cname, city, snum и rating
и значениями: 2001, Hoffman, London, 1001 и 100.

Выведите этот массив (вместе с именами ключей) на экран.

2. Отсортируйте этот массив по значениям. Выведите результат на экран.

3. Отсортируйте этот массив по ключам. Выведите результат на экран.

4. Выполните сортировку массива с помощью функции sort(). Выведите результат на экран.

(Использовать листинги 9-1 - 9-10). -->

<html> <head>
<title> Task 2.7 </title>
</head> 
<body>

    <?php
        function print_array($arr) {
            foreach ($arr as $key=>$value) {
                print "$key: $value; ";
            }
            print "<hr/>";
        }

        $cust = array (
            'cnum' => 2001,
            'cname' => "Hoffman",
            'city' => "London",
            'snum' => 1001,
            'rating' => 100
        );
        print_array($cust);
        asort($cust);
        print_array($cust);
        ksort($cust);
        print_array($cust);
        sort($cust);
        print_array($cust);
    ?>
</body> </html>


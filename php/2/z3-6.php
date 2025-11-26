<!-- В скрипте z3-6.php

1. Создайте ассоциативный массив $cust[]
с ключами cnum, cname, city, snum и rating
и значениями: 2001, Hoffman, London, 1001 и 100.

Выведите этот массив (вместе с именами ключей) на экран.

2. Отсортируйте этот массив по значениям. Выведите результат на экран.

3. Отсортируйте этот массив по ключам. Выведите результат на экран.

4. Выполните сортировку массива с помощью функции sort(). Выведите результат на экран.

(Использовать листинги 9-1 - 9-10). -->

<html>

<head>
    <title>Ассоциативный массив - сортировка</title>
</head>

<body>
    <?php
    // 1. Создание массива ключ => значение
    $cust = [
        "cnum" => 2001,
        "cname" => "Hoffman",
        "city" => "London",
        "snum" => 1001,
        "rating" => 100
    ];

    // Вывод исходного массива
    echo "<b>Исходный массив:</b><br>";
    foreach ($cust as $key => $value) {
        echo "$key => $value<br>";
    }
    echo "<br>";

    // 2. Сортировка по значениям (asort)
    $byValues = $cust; // копия
    asort($byValues);

    echo "<b>Сортировка по значениям (asort):</b><br>";
    foreach ($byValues as $key => $value) {
        echo "$key => $value<br>";
    }
    echo "<br>";

    // 3. Сортировка по ключам (ksort)
    $byKeys = $cust; // копия
    ksort($byKeys);

    echo "<b>Сортировка по ключам (ksort):</b><br>";
    foreach ($byKeys as $key => $value) {
        echo "$key => $value<br>";
    }
    echo "<br>";

    // 4. Сортировка через sort() (ключи сбросятся, потому что массив пересоздается, ключи удаляются и все сортируется)
    $sorted = $cust; // копия
    sort($sorted);

    echo "<b>Сортировка через sort() (ключи теряются):</b><br>";
    foreach ($sorted as $key => $value) {
        echo "$key => $value<br>";
    }
    ?>
</body>

</html>
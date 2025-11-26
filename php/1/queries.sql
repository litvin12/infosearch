-- Напишите запрос, который выводит все строки из таблицы Покупателей, для которых номер продавца равен 1001.
SELECT * FROM cust WHERE snum = 1001;

-- Напишите запрос, который выводит таблицу Продавцов со столбцами в следующем порядке: city, sname, snum, comm.
SELECT city, sname, snum, comm FROM sal;

-- Напишите запрос, который выводит оценку (rating), сопровождаемую именем каждого покупателя в городе San Jose.
SELECT rating, cname FROM cust WHERE city = 'San Jose';

-- Напишите запрос, который выводит значение номера продавца всех продавцов из таблицы Заказов без каких бы то ни было повторений.
SELECT DISTINCT snum FROM ord;

-- Напишите запрос, который может выдать вам поля sname и city для всех продавцов в Лондоне с комиссионными строго больше 0.11
SELECT sname, city FROM sal WHERE city = 'London' AND comm > 0.11;

-- Напишите запрос к таблице Покупателей, который может вывести данные обо всех покупателях с рейтингом меньше или равным 200, если они не находятся в Риме
SELECT * FROM cust WHERE rating <= 200 AND city != 'Rome';

-- Запросите двумя способами все заказы на 3 и 5 октября 1990 г.
SELECT * FROM ord WHERE odate IN ('1990-10-03', '1990-10-05');

-- Напишите запрос, который может вывести всех покупателей, чьи имена начинаются с буквы, попадающей в диапазон от A до G.
SELECT * FROM cust WHERE cname REGEXP '^[A-G]';

-- Напишите запрос, который выберет всех продавцов, имена которых содержат букву e.
SELECT * FROM sal WHERE sname LIKE '%e%';

-- Напишите запрос, который сосчитал бы сумму всех заказов на 3 октября 1990 г.
SELECT SUM(amt) AS total_amount FROM ord WHERE odate = '1990-10-03';

-- Напишите запрос, который сосчитал бы сумму всех заказов для продавца с номером 1001
SELECT SUM(amt) AS total_amount FROM ord WHERE snum = 1001;

-- Напишите запрос, который выбрал бы наибольший заказ для каждого продавца.
SELECT snum, MAX(amt) AS max_order FROM ord GROUP BY snum;

-- Напишите запрос, который выбрал бы покупателя, чье имя является первым в алфавитном порядке среди имен, заканчивающихся на букву s.
SELECT * FROM cust WHERE cname LIKE '%s' ORDER BY cname LIMIT 1;

-- Напишите запрос, который выбрал бы средние комиссионные в каждом городе.
SELECT city, AVG(comm) AS avg_commission FROM sal GROUP BY city;

-- Напишите запрос, который вывел бы для каждого заказа на 3 октября его номер, стоимость заказа в евро (1$=0.8 евро), имя продавца и размер комиссионных, полученных продавцом за этот заказ.
SELECT 
    o.onum, 
    o.amt * 0.8 AS amt_euro, 
    s.sname, 
    o.amt * s.comm AS commission
FROM ord o
JOIN sal s ON o.snum = s.snum
WHERE o.odate = '1990-10-03';

-- Напишите запрос, который выводит номера заказов в возрастающем порядке, а также имена продавцов и покупателей заказов, продавец которых находится в Лондоне или Риме.
SELECT 
    o.onum, 
    s.sname, 
    c.cname
FROM ord o
JOIN sal s ON o.snum = s.snum
JOIN cust c ON o.cnum = c.cnum
WHERE s.city IN ('London', 'Rome')
ORDER BY o.onum ASC;

-- Запросите имена продавцов в алфавитном порядке, суммарные значения их заказов, совершенных до 5 октября, и полученные комиссионные.
SELECT 
    s.sname,
    SUM(o.amt) AS total_orders,
    SUM(o.amt * s.comm) AS total_commission
FROM sal s
JOIN ord o ON s.snum = o.snum
WHERE o.odate < '1990-10-05'
GROUP BY s.sname
ORDER BY s.sname;

-- Выведите номера заказов, их стоимость и имена продавцов и покупателей, если продавцы и покупатели находятся в городах, чьи названия начинаются с букв из диапазона от L до R.
SELECT 
    o.onum,
    o.amt,
    s.sname,
    c.cname
FROM ord o
JOIN sal s ON o.snum = s.snum
JOIN cust c ON o.cnum = c.cnum
WHERE s.city REGEXP '^[L-R]' AND c.city REGEXP '^[L-R]';

-- Запросите все пары покупателей, обслуживаемые одним и тем же продавцом. Исключите комбинации покупателей с самими собой, а также пары в обратном порядке.
SELECT 
    c1.cname AS customer1,
    c2.cname AS customer2,
    c1.snum AS seller
FROM cust c1
JOIN cust c2 ON c1.snum = c2.snum
WHERE c1.cnum < c2.cnum;

-- С помощью подзапроса выведите имена всех покупателей, чьи продавцы имеют комиссионные меньше 0.13.
SELECT cname 
FROM cust 
WHERE snum IN (SELECT snum FROM sal WHERE comm < 0.13);

-- Напишите команду, создающую копию таблицы Продавцов с одновременным копированием данных из SAMPLE.SAL. Убедитесь в сходности структур таблиц при помощи команды DESC и идентичности данных в таблице-оригинале и таблице-копии.
CREATE TABLE sal_copy AS SELECT * FROM sal;
DESC sal;
DESC sal_copy;
SELECT * FROM sal;
SELECT * FROM sal_copy;

-- Напишите последовательность команд, которая вставляет две новые записи в вашу таблицу Продавцов, выводит таблицу после вставки, удаляет одну запись о новом продавце и вновь выводит таблицу.
INSERT INTO sal (snum, sname, city, comm) VALUES 
(1010, 'Smith', 'Paris', 0.14),
(1011, 'Brown', 'Berlin', 0.12);
SELECT * FROM sal;
DELETE FROM sal WHERE snum = 1010;
SELECT * FROM sal;

-- Напишите последовательность команд, которая вставляет две строки в вашу таблицу Продавцов, увеличивает в 2 раза комиссионные у всех продавцов и выводит содержимое таблицы после каждого изменения.
INSERT INTO sal (snum, sname, city, comm) VALUES 
(1012, 'Wilson', 'Madrid', 0.09),
(1013, 'Taylor', 'Milan', 0.11);
SELECT * FROM sal;
UPDATE sal SET comm = comm * 2;
SELECT * FROM sal;
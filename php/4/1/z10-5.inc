<?php
        $rus_name = array(
            'cnum' => 'Номер покупателя', 
            'cname' => 'Имя покупателя', 
            'city' => 'Город', 
            'rating' => 'Оценка', 
            'snum' => 'Номер продавца',
			'snum' => 'Номер продавца', 
            'sname' => 'Имя продавца', 
            'city' => 'Город', 
            'comm' => 'Комиссия',
			'onum' => 'Номер заказа', 
            'amt' => 'Стоимость', 
            'odate' => 'Дата', 
            'cnum' => 'Number customer', 
            'snum' => 'Номер продавца'
        );

        function vid_structure($conn, $table) {
            if (!$conn) {
                echo "<p style='color: red;'>⚠️ Соединение с БД не установлено</p>";
                return;
            }
            
            $safe_table = mysqli_real_escape_string($conn, $table);
            $res = mysqli_query($conn, "DESCRIBE `" . $safe_table . "`");
            
            echo "<h3>Структура таблицы «" . htmlspecialchars($table) . "»</h3>\n";
            
            if (!$res) {
                echo "<p style='color: red;'>❌ Ошибка: " . htmlspecialchars(mysqli_error($conn)) . "</p>\n";
                return;
            }
            
            echo "<table border='1'>\n";
            echo "<tr><th>Field</th><th>Type</th><th>Null</th><th>Key</th><th>Default</th><th>Extra</th></tr>\n";
            
            while ($row = mysqli_fetch_assoc($res)) {
                echo "<tr>";
                echo "<td>" . htmlspecialchars($row['Field']) . "</td>";
                echo "<td>" . htmlspecialchars($row['Type']) . "</td>";
                echo "<td>" . htmlspecialchars($row['Null']) . "</td>";
                echo "<td>" . htmlspecialchars($row['Key']) . "</td>";
                echo "<td>" . htmlspecialchars($row['Default']) . "</td>";
                echo "<td>" . htmlspecialchars($row['Extra']) . "</td>";
                echo "</tr>\n";
            }
            echo "</table>\n";
        }

        function vid_content($conn, $table) {
            if (!$conn) {
                echo "<p style='color: red;'>⚠️ Соединение с БД не установлено</p>";
                return;
            }
            
            $safe_table = mysqli_real_escape_string($conn, $table); <!-- защита от инъекций, prepare нельзя использовать т.к. имена таблиц, колонок и тп параметризовать не умеет -->
            $res = mysqli_query($conn, "SELECT * FROM `" . $safe_table . "` LIMIT 1000");
            
            echo "<h3>Содержимое таблицы «" . htmlspecialchars($table) . "»</h3>\n";
            
            if (!$res) {
                echo "<p style='color: red;'>❌ Ошибка: " . htmlspecialchars(mysqli_error($conn)) . "</p>\n";
                return;
            }
            
            $fields = mysqli_fetch_fields($res);
            echo "<table border='1'>\n<tr>\n";
            
            foreach ($fields as $f) {
                echo "<th>" . htmlspecialchars($f->name) . "</th>";
            }
            echo "</tr>\n";
            
            while ($row = mysqli_fetch_assoc($res)) {
                echo "<tr>\n";
                foreach ($fields as $f) {
                    echo "<td>" . htmlspecialchars($row[$f->name]) . "</td>";
                }
                echo "</tr>\n";
            }
            echo "</table>\n";
            echo '<p><a href="z10-1.htm">← Назад к выбору таблицы</a></p>';
        }
        foreach ($structure as $table){
	        vid_structure($conn, $table);
        }
	    foreach ($content as $table){
		    vid_content($conn, $table);
        }
        print "<p>";
        print "<a href=\"z10-1.htm\">Back to choose tables</a>";
?>
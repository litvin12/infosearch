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
            $result = mysqli_query($conn, "DESC $table");
            $num_rows = mysqli_num_rows($result);
            $num_fields = mysqli_num_fields($result);

            print "<h4>Content of table $table</h4>\n";
            print "<table border=1 cellpadding=5>\n";
            print "<tr>";
            for ($x = 0; $x < $num_fields; $x++) {
                $name = mysqli_fetch_field_direct($result, $x)->name;
                print "\t<th><i>$name</i></th>";
            }
            print "</tr>\n";

            while ($a_row = mysqli_fetch_row($result)) {
                print "<tr>";
                foreach ($a_row as $field)
                    print "\t<td><i>$field</i></td>";
                print "</tr>\n";
            }
            print "</table>\n";
        }

        function vid_content($conn, $table) {
            $result = mysqli_query($conn, "SELECT * FROM $table");
            $num_rows = mysqli_num_rows($result);
            $num_fields = mysqli_num_fields($result);
            $info = mysqli_query($conn, "DESC $table");
            
            print "<h4>Content of table $table</h4>\n";
            print "<table border=1 cellpadding=5>\n";
            print "<tr>";
            for ($x = 0; $x < $num_fields; $x++) {
                $name = mysqli_fetch_field_direct($result, $x)->name;
                $transl = $rus_name[$name];
                print "\t<th>$transl<br>$name</br></th>";
            }
            print "</tr>\n";

            while ($a_row = mysqli_fetch_row($result)) {
                print "<tr>";
                foreach ($a_row as $field)
                    print "\t<td>$field</td>";
                print "</tr>\n";
            }
            print "</table>\n";
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
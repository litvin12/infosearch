<?php
// z10-6.inc: отключение от базы
if (isset($mysqli) && $mysqli instanceof mysqli) {
    $mysqli->close();
}
?>

<?php
// z10-6.inc: отключение от базы

if (isset($conn) && is_resource($conn)) {
    mysqli_close($conn);
    // echo "✅ Соединение закрыто успешно\n";
}
?>
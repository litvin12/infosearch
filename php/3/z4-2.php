<!--
На основе предыдущего задания создайте файл z4-2.php с HTML-формой, которая вызывает сама себя.
По умолчанию установите такие значения: для align - "left", для valign - "top".
-->
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <title>z4-2 — Самозаполняющаяся форма</title>
</head>
<body>
<?php
    $align = 'left';
    $valign = 'top';
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $align = isset($_POST['align']) ? $_POST['align'] : $align;
        $valign_raw = isset($_POST['valign']) ? $_POST['valign'] : $valign;
        if (is_array($valign_raw)) {
            $valign = $valign_raw[0];
        } else {
            $valign = $valign_raw;
        }
    }
    $allowed_align = array('left','center','right');
    $allowed_valign = array('top','middle','bottom');
    if (!in_array($align, $allowed_align)) $align = 'left';
    if (!in_array($valign, $allowed_valign)) $valign = 'top';
?>

    <form method="post" action="<?= htmlspecialchars($_SERVER['PHP_SELF']) ?>">
        <fieldset>
            <legend>Горизонтальное (align)</legend>
            <label><input type="radio" name="align" value="left" <?= $align=='left'? 'checked':'' ?>> left</label>
            <label><input type="radio" name="align" value="center" <?= $align=='center'? 'checked':'' ?>> center</label>
            <label><input type="radio" name="align" value="right" <?= $align=='right'? 'checked':'' ?>> right</label>
        </fieldset>
        <br>
        <fieldset>
            <legend>Вертикальное (valign)</legend>
            <label><input type="checkbox" name="valign[]" value="top" <?= $valign=='top'? 'checked':'' ?>> top</label>
            <label><input type="checkbox" name="valign[]" value="middle" <?= $valign=='middle'? 'checked':'' ?>> middle</label>
            <label><input type="checkbox" name="valign[]" value="bottom" <?= $valign=='bottom'? 'checked':'' ?>> bottom</label>
        </fieldset>
        <br>
        <button type="submit">Выполнить</button>
    </form>

<?php if ($_SERVER['REQUEST_METHOD'] === 'POST'): ?>
    <h4>Результат</h4>
    <table border="1">
        <tr>
            <td width="100" height="100" align="<?= htmlspecialchars($align) ?>" valign="<?= htmlspecialchars($valign) ?>">Текст</td>
        </tr>
    </table>
<?php endif; ?>

</body>
</html>

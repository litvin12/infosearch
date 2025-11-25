<html> <head>
<title> Task 4.1 </title>
</head>
<body>

    <?php            
        $PARAMS = (!empty($_POST))? $_POST : $_GET;
        $structure = (!empty($PARAMS["structure"]))? $PARAMS["structure"] : array();
        $content = (!empty($PARAMS["content"]))? $PARAMS["content"] : array();

        include("z10-3.inc");
        $conn = include("z10-4.inc");
        include("z10-5.inc");
        include("z10-6.inc");
    ?>
    
</body>
</html>
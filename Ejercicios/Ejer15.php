<?php

$text = 'w3resource';

$char = 'r';

$count = 0;

for ($i = '0'; $i < strlen($text); $i++) { 
    if (substr($text, $i, 1) == $char) {
        $count+=1;
    }
}

echo $count;

?>
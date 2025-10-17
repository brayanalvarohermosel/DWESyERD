<?php

$numbers = [];
for ($i = 0; $i < 50; $i++) {
    $numbers[] = rand(0, 99);
}

foreach ($numbers as $number) {
    echo $number . ' ';
}

?>
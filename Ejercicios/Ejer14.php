<?php

$numbers = [12, 45, 23, 67, 34, 89, 90, 11, 5, 78];

foreach ($numbers as $i => $number) {
    echo max($numbers[$i], $number) . ' ';
}

?>
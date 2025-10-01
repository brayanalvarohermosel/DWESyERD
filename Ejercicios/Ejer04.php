<?php

    $n = 30;
    $diference;

    if ($n == 51) {
        $diference = 0;
    }else if ($n > 51) {
        $diference = ($n - 51) * 3;
    }else{
        $diference = 51 - $n;
    }

    echo('La diferencia es: ' . $diference)

?>
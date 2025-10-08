<?php

function factorial($number){
    $total = 1;

    if ($number == 0) {
        return 1;
    }
    
    for ($i=$number; $i >= 1; $i--) { 
        $total *= $i;
    }
    
    return 'El factorial de ' . $number . ' es ' . $total;
}

echo factorial(5);

?>
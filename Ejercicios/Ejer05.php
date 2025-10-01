<?php
    $number = 4;
    $total = 1;

    for ($i=$number; $i >= 1; $i--) { 
         $total *= $i;
    }
    
    echo('El factorial de ' . $number . ' es: ' . $total);
?>
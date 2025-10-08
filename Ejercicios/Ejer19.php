<?php 

function primNumbers($number){

    for ($i=2; $i < $number; $i++) { 
        if ($number % $i == 0) {
            return 0;
        }

    }
    return 1;
}

if (primNumbers(6) == 0) {
    echo 'No es Primo';
}else {
    echo 'Es Primo';
}

?>
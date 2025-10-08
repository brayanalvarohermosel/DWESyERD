<?php

$numbers = array(5, 3, 8, 1, 2);

function arraySorting($a){
    
    for($i = 0; $i < count($a); $i++){
        $aux = $i;
        for($j = $i +1 ; $j < count($a); $j++){
            if($a[$j] < $a[$aux]){
                $temp = $a[$aux];
                $a[$aux] = $a[$j];
                $a[$j] = $temp;
            }
        }
    }
    return $a;
}


print_r(arraySorting($numbers));
?>
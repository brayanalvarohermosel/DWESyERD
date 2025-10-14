<?php

for ($i=1; $i <= 10; $i++) { 
    for ($j=1; $j <=10 ; $j++) { 
        $total[$i][$j] = $i * $j;
        echo "$i x $j = " . $total[$i][$j] . "\n";
    }
}

?>
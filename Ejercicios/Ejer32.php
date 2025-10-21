<?php

$total = 0;

for ($i = 1; $i <= 10; $i++) {
    $total += $i;
}

echo 'Resultado de la suma de los numeros entre el 1 y el 10: ' . $total;

//Usando inicio y final

$ini = 1;
$fin = 10;
$total = 0;

for ($i = $ini; $i <= $fin; $i++) {
    $total += $i;
}

echo "\nResultado de la suma de los numeros entre el 1 y el 10: " . $total;

?>
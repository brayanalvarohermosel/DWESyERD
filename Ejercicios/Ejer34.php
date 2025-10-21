<?php

$base = 5;
$exp = 2;
$resultado = 1;

for ($i = 0; $i < $exp; $i++) {
    $resultado *= $base;
}

echo $base . ' ^ ' . $exp . ' = ' . $resultado;

//Ejercicio anterior con Do while

$base = 5;
$exp = 3;
$resultado = 1;
$i = 0;

do {
    $resultado *= $base;
    $i++;
} while ($i < $exp);

echo "\n". $base . ' ^ ' . $exp . ' = ' . $resultado;

?>
<?php

// Funcion que averigua si un numero es par o impar
function esPar($num)
{
    if ($num % 2 == 0) {
        return true;
    }
}

/*
funcion que genera un array con X tamaño($tam) de numeros aleatorios 
entre un minimo($min) y un maximo($max)
*/
function arrayAletorio(int $tam, int $min, int $max)
{
    $array= [];
    for ($i = $min; $i < $tam; $i++) {
        $array[] = rand($min, $max);
    }
    foreach ($array as $num) {
        echo $num . ' ';
    }
}

function arrayPares(array $array)
{
    $numPares = 0;
    foreach ($array as $num) {
        if (esPar($num)) {
            $numPares++;
        }
        
        
    }
    return $numPares;
}

$arrayRandom[] = arrayAletorio(50, 0, 100);
foreach ($arrayRandom as $num) {
    echo $num . ' ';
}

echo "\nNumeros pares en el array: " . arrayPares($arrayRandom);

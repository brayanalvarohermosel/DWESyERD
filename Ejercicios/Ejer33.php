<?php

function digits(int $num): int {
    $num = count(str_split((string)abs($num)));
    return $num;
}

echo 'El numero 55 esta compuesto por: ' . digits(55) . ' digitos.';

?>
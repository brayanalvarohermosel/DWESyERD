<?php

function digitos(int $num) : int {
    return strlen((string)abs($num));
}

function digitoN(int $num, int $pos): int {
    $numStr = (string)abs($num);
    return (int)$numStr[$pos - 1];
}

function quitaPorDetras(int $num, int $cant) : int {
    $numStr = (string)abs($num);
    if ($cant >= strlen($numStr)) {
        return 0;
    }
    $result = substr($numStr, 0, -$cant);
    return (int)$result;
}

function quitarPorDelante(int $num, int $cant) : int {
    $numStr = (string)abs($num);
    if ($cant >= strlen($numStr)) {
        return 0;
    }
    $result = substr($numStr, $cant);
    return (int)$result;
}

?>
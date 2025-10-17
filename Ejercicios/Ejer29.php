<?php
function mayor(): int
{
    $args = func_get_args();
    if (empty($args)) {
        return 0;
    }
    $mayor = $args[0];
    foreach ($args as $num) {
        if ($num > $mayor) {
            $mayor = $num;
        }
    }
    return $mayor;
}

function concatenar(...$palabras): string
{
    return implode(' ', $palabras);
}

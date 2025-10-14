<?php

function mostrarPares($inicio, $fin) {
    
    for ($i = $inicio; $i <= $fin; $i++) {
        if ($i % 2 == 0) {
            echo $i;
        }
    }
    
}

mostrarPares(0, 50);
?>
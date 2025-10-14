<?php
for ($col = 1; $col <= 8; $col++) {

    $total = $row + $col;

    if ($total % 2 == 0) {

        echo "blanco";
    } else {

        echo "negro";
    }
}

?>

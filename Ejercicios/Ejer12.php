<?php

$names = array("Sophia"=>"31","Jacob"=>"41","William"=>"39","Ramesh"=>"40");
asort($names);

foreach ($names as $y=> $y_value) {
    echo 'Nombre: ' .$y .', edad: ' . $y_value .' ';
}

?>
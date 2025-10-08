<?php

function stringReversal ($sentence){
    $newSentence = strlen($sentence);
    if ($newSentence == 1) {
        return 1;
    }else{
        $newSentence--;
        return stringReversal(substr($sentence, 1, $newSentence)) . substr($sentence, 0, 1);
    }
}

echo stringReversal("4321");

?>
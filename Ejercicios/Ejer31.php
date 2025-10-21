<?php

$answers = ['Si', 'no', 'quizás', 'claro que sí', 'por supuesto que no', 'no lo tengo claro', 'seguro', 'yo diría que sí', 'ni de coña'];

    $question = 'habra lluvia esta noche?';
    $answer = $answers[array_rand($answers)];
    echo 'pregunta: '.$question;
    echo '; Respuesta: '. $answer;
?>
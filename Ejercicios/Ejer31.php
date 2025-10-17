<?php

$answers = ['Si', 'no', 'quizás', 'claro que sí', 'por supuesto que no', 'no lo tengo claro', 'seguro', 'yo diría que sí', 'ni de coña'];

if (isset($_GET['pregunta'])) {
    $question = ($_GET['pregunta']);
    $answer = $answers[array_rand($answers)];
    echo 'pregunta: '.$question;
    echo 'Respuesta: '. $answer;
}

?>
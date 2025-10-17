<?php
$json = '{
"Title": "The Cuckoos Calling",
"Author": "Robert Galbraith",
"Detail": {
    "Publisher" : "Little Brown"
    }
}';

$data = json_decode($json, true);

echo 'Titulo: ' . $data['Title'] . "\n";
echo 'Autor: ' . $data['Author'] . "\n";
echo 'Editorial: ' . $data['Detail']['Publisher'];


?>
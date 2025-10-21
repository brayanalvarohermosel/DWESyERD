<?php

class car{
    // Atributos
    public $brand;
    public $model;
    public $year;
    public $actualSpeed;

    // Setters y Getters
    function set_brand($brand){ $this->brand = $brand;}
    function set_model($model){$this->model = $model;}
    function set_year($year){$this->year = $year;}
    function set_actualSpeed($actualSpeed){$this->actualSpeed = $actualSpeed;}

    function get_brand(){ return $this->brand;}
    function get_model(){return $this->model;}
    function get_year(){return $this->year;}
    function get_actualSpeed(){return $this->actualSpeed;}

    /*
    Funciones;
    - Accelerate(Función que suma el valor dado al atributo 'actualSpeed')
    - Break(Función que resta el valor dado al atributo 'actualSpeed')
    - Details(Función que devuelve toda la información del coche)
    */
    function accelerate($incrementSpeed) { 
        $this-> actualSpeed += $incrementSpeed;
    }
    
    function break($decresseSpeed){
        $this-> actualSpeed -= $decresseSpeed;
    }

    function details(){
        return 'Marca: ' . $this -> brand.
        ', Modelo: ' . $this -> model.
        ', Año: ' . $this -> year.
        ', Velocidad actual: ' . $this -> actualSpeed.
        ' ';
    }
}

// Coche1 y usando la funcion accelerate y details
echo 'Coche 1: ';
$car1 = new car();
$car1 -> set_brand('Toyota ');
$car1 -> set_model('Corolla ');
$car1 -> set_year(2020);
$car1 -> set_actualSpeed(50);
$car1 -> accelerate(50);
echo $car1 -> details();

// Coche2 y usando la funcion break y details
echo "\nCoche 2: ";
$car2 = new car();
$car2 -> set_brand('Honda ');
$car2 -> set_model('Civic ');
$car2 -> set_year(2019);
$car2 -> set_actualSpeed(60);
$car2 -> break(20);
echo $car2 -> details();

?>
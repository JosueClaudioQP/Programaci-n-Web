#!"C:\xampp\perl\bin\perl.exe"
use strict;
use warnings;
use CGI;

my $cgi = CGI->new;
print $cgi->header("text/html");
my $operacion = $cgi->param('operacion');
my $resp = ""; 

if($operacion){
    if($operacion =~ /^\s*(-?\d+(\.\d+)?)\s*([-+*\/])\s*(-?\d+(\.\d+)?)\s*$/){
        my $num1 = $1;
        my $operador = $3;
        my $num2 = $4;
        my $resultado;

        if($operador eq "+"){
            $resultado = $num1 + $num2;
            $resp = $resultado;
        } elsif ($operador eq "-"){
            $resultado = $num1 - $num2;
            $resp = $resultado;
        } elsif ($operador eq "*"){
            $resultado = $num1 * $num2;
            $resp = $resultado;
        } elsif ($operador eq "/"){
            if($num2 != 0){
                $resultado = $num1 / $num2;
                $resp = $resultado;
            } else {
                $resp = "<p>Error, no es posible dividir entre 0</p>";
            }
        }
        if (defined $resultado) {
            $resp = "<p>Resultado: $resultado</p>";
        }
    } else {
        $resp = "<p>Ingresar 2 numeros y un signo aritmetico</p>";
    }
} else {
     $resp = "<p>No se han ingresado datos</p>";
}

print <<HTML;
<html>
    <head>
        <title>Calculadora</title>
        <link rel="stylesheet" href="../css/styles.css">
        <link href="https://fonts.googleapis.com/css2?family=Afacad:wght@400;500&family=Josefin+Sans&family=Kalnia:wght@300&display=swap" rel="stylesheet">
    </head>
    <body>
        <div class="contenido">
            <h1>Calculadora</h1>
            <p>Ingresar numeros:</p>
            <form action="calculadora.cgi" method="post">
                <input type="text" name="operacion"><br>
                <input type="submit" value="Calcular">
            </form>
            $resp
        </div>
    </body>
</html>
HTML
#!"C:\xampp\perl\bin\perl.exe"
use strict;
use warnings;
use CGI;

my $cgi = CGI->new;
print $cgi->header("text/html");
my $operacion = $cgi->param('operacion');

if($operacion =~ /^\s*(-?\d+(\.\d+)?)\s*([-+*\/])\s*(-?\d+(\.\d+)?)\s*$/){
    my $num1 = $1;
    my $operador = $3;
    my $num2 = $4;
    my $resultado;

    if($operador eq "+"){
        $resultado = $num1 + $num2;
        print $resultado;
    }
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
        </div>
    </body>
</html>
HTML
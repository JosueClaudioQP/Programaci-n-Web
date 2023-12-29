#!"C:\xampp\perl\bin\perl.exe"
use strict;
use warnings;
use CGI;

my $cgi = CGI->new;
print $cgi->header("text/html");

my $operacion = $cgi->param('operacion');
print <<HTML;
<html>
    <head>
        <title>Calculadora</title>
        <link rel="stylesheet" href="styles.css">
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
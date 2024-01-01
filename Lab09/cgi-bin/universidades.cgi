#!"C:\xampp\perl\bin\perl.exe"
use strict;
use warnings;
use CGI;

my $q = CGI->new;
print $q->header("text/html");
print <<HTML;
<html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="../css/styles.css">
        <title>Universidades Licenciadas</title>
    </head>
    <body>
        <h1>UNIVERSIDADES LICENCIADAS</h1>
        <form action="universidades.cgi">
            <label for="list">Elegir opcion de busqueda</label>
            <select name="list">
                <option value="nombre">Nombre de universidad</option>
                <option value="periodo">Periodo de licenciamiento</option>
                <option value="depart">Deparamento local</option>
                <option value="programa">Denominacion del programa</option>
            </select>
        <p>Ingresar datos:</p>
        <input type="text" name="keyword"><br><br>
        <input type="submit" value="Buscar">
        </form>
    </body>
</html>
HTML

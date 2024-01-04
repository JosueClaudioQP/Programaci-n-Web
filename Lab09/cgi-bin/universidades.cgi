#!"C:\xampp\perl\bin\perl.exe"
use strict;
use warnings;
use CGI;

my $q = CGI->new;

print $q->header("text/html");
print <<HTML;
<html>
    <head>
        <meta charset="UTF-8">
        <title>Universidades Licenciadas</title>
        <link rel="stylesheet" href="../css/style.css">
    </head>
    <body>
        <h1>UNIVERSIDADES LICENCIADAS</h1>
        <div class="form">
            <form action="universidades.cgi">
                <label for="list">Elegir opcion de busqueda</label>
                <select name="list">
                    <option value="nombre">Nombre de universidad</option>
                    <option value="periodo">Periodo de licenciamiento</option>
                    <option value="depart">Departamento local</option>
                    <option value="programa">Denominacion del programa</option>
                </select>
                <p>Ingresar datos:</p>
                <input type="text" name="keyword"><br><br>
                <input type="submit" value="Buscar">
            </form>
        </div>
    </body>
</html>
HTML

my $list = $q->param("list");
my $keyword = $q->param("keyword");
my $flag;

if ($list && $keyword) {
    my $archivo_csv = 'base.csv';
    open(my $fh, '<', $archivo_csv) or die "No se puede abrir el archivo CSV: $!";

    print "<table border='1'>";
    print "<tr><th>Nombre de Universidad</th><th>Periodo de Licenciamiento</th><th>Departamento Local</th><th>Denominacion del Programa</th></tr>";

    while (my $line = <$fh>) {
        chomp $line;
        my @fields = split /\|/, $line;

        my ($nombre_universidad, $periodo_licenciamiento, $departamento_local, $denominacion_programa) = @fields[1, 4, 10, 16];

        my $value;
        if ($list eq "nombre") {
            $value = $nombre_universidad;
        } elsif ($list eq "periodo") {
            $value = $periodo_licenciamiento;
        } elsif ($list eq "depart") {
            $value = $departamento_local;
        } elsif ($list eq "programa") {
            $value = $denominacion_programa;
        }

        if ($value && $value =~ /$keyword/i) {
            print "<tr><td>$nombre_universidad</td><td>$periodo_licenciamiento</td><td>$departamento_local</td><td>$denominacion_programa</td></tr>\n";
            $flag = 1;
        }
    }

    close($fh);
    print "</table>";
}

if (!$flag) {
    print "<h1>No encontrado</h1>\n";
}


#!"C:xampp\perl\bin\perl.exe"
use strict;
use CGI;
  
print "Content-type: text/html\n\n";
print<<BLOCK;
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Google Search</title>
  <link rel="stylesheet" href="styles.css">
  <link href="https://fonts.googleapis.com/css2?family=Afacad&family=Josefin+Sans&family=Kalnia:wght@300&display=swap" rel="stylesheet">
</head>
<body>
  <header>
    <nav>
      <ul>
        <li><a href="index.html">Inicio</a></li>
        <li><a href="BusqSimple.html">Búsqueda Simple</a></li>
        <li><a href="BusqImagenes.html">Búsqueda de Imágenes</a></li>
        <li><a href="BusqAvanzada.html">Búsqueda Avanzada</a></li>
        <li><a href="ejemp.html">Búsqueda Avanzada 2</a></li>
      </ul>
    </nav>
  </header>
  <main>
    <h1>Bienvenido a Google Search</h1>
  </main>
</body>
</html>
BLOCK

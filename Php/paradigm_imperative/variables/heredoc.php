<?php
/* @brief: Heredoc es una forma de definir cadenas de texto largas en PHP.
 * @details: heredoc usage mode.
 * @file: heredoc.php
 * @date: 06/04/2024
 * @version 1.0 */

echo <<<LABEL
<!DOCTYPE html>
<html lang = 'es'>
<head>
    <meta charset = 'UTF-8'>
    <meta http-equiv = 'X-UA-Compatible' content = 'IE=edge'>
    <meta name = 'viewport' content = 'width=device-width, initial-scale=1.0'>
    <title>PHP</title>
    </head>
    <body>
        <form action ='index.php' method = 'post'>
            <input type = 'text' name = 'name' placeholder = 'Nombre'>
            <input type = 'text' name = 'email' placeholder = 'Correo'>
            <input type = 'submit' name = 'submit' value = 'Enviar'>
        </form>
        </body>
        </html>
LABEL;

// Arguments of a function
var_dump(array(<<<EOD
foobar!
EOD
));


// Inicializar variables estáticas
function foo()
{
static $bar = <<<LABEL
Nada aquí...
LABEL;
}

// Propiedades/constantes de clase
class foo
{
const BAR = <<<FOOBAR
Ejemplo de constante
FOOBAR;

public $baz = <<<FOOBAR
Ejemplo de propiedad
FOOBAR;
}
?>


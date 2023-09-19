CASO
 
1.- Crear un proyecto Django con el nombre nombre_apellido. 
2.- Dentro del proyecto, cree 2 aplicaciones una con el nombre menuApp y otra con 
el nombre optionApp con sus respectivas configuraciones. 
3.- La aplicación menuApp debe contar con una vista llamada vistaMenu con las 
siguientes características:
a) Debe ser su página principal.
b) Debe mostrar un título con la frase “Seleccione una opción”.
c) Una lista con 2 URL que llevarán cada una a las vistas de la aplicación 
optionApp.
4.- La aplicación optionApp debe contar con 2 vistas llamadas: vistaTabla y 
vistaLoteria.
5.- La vistaTabla debe tener las siguientes características:
a) Un título con la frase “Mis Países Favoritos”
b) Una tabla HTML con 3 columnas con los títulos País, Continente, Bandera.
c) Debe contener al menos 3 países con los datos mencionados anteriormente y 
la bandera debe ser una imagen.
d) Un botón para volver a la página principal.
6.- La vistaLotería debe tener las siguientes características:
a) Un título con la frase “Estos son los números de la suerte en este 
momento”
b) Una lista con 10 números al azar entre el 1 y el 100 ordenados de menor a 
mayor.
c) Un botón para volver a la página principal.
7.- Todas las vistas deben utilizar HttpResponse para su funcionamiento y deben 
devolver una variable

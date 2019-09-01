CONTENIDO
dos scripts hechos en python 2,7

FUNCION DE LOS SCRIPTS

- El primer script llamado PruebaOne activa tu camara y reconoce rostros usando la libreria de OpenCV (OpenCV 3.0)

- El segundo script llamado PruebaTwo importa la libreria Threading que es necesaria para lanzar los hilos en python, importa el script llamado PruebaOne para poder acceder a sus propiedades y funciones, también importa la libreria Time que se usa para crear una cuenta regresiva.

LANZAMIENTO DE UN HILO EN PYTHON

En el script llamado PruebaTwo con la libreria threading lanzamos el hilo de la función del reconocimiento de rostros del script PruebaOne

con esta linea creamos el hilo
c = threading.Thread(target = PruebaOne.DetectionFace)

con esta segunda linea iniciamos o lanzamos el hilo
c.start()

en este bloque for creamos una cuenta regresiva de 10 a 0 y al terminar accede a la propiedad run de el script PruebaOne y lo vuelve falso.

for i in xrange(10,0,-1):
    time.sleep(1)
    print i
    if i <= 1:
        PruebaOne.run = False

DETENER UN HILO (KILLER HILO)

Para detener el hilo se a creado en el script PruebaOne una condicion if que analiza su propiedad run la cual mientras sea verdadera deja correr el hilo sin problema alguno de lo contrario al ser falsa detiene la ejecución del hilo

con esta linea analizamos si la propiedad run es verdadera o falsa
if run == False:

con esta linea paramos el hilo y la ejecución del mismo
sys.exit().


Ahora desde el script PruebaTwo con la cuenta regresiva finalizada solo volvemos falsa la propiedad run
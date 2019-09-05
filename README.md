CONTENIDO
dos scripts hechos en python 2,7

FUNCION DE LOS SCRIPTS

- El primer script llamado PruebaOne activa tu camara y reconoce rostros usando la libreria de OpenCV (OpenCV 3.0)

- El segundo script llamado PruebaTwo importa la libreria Multiprocessing y Process que son necesarias para lanzar los procesos en segundo plano en python, importa el script llamado PruebaOne para poder acceder a su funcion "Detectionface", también importa la libreria Time que se usa para crear un delay de 10 segundos.

LANZAMIENTO DE UN PROCESO EN PYTHON

En el script llamado PruebaTwo con la libreria multiprocessing y Process lanzamos el proceso de la función del reconocimiento de rostros del script PruebaOne

con esta linea creamos el proceso
p = Process(target=PruebaOne.DetectionFace)

con esta segunda linea iniciamos o lanzamos el proceso
p.start()

con esta linea creamos un delay de 10 segundos

time.sleep(10)

DETENER UN PROCESO (KILLER PROCESS)

Para detener el proceso que se a creado en el script PruebaTwo usamos la libreria Psutil y una función KillProcess a la que le pasamos el PID como argumento del proceso que queremos que se detenga y con la libreria psutil y el PID del proceso identificamos el procesos que queremos detener

con esta linea identificamos al proceso que queremos detener
p = psutil.Process(posProcess)

con este bloque for buscamos otras posibles instancias del proceso que lanzamos y si las hay las detiene también

for proc in p.children(recursive=True):
        proc.kill()

con esta linea paramos el proceso y la ejecución del mismo
p.kill()


Ahora desde el script PruebaTwo con la cuenta regresiva finalizada solo volvemos falsa la propiedad run
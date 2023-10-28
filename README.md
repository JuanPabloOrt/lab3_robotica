# lab3_robotica
Theylor Amata
Juan Pablo Ortiz
2023-2 Robotica
En este repositorio se explica el paso a paso del uso de ROS , Toolbox para matlab y creacion de un script en python para el movimiento del nodo turtle
Para este laboratorio se utilizo el software libre ROS para linux, este corre en la version de Ubuntu 20.04.
El ros Fue implementado usando Ubunto y trbajandolo sobre una maquina virtual.

Se utilizo Python 3.9.18, para el enlace entre ROS y Matlab, ademas de que es utilizado el Toolbox ROS tambien, por otro lado, es necesario hace enfasis en que se requirio que el ubuntu fuera el 20.04.

# Conexion con matlab

Para realizar la conexion, fue necesario tener el toolbox ROS, con este toolbox se logra hacer la union de Matlab y ROS.

la conexión entre ROS (Robot Operating System) y MATLAB se puede realizar utilizando el Robotics System Toolbox de MATLAB, que proporciona funcionalidades para interactuar con robots y sistemas de control.

Para conectar ROS con MATLAB y Python a través del Robotics System Toolbox, aquí hay un resumen de los pasos básicos:
Conexión de ROS con MATLAB:

Instalar ROS: Asegúrate de tener instalado ROS en tu sistema.
Configurar el entorno de trabajo de ROS: Antes de comenzar, inicia el sistema de ROS mediante el comando roscore en una terminal.
Configurar la conexión con MATLAB:
Inicia MATLAB.
Utiliza el Robotics System Toolbox para conectarte a ROS. MATLAB proporciona funciones específicas para trabajar con ROS, como rosinit para iniciar la conexión con el máster de ROS.
Interactuar con nodos ROS: Conecta y controla nodos ROS desde MATLAB utilizando funciones como rostopic, rosbag, rospublisher, rossubscriber, entre otras.
Conexión de ROS con Python:
Instalar ROS: Asegúrate de tener ROS instalado en tu sistema.
Instalar bibliotecas ROS para Python: Utiliza rospy, la biblioteca de ROS para Python, que te permitirá interactuar con ROS desde scripts de Python.
Configurar la conexión con ROS desde Python
Interactuar con ROS desde Python: Utiliza rospy para publicar o suscribirte a tópicos, interactuar con servicios y más, de manera similar a como lo harías desde MATLAB.
Integración con MATLAB y Python:
El Robotics System Toolbox de MATLAB también admite la comunicación bidireccional con ROS. Puedes comunicarte entre MATLAB y Python utilizando ROS como intermediario.
MATLAB puede llamar a funciones o scripts de Python que utilizan rospy.
Python puede suscribirse o publicar mensajes a tópicos de ROS que MATLAB también puede leer o escribir.
Es importante tener en cuenta que ambos entornos deben tener acceso a las mismas interfaces o mensajes ROS para una comunicación fluida.
Por favor, ten en cuenta que los detalles específicos de la implementación dependerán de tu configuración de ROS, la estructura de tu red, los mensajes y los comandos que necesites intercambiar entre MATLAB y Python.

A continuacion se muestra como se realizo el script en Matlab
![ros_matlab](https://github.com/JuanPabloOrt/lab3_robotica/assets/144562439/1df41383-c720-4144-86c8-169c9b65fabb)


Se observa como se ejecuta la pantalla de turtle node y se realiza el movimiento de la tortuga, siendo indicio de que fue correcta la instalcion del ROS y Matlab y la conexion de los nodos.

# Creacion script Python



El script se crea basado en las librerias brindadas en la guia, Se reconocen las teclas segun ASCII, luego se crea la funcion que lee las escritura de teclado, luego de eso se crea la funcion que obtiene la entrada del teclado y lo escibe al ROS para que este se mueva en la direcion deseada segund sea Presionado. son ASDW( izqu, abajo, derechac, arriba) R para mostras trayectoria, y espacio para movimiento instantaneo.

![py](https://github.com/JuanPabloOrt/lab3_robotica/assets/144562439/5e409677-205a-45a0-8360-95faaafce9d0)


# Creacion Entorno Hello_turtle

Para la creacion del escenario, es preciso iniciar Ros en consola con el comando roscore.
![roscore](https://github.com/JuanPabloOrt/lab3_robotica/assets/144562439/e2496db4-d23f-4c0f-8467-af5925b0705f)

Luego de esto, se realiza la creacion del entrono, todo con el tool catkin, Este tool determina cual va a ser el escenario donde va a estar la simulacion, o la prueba que se dessee realizar.

Para realizar esto, es necesario tener presente los archivos de los repostiorios brindados en la guia, en especial el Hello_turtle https://github.com/felipeg17/hello_turtle/commits?author=fegonzalez7
Luego de tener todos estos archivos, se organizan los ficheros, y se edita el CMakelist.txt, añadiendo en la seccion de lectura de script de python el realizado por nosotros que fue lab.py para la lectura de teclado y traduccion en movimiento de la tortuga. 
![ficheros](https://github.com/JuanPabloOrt/lab3_robotica/assets/144562439/d09d72e3-f4a9-4795-9306-c6816f97f23e)


Entonces se da la creacion de la carpeta SRC donde se añaden los launch y los scripts de python para la formacion del escenario, luego se  ejecuta y crea el escenario con el comando catkin_make y se compila un codigo de la sigueinte forma
![catkin](https://github.com/JuanPabloOrt/lab3_robotica/assets/144562439/b49c3181-da0f-4673-b9ba-8bee279e327f)

Se crean varios ficheros nuevos, estos son los escenarios para el proyecto deseado, desafortunadamente, al momento de ejecutar nuesto proyecto, se presento un error de lectura de los scripts de python, al cual se le trabajo a lo largo de varios dias, pero no se encontró el defecto dentro de Cmakelist.txt  Ya que el compilador no encuentra el script lab.py como se muestra acontinuación
![error](https://github.com/JuanPabloOrt/lab3_robotica/assets/144562439/7d5d8d0c-e7b7-4f3e-9396-3b65b7d00312)

Por lo cual no se pudo realizar la prueba de movimiento deseada. Esto se pudo deber a un error de creacion de escenario, o incluso un error dentro del script que puede anular todo el proyecto. Por esto se realizo en varias carpetas la creacion del escenario con el fin de realizar un debug del proyecto, pero siempre se llegó al mismo resultado. 

Es importante antes de la creacion del script lector uy traductor del teclado a ovimiento realizar purebas de escritorio, para verificar paso a paso el funcionamiento correcto de este.

# Conclusiones

ROS es una herramienta poderosa para desarrolladores de robotica, e incluso videojuegos, que al ser software libre, con el dominio suficiente permite lograr simulaciones de escenarios o incluso movimientos controlados por teclado como deberia verse en una Megaindustria y su sala de control. por tanto para defectos de nuestro intentos de comandos a distancia por computador de un equipo, el nuestro no logro realizar la compilación del proyecto debido a errores hmanos. o incluso errores compilatorios del sistema, esto sucede a menudo en programas utilizano como base UNIX. Es importante para futuros trabajos probar paso a paso cada escript y verificar la escritura de las instrucciones d ecompilación para asi lograr un poryecto con ROS exitoso. Por otra parte se observo exitosamente como una herramienta cientifica como Matlab permite interactuar con este software libre, dando asi paso a una poderosa utilidad de desarrollo para la robotica ya sea aficionada o industrial.

# lab3_robotica
En este repositorio se explica el paso a paso del uso de ROS , Toolbox para matlab y creacion de un script en python para el movimiento del nodo turtle
Para este laboratorio se utilizo el software libre ROS para linux, este corre en la version de Ubuntu 20.04.
El ros Fue implementado usando Ubunto y trbajandolo sobre una maquina virtual.

Se utilizo Python 3.9.18, para el enlace entre ROS y Matlab, ademas de que es utilizado el Toolbox ROS tambien, por otro lado, es necesario hace enfasis en que se requirio que el ubuntu fuera el 20.04.

#Conexion con matlab

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
<p align="center"><img src="./Herramienta, ros_matlab.jpg" width=60%></p>

Se observa como se ejecuta la pantalla de 
# TerceraPre-entrega_Davila
En este proyecto denominado TerceraPre-entrega,se han desarrollado tres formularios principales para un cliente,producto y tienda. En dichos formularios,se podran registrar los datos solicitados para cada tipo y seran almacenados en una base de datos. 
Por otro lado,se crearon tres formularios mas pero sus funciones son solamente de busqueda,es decir, dependiendo si queremos buscar datos de un cliente,producto o tienda,es el formulario que vamos a utilizar.Dicho formulario,esta programado para buscar por el nombre,ya que es el mejor id para buscar todos los datos referidos a ese nombre y mostrarlos en la pantalla. 
Se ha trabajo en Python,con ciertas inclusiones de html5 para poder dar un poco mas de estetica a los formularios. Con el, creamos 6 templates,uno para cada formulario,a los cuales se acceden a partir de la configuracion establecida con respecto a sus url dentro del codigo. 
Con respecto a cliente,producto y tienda,se crearon clases respectivas (archivo models.py) a cada uno y se reflejaron en formato de formularios (forms.py) a partir de librerias de django. La funcion de cada formulario,esta desarrollada en el archivo views.py.
Con respecto a los formularios de busqueda,solo se crearon tres clases en el archivo forms.py,y se trabajo su funcionalidad en el archivo views. En dicho archivo esta esepcificado a que accion corresponde y en el archivo urls.py se encuentra la url correspondiente en cada path para poder acceder a la misma.

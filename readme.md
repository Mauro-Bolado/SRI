# Proyecto Final
## Sistema de Recuperación de Información

### Descripción:

##### Concepto:
La recuperación de información es el conjunto de actividades orientadas a facilitar la localización de determinados datos u objetos, y las interrelaciones que estos tienen a su vez con otros. Existen varias disciplinas vinculadas a esta actividad como la lingüística, la documentación o la informática.

Aunque tradicionalmente se limitaba a la recuperación de documentos escritos, el término se redefinió para incorporar la creciente aparición de materiales multimedia. Asi, los nuevos buscadores de información en Internet, que originariamente buscaban textos, expandieron su actividad a imágenes, videos o audios.  De esta forma términos como Recuperación de textos, recuperación documental y recuperación de información son utilizados como equivalentes.

Por otro lado, la necesidad de localizar datos concretos ha ido expandiendo su área de actuación. En la actualidad se está migrando desde la recuperación de documentos a la recuperación pregunta-respuesta, que responden con el dato concreto y no con el conjunto de documentos que posiblemente contenga este dato.

### Modelo Vectorial:

##### Historia:
El Modelo vectorial de recuperación de información fue presentado por Gerard Salton en 1975 y posteriormente asentado en 1983 junto con Mc Gill . Propone un marco en el que es posible el emparejamiento parcial a diferencia del modelo de recuperación booleano, asignando pesos no binarios a los términos índice de las preguntas y de los documentos. Estos pesos de los términos se usan para computar el grado de similitud entre cada documento guardado en el sistema y la pregunta del usuario.

##### Concepto general:
La idea básica de este modelo de recuperación vectorial reside en la construcción de una matriz (podría llamarse tabla) de términos y documentos, donde las filas fueran estos últimos y las columnas correspondieran a los términos incluidos en ellos. Las filas de esta matriz (que en términos algebraicos se denominan vectores) serían equivalentes a los documentos que se expresarían en función de las apariciones (frecuencia) de cada término. La longitud del vector de documentos sería igual al total de términos de la matriz (el número de columnas). De esta manera, un conjunto de m documentos se almacenaría en una matriz de m filas por n columnas, siendo n el total de términos almacenamos en ese conjunto de documentos.

La segunda idea asociada a este modelo es calcular la similitud entre la pregunta (que se convertiría en el vector pregunta, expresado en función de la aparición de los n términos en la expresión de búsqueda) y los m vectores de documentos almacenados. Los más similares serían aquellos que deberían colocarse en los primeros lugares de la respuesta.

##### Implementación actual:

###### Aproximación por cosenos:
La aproximación por el coseno entre dos vectores concurre en que tan distantes son las direcciones de los mismos, con esta idea y lo planteado anteriormente del modelo vectorial se tiene la actual implementación.

###### Procesamiento de los datos:
La idea es convertir todos los documentos del dataset en vectores (parse_documents), procesar la ¨query¨(consulta) para que también sea un vector (parse_query), determinar el vocabulario de todo el conjunto de vectores (get_vocabulary) y calcular las ocurrencias de cada palabra del vocabulario en el documento (get_word_counts).

###### Obtención del resultado:
Aplicando la aproximación por cosenos al vector pregunta con los vectores de documentos se obtiene un top de los más próximos a la pregunta según el modelo. (get_cosine_similarity)

###### Forma de uso y particularidades:
Para la implementación actual ser ejecutada es necesario escribir en la consola interactiva:
- python run.py [query argument] [dataset path argument]
  
Se obtiene como resultado una lista de 10 (valor modificable en futuras versiones) documentos que fueron los más cercanos a la consulta.
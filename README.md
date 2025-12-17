# Ejercicio de práctica para prueba!

Hola Doris!
Espero te encuentres muy bien

Te dejo aqui lo que sería tu prueba para Backend

Tienes que crear una API para este frontend, intenté dejarlo lo mejor comentado posible ya que mi idea no es que trabajen tanto frontend, mucho menos porque estos conceptos no los han visto

Para el uso de guardar una persona necesitas de un token, para ello se puede obtener uno en la página "con token"
El API solamente tiene que tener 3 funciones en views:
1. Una función que entregue una persona aleatorio
   - Para eso puedes utilizar la libreria `random` con su funcionalidad `randint`
   - No es necesario el uso de token para esto
   - El frontend deberia hacerse cargo de cambiar el nombre en la página
2. Una función que entregue **todas** las personas de la base de datos
   - Necesitamos de un token para esto
   - Por ello tienes que restringir esta petición si no está autenticado
3. Una función que guarde una persona
   - También se necesitará de un token para esto

Para la base de datos solamente busco un modelo Persona que tenga nombre y apellido
El frontend deberia de hacerse cargo de todo, tiene funciones para obtener el JWT, para usarlo y para guardarlo en localStorage

Mucho éxito!
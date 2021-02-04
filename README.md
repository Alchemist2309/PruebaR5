# PruebaR5
### Instalación chrome driver linux
- Descargar versión de chromeriver segun la versión de google instalada en el equipo, en el siguiente link puede descargar el driver https://chromedriver.chromium.org/
- copie el archivo en la ruta /usr/bin

### Proceso CI
- instalación de jenkins y configuración en maquina local 
- instalación de docker y docker-compose
- desrcargar imagen con el comando en la maquina local - docker pull selenium/standalone-chrome
- se crea el archivo dockerfile para construir nuestra propia imagen docker con los requerimientos para la ejecución del proyecto
- se crea el docker-compose para darle la estructura y configuración para iniciarse el contenedor
- se le dan permisos a el usuario jenkins en sudoers de la maquina local
- se crea la tarea en jenkins de tipo estilo libre "tarea basica"
- se asigna el nombre de la tarea "PruebaR5"
- se configura el origen del codigo fuente desde github
- en disparadores de ejecuciones se checkea consultar repositrio(SCM) y digita la expresión cron * * * * * que equivale a revisar el repositorio en github cada minuto
- se configura en ejecutar la linea de comandos shell:

- sudo docker-compose up -d --build - construye la imagen basada en el dockerfile y luego la ejecuta 

- sudo docker cp ./ selenium-test-soat:/testeo - copia todo el repositorio y lo envia al contenedor para que existan los archvos del proyecto en el contenedor 

- ejecutar los archivos del proyecto con la automatización de las pruebas 
- sudo docker exec selenium-test-soat bash -c "python3 ./src/test/test_buy_soat_not_valid01.py"
- sudo docker exec selenium-test-soat bash -c "python3 ./src/test/test_buy_soat_not_valid02.py"
- sudo docker exec selenium-test-soat bash -c "python3 ./src/test/test_buy_soat_valid01.py"
- sudo docker exec selenium-test-soat bash -c "python3 ./src/test/test_buy_soat_valid02.py"

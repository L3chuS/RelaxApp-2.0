# RelaxApp 2.0

<img src="./Configuration_Files/images/3.PNG" width=25% height=25%>

---
### Qué es RelaxApp 2.0?

#### Es una aplicación de escritorio creada para gestionar descansos musculares y visuales. Permite personalizar temporizadores y establecer alertas mientras estés realizando alguna actividad en particular.
#### RelaxApp 2.0 es una evolución de la versión 1.0 que mantiene su funcionalidad principal, pero introduce una nueva arquitectura basada en una API REST con Django REST Framework, separando la interfaz de usuario de la lógica del servidor y de la base de datos. Esta separación permite mejorar la organización, mantenimiento y escalabilidad de la aplicación.

---

### Compatibilidad

#### - ✅ Windows 10 / 11
#### - ❌ Linux
#### - ❌ macOS

---

### Tecnologías utilizadas

#### >> Python 3: Lenguaje de desarrollo
#### >> Customtkinter: Interfaz gráfica
#### >> Django: Framework para el desarrollo del backend
#### >> Django REST Framework: Desarrollo de la API REST
#### >> MySql: Base de datos
#### >> Railway: Base de datos en la nube
#### >> Pygame: Gestión de sonidos
#### >> Python-dotenv: Gestión de variables de entorno
#### >> Requests: Comunicación entre la interfaz y la API REST

---

### Instalación:

#### 1 - Dirígete al apartado de "releases", busca en las "Assets" y descarga "RelaxApp_Setup_2.0.0".
#### 2 - Ejecuta el archivo descargado.
#### 3 - Sigue los pasos indicados por el instalador hasta finalizar.
#### 4 - Inicia la aplicación.
#### 5 - En el menú de inicio registra tu usuario desde el botón ubicado a la izquierda abajo.
#### 6 - Completa los campos requeridos y pulsa aceptar.
#### 7 - Disfruta de RelaxApp.

---

### Primeros pasos:

#### >> Inicialmente el menú principal te permite iniciar sesión, registrarte o cambiar tu contraseña:

<img src="./Configuration_Files/images/1.PNG" width=25% height=25%>

#### >> El menú de registro pide datos básicos necesarios para comenzar a utilizarla: 

<img src="./Configuration_Files/images/2.PNG" width=25% height=25%>

---

### Cómo funciona?

#### >> Una vez logueado, verás todas las opciones para configurar la aplicación:

<img src="./Configuration_Files/images/3.PNG" width=25% height=25%> 

#### >> Si elijes el sub-menú de descanso visual o de estirar podrás establecer la configuración general. Allí verás distintos campos a configurar:
* Duración: hace referencia al tiempo en horas y minutos que el usuario prevee que estará realizando la actividad.
* Intervalo Alertas: define cuanto tiempo en minutos transcurre entre cada descanso.
* Tiempo Descanso: es la duración establecida antes de volver a tu actividad principal.
* Activar sonido: permite habilitar una alerta sonora cada vez que haya un descanso o cuando la aplicación finalice.

<img src="./Configuration_Files/images/4.PNG" width=25% height=25%>

#### >> Así quedaría un ejemplo de la aplicación configurada:

<img src="./Configuration_Files/images/5.PNG" width=25% height=25%>

#### >> Es decir, durante 8hs, descansarás 5 minutos cada 60 minutos que hayan pasado.

#### >> RelaxApp te permite gestionar los sonidos a tu manera. Tendrás para seleccionar 2:
* Uno será para cada alerta de descanso.
* El otro para cuando la cuenta atrás haya finalizado.
#### >> Al mismo tiempo, hay 2 sonidos por default pero también puedes importar tus propias alarmas en los formatos permitidos:

<img src="./Configuration_Files/images/6.PNG" width=25% height=25%>

#### >> Una vez tengas tus opciones configuradas podrás acceder al menú de "Perfiles" para guardarlos y no tener que configurarlos cada vez que inicies la app. Puedes guardas hasta 3 distintos y adaptarlos a tus actividades cotidianas:

<img src="./Configuration_Files/images/7.PNG" width=25% height=25%>

---

### Comenzando:

#### >> Cuando tengas todo listo, deberás elegir al menos una opción para iniciar RelaxApp. Si ya tienes un perfil guardado, puedes seleccionar esa opción. En caso de que no lo tengas, puedes elegir "Descanso Visual", "Estirar" o los dos y se iniciará con los últimos valores que tengas cargados desde que se haya iniciado la sesión. Es importante destacar que, al cerrar la sesión, sólo se mantienen los perfiles guardados. Las configuraciones realizadas en "Descanso Visual", "Estirar" o "Sonidos" son temporales. 

<img src="./Configuration_Files/images/8.PNG" width=25% height=25%>

#### >> Finalmente, RelaxApp comenzará la cuenta atrás con lo que hayas configurado o el perfil que tengas establecido por defecto. Mientras el tiempo restante va disminuyendo, el descanso comenzará cuando el intervalo haya finalizado. Cuando este descanso termine, dará inicio nuevamente al intervalo y así sucesivamente hasta que el tiempo restante sea cero. Aquí se ve un ejemplo de la aplicación en funcionamiento:

https://github.com/user-attachments/assets/c9dd7898-b509-4b72-9e90-49ce7248c5a5

---

### Autor:

#### Nombre: Esteban Santos Mendoza
#### Github: https://github.com/L3chuS

---

# ![Imágen perfil.](https://raw.githubusercontent.com/L3chuS/L3chus/main/Perfil_Emoji.png) Hola, soy Esteban Santos Mendoza!! 👋 

### Soy informático que trabaja hace 7 años en el mundo del soporte técnico. Actualmente me estoy formando como desarrollador en Python y estudiando un grado superior en el IOC (Institut Obert de Catalunya) en Desarrollo de Aplicaciones Web.
### En mi perfil de GitHub tienes más información sobre mi. Saludos!

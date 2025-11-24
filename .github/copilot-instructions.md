- Propósito
- Proveer a un agente de IA con el conocimiento mínimo y específico para ser productivo en este repositorio educativo de Python.

Resumen del proyecto
- Repositorio pequeño de ejemplos y ejercicios en Python organizados en dos carpetas principales:
  - `FORO_UD03/`: scripts de foro y demostraciones (p. ej. `manipulacion_básica_1.py`, `1_figura_triangulo_cuatros.py`).
  - `UD03_EJ_UD01/`: ejercicios numerados `Ejercicio_1.py` … `Ejercicio_22.py`.
- No hay paquetes instalables ni configuraciones de build complejas; son scripts ejecutables y archivos sueltos.

Arquitectura y flujo de datos (big picture)
- No hay servicios ni procesos persistentes: cada archivo `.py` es una unidad ejecutable independiente que opera con entrada/salida estándar o imprime resultados.
- No hay comunicación entre procesos ni dependencias entre directorios; modificar un script raramente afecta a otro, salvo que se importe explícitamente.

Convenciones del proyecto (útiles para el agente)
- Nombres: los ejercicios usan el patrón `Ejercicio_<n>.py` y los ejemplos del foro usan nombres descriptivos numéricos o con guiones bajos.
- Codificación/archivos: algunos nombres contienen caracteres acentuados (p. ej. `manipulacion_básica_1.py`). NO renombres archivos con acentos: mantener UTF-8 y rutas tal cual.
- Estilo: código procedural, pocas funciones reutilizables; evita introducir paquetes o reestructuraciones grandes sin permiso explícito.

Cómo ejecutar (Windows PowerShell)
- Ejecutar un script simple:
  - `python .\FORO_UD03\manipulacion_básica_1.py`
  - `python .\UD03_EJ_UD01\Ejercicio_1.py`
- Si el usuario está en otra carpeta, usar rutas relativas desde la raíz del repo.

Pruebas y construcción
- No hay tests automatizados ni CI configurado en el repo. No crear infra de pruebas a menos que el usuario lo solicite.

Patrones y ejemplos detectables
- Scripts de salida por consola: buscar `print(` para entender qué espera el usuario como salida.
- Entradas: pocos scripts piden input interactivo; si vas a automatizar ejecuciones, evita romper interactividad.

Integraciones externas
- No se usan dependencias externas (no hay `requirements.txt` ni `pyproject.toml`). Antes de añadir paquetes, confirmar con el usuario.

Qué puede cambiar un agente y qué evitar
- Cambiar/formatar: correcciones puntuales, refactorizaciones pequeñas (extraer funciones) y arreglos de encoding son aceptables.
- Evitar: renombrar masivamente archivos (especialmente con acentos), introducir dependencias sin autorización, reorganizar la estructura de carpetas.

Ejemplos concretos
- Si mejoras `FORO_UD03/1_figura_triangulo_cuatros.py`, mantén la salida y las funciones públicas compatibles.
- Si corriges `UD03_EJ_UD01/Ejercicio_10.py`, prueba la ejecución con `python .\UD03_EJ_UD01\Ejercicio_10.py` y verifica outputs impresos.

Preguntas para el mantenedor (antes de cambios grandes)
- ¿Quieres que convierta los scripts en un paquete instalable o mantengo la estructura de scripts sueltos?
- ¿Puedo renombrar archivos con caracteres no-ASCII para facilitar el trabajo en CI/Windows si lo solicitas?

Dónde mirar primero (archivos clave)
- `FORO_UD03/` — ejemplos y demostraciones (buen punto de partida para cambios pequeños).
- `UD03_EJ_UD01/` — colección de ejercicios; sigue los patrones de nombres y salidas.

Contacto y revisión
- Después de aplicar cambios significativos, abre un PR y solicita revisión manual; documenta la intención en la descripción del PR.

Fin

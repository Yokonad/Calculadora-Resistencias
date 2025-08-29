
# CALCULADORA DE RESISTENCIAS POR CODIGO DE COLORES

## DESCRIPCION DEL PROYECTO

### Objetivo
Herramienta profesional para el calculo de resistencias electricas por codigo de colores, con interfaz simple y funcionalidad esencial.

### Caracteristicas Principales
- Calculo automatico del valor segun colores seleccionados
- Soporte completo para resistencias de 4, 5 y 6 bandas
- Sistema de historial de calculos
- Interfaz de terminal simple y profesional
- Sugerencias comerciales y combinaciones alternativas
- Sistema de ayuda completo

## FUNCIONALIDADES

### Menu Principal
```
MENU PRINCIPAL
--------------------
1. Calcular resistencia por colores
2. Historial de calculos
3. Ayuda y guia de uso
4. Salir
```

### Calculo de Resistencia
- Seleccion de cantidad de bandas (4, 5 o 6)
- Seleccion guiada de colores para cada banda
- Calculo automatico del valor en ohmios
- Calculo de tolerancia y rango posible
- Calculo de coeficiente termico (6 bandas)

### Historial de Calculos
- Registro automatico de todos los calculos
- Muestra los ultimos 10 calculos realizados
- Incluye fecha, hora y valores calculados

### Ayuda Completa
- Guia detallada de lectura de resistencias
- Explicacion de tipos de resistencias
- Tabla de colores de referencia
- Conceptos de tolerancia y precision

## REQUISITOS TECNICOS

### Entorno
- Python 3.7 o superior
- Sistema operativo: Windows, macOS, Linux
- Terminal estandar (no requiere UTF-8 especial)

### Instalacion
```bash
python --version
```

## MODO DE USO

### Ejecucion
```bash
python "calucaldora _resistencias.py"
```

### Navegacion del Menu
1. Selecciona una opcion del menu principal (1-4)
2. Sigue las instrucciones en pantalla
3. Usa numeros para seleccionar colores
4. Presiona Enter para continuar entre pantallas

### Seleccion de Colores
Los colores se muestran en formato simple:
```
SELECCION DE COLOR - DIGITO
------------------------------
 0. Negro     (valor: 0)
 1. Marron    (valor: 1)
 2. Rojo      (valor: 2)
 3. Naranja   (valor: 3)
 ...
```

## ESTRUCTURA DEL CODIGO

### Funciones Principales

#### Interfaz y Navegacion
```python
def mostrar_banner():          # Banner de bienvenida simple
def mostrar_menu_principal():  # Menu principal
def limpiar_pantalla():        # Limpieza de pantalla
def mostrar_colores():         # Seleccion de colores
```

#### Calculos Core
```python
def valor_resistencia():              # Calculo principal de resistencia
def valores_comerciales_cercanos():   # Sugerencias comerciales
def sugerir_combinaciones_paralelo(): # Combinaciones en paralelo
def sugerir_combinaciones_serie():    # Combinaciones en serie
```

#### Funciones de Usuario
```python
def calcular_resistencia_principal(): # Flujo principal de calculo
def mostrar_historial():             # Historial de calculos
def mostrar_ayuda():                 # Sistema de ayuda
```

### Estructuras de Datos

#### Tabla de Colores
```python
COLORES = [
    ("Color", digito, tolerancia%, coef_termico),
    ("Negro", 0, None, None),
    ("Marron", 1, 1, 100),
    # ... mas colores
]
```

#### Valores Comerciales
Series estandar E12/E24 desde 1Ohm hasta 1MOhm

## EJEMPLOS DE USO

### Ejemplo: Resistencia de 4 bandas
```
Bandas seleccionadas:
- 1a banda: Rojo (2)
- 2a banda: Marron (1)  
- 3a banda: Rojo (x10^2)
- 4a banda: Dorado (±5%)

Resultado: 2,100 Ohm (2.1 kOhm) ±5%
Rango: 1,995 Ohm - 2,205 Ohm
```

### Ejemplo: Salida del programa
```
CALCULADORA DE RESISTENCIAS POR CODIGO DE COLORES
Version 2.0 - Herramienta Profesional
==================================================

MENU PRINCIPAL
--------------------
1. Calcular resistencia por colores
2. Historial de calculos
3. Ayuda y guia de uso
4. Salir

Selecciona una opcion (1-4): 1

CALCULO POR CODIGO DE COLORES
==================================================

¿Cuantas bandas tiene la resistencia? (4, 5 o 6): 4

Configurando resistencia de 4 bandas...

SELECCION DE COLOR - DIGITO
------------------------------
 1. Marron    (valor: 1)
 2. Rojo      (valor: 2)
 3. Naranja   (valor: 3)
 4. Amarillo  (valor: 4)
 5. Verde     (valor: 5)
 6. Azul      (valor: 6)
 7. Violeta   (valor: 7)
 8. Gris      (valor: 8)
 9. Blanco    (valor: 9)

Selecciona el color de la 1a banda (digito 1): 2
```

## MEJORAS Y ACTUALIZACIONES

### Novedades v2.0
- Interfaz profesional y limpia sin decoraciones
- Sistema de navegacion simple e intuitivo
- Funcionalidades esenciales enfocadas
- Historial de calculos para seguimiento
- Sistema de ayuda completo integrado
- Codigo optimizado y mantenible

### Compatibilidad Mejorada
- Limpieza de pantalla adaptativa (Windows/Linux/macOS)
- Validacion robusta de entradas del usuario
- Manejo de errores mejorado con mensajes claros
- No requiere caracteres especiales ni UTF-8 avanzado

## DESARROLLO TECNICO

### Archivos del Proyecto
```
Proyecto Calculadora Resistencias v2.0
├── calucaldora _resistencias.py  # Aplicacion principal
├── README.md                     # Documentacion completa  
└── GUIA_RAPIDA.txt              # Guia de uso rapido
```

### Testing y Validacion
- Valores estandar: Verificado con serie E12/E24
- Calculos matematicos: Validados contra formulas oficiales  
- Casos extremos: Probado con valores minimos y maximos
- Interfaz de usuario: Testing de usabilidad en terminal

### Mantenimiento
- Codigo modular: Funciones independientes para facil mantenimiento
- Documentacion inline: Comentarios explicativos en codigo
- Estructura escalable: Preparado para futuras expansiones
- Interfaz simple: Facil de usar y entender
  
## 8. DESARROLLADOR

Nombre: Dan Ramos Reynaldo

## 9. LICENCIA

Distribuido bajo Licencia MIT


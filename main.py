import pyautogui as py
import time
import pyperclip
import sys
import os



ARCHIVO_TEXTO = "text.txt"

# Coordenadas (X, Y)
COORD_FOCO_TEXTO = (1000, 450) 
COORD_SIGUIENTE_PAGINA = (1100, 650)

# Límites de formato
MAX_CARACTERES_POR_LINEA = 19
MAX_LINEAS_POR_PAGINA = 14

# Tiempos de espera (en segundos)
TIEMPO_PREPARACION = 3
TIEMPO_ACTUALIZACION_PORTAPAPELES = 0.5
TIEMPO_TRANSICION_PAGINA = 1.0
TIEMPO_PULSACION = 0.1

# Seguridad
py.FAILSAFE = True 



def separar_en_paginas(texto: str, max_cols: int, max_rows: int) -> list[str]:
    """
    Simula el ajuste de línea de la interfaz gráfica.
    Separa el texto en páginas respetando los límites de columnas y filas.
    """
    paginas = []
    lineas_pagina_actual = []
    
    parrafos = texto.replace('\r\n', '\n').split('\n')
    
    for parrafo in parrafos:
        if not parrafo:
            lineas_pagina_actual.append("")
            if len(lineas_pagina_actual) == max_rows:
                paginas.append("\n".join(lineas_pagina_actual))
                lineas_pagina_actual = []
            continue
            
        palabras = parrafo.split(' ')
        linea_actual = ""
        
        for palabra in palabras:
            if not linea_actual:
                linea_actual = palabra
            else:
                if len(linea_actual) + 1 + len(palabra) <= max_cols:
                    linea_actual += " " + palabra
                else:
                    lineas_pagina_actual.append(linea_actual)
                    
                    if len(lineas_pagina_actual) == max_rows:
                        paginas.append("\n".join(lineas_pagina_actual))
                        lineas_pagina_actual = []
                        
                    linea_actual = palabra
        
        if linea_actual:
            lineas_pagina_actual.append(linea_actual)
            if len(lineas_pagina_actual) == max_rows:
                paginas.append("\n".join(lineas_pagina_actual))
                lineas_pagina_actual = []
                
    if lineas_pagina_actual:
        paginas.append("\n".join(lineas_pagina_actual))
        
    return paginas


def cargar_texto(ruta_archivo: str) -> str:
    """
    Lee el archivo de texto manejando posibles errores de ruta o formato.
    """
    if not os.path.exists(ruta_archivo):
        print(f"Error: El archivo '{ruta_archivo}' no existe.")
        sys.exit(1)
        
    try:
        with open(ruta_archivo, 'r', encoding='utf-8-sig') as archivo:
            return archivo.read()
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        sys.exit(1)


def pasar_pagina():
    """Ejecuta el clic para avanzar a la siguiente página."""
    py.click(COORD_SIGUIENTE_PAGINA[0], COORD_SIGUIENTE_PAGINA[1])
    time.sleep(TIEMPO_TRANSICION_PAGINA)


def escribir(texto: str):
    """
    Toma el texto completo, lo formatea y simula los comandos de teclado
    para pegarlo página por página.
    """
    print("El script comenzará en:")
    for i in range(TIEMPO_PREPARACION, 0, -1):
        print(f"{i}...") 
        time.sleep(1)
    
    # Hacer clic para enfocar el cuadro de texto
    py.click(COORD_FOCO_TEXTO[0], COORD_FOCO_TEXTO[1])
    time.sleep(0.5) 
    
    paginas = separar_en_paginas(texto, MAX_CARACTERES_POR_LINEA, MAX_LINEAS_POR_PAGINA)
    
    for indice, pagina in enumerate(paginas, 1):
        print(f"--- ESCRIBIENDO PÁGINA {indice}/{len(paginas)} ---")
        
        pyperclip.copy(pagina)
        time.sleep(TIEMPO_ACTUALIZACION_PORTAPAPELES)
        
        py.keyDown('ctrl')
        time.sleep(TIEMPO_PULSACION)
        py.press('v')
        time.sleep(TIEMPO_PULSACION)
        py.keyUp('ctrl')
        
        time.sleep(0.5)
        
        # No pasar página si es la última
        if indice < len(paginas):
            pasar_pagina()

    print("--- ESCRITURA FINALIZADA ---")


def liberar_teclas():
    """Libera modificadores de teclado que puedan quedar atascados por el sistema."""
    for tecla in ['alt', 'ctrl', 'shift', 'win']:
        py.keyUp(tecla)


def main():
    """Función principal de ejecución."""
    liberar_teclas()
    texto_base = cargar_texto(ARCHIVO_TEXTO)
    escribir(texto_base)


if __name__ == "__main__":
    main()
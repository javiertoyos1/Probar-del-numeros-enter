import pyautogui
import time
import keyboard

pyautogui.FAILSAFE = True

coordenadas_file = 'coordenadas.txt'
ultimo_numero_file = 'ultimo_numero.txt'

# Preguntar si se desea continuar por el último número utilizado
use_last_number = pyautogui.confirm('¿Desea continuar por el último número utilizado?', buttons=['Sí', 'No'])
if use_last_number == 'Sí':
    try:
        with open(ultimo_numero_file, 'r') as f:
            ultimo_numero_str = f.readline().strip()
            i = int(ultimo_numero_str)
            print(i)
            
            # Leer las coordenadas guardadas del archivo
            with open(coordenadas_file, 'r') as f:
                coordenadas1_str = f.readline().strip()
                coordenadas1 = tuple(map(int, coordenadas1_str.split(',')))
    except:
        0
else:
    i = 0
    # Guardar el número 0 en el archivo
    with open(ultimo_numero_file, 'w') as f:
        f.write('0')

    # Preguntar si se desean utilizar las coordenadas guardadas o unas nuevas
    use_saved_coords = pyautogui.confirm('¿Desea utilizar las coordenadas guardadas?', buttons=['Sí', 'No'])
    if use_saved_coords == 'No':
        # Mostrar un cuadro de diálogo para que el usuario haga clic en la pantalla y establezca las coordenadas de la primera zona
        pyautogui.alert(text='Posiciona el cursor en la coordenada deseada y pulsa ENTER', title='Establecer coordenadas', button='OK')
        coordenadas1 = pyautogui.position()
    
        # Guardar las coordenadas en el archivo
        with open(coordenadas_file, 'w') as f:
            f.write(f"{coordenadas1[0]},{coordenadas1[1]}\n")
    else:
        # Leer las coordenadas guardadas del archivo
        with open(coordenadas_file, 'r') as f:
            line = f.readline()
            coordenadas1 = tuple(map(int, line.strip().split(',')))

# Hacer clic en las coordenadas especificadas
pyautogui.click(coordenadas1[0], coordenadas1[1])
    
# Prueba todos los números desde 0000 hasta 9999
for i in range(i,10000):
    # Si 'p' se mantiene presionado, pausar el script
    if keyboard.is_pressed('p'):
        pyautogui.alert('Presiona ENTER para continuar.')
    # Si 'q' se mantiene presionado, terminar el script y guardar el último número probado
    if keyboard.is_pressed('q'):
        with open(ultimo_numero_file, 'w') as f:
            f.write(str(i))
        break

    # Formatea el número a una cadena de 4 dígitos
    code = str(i).zfill(4)
    
    # Escribe el código
    pyautogui.write(code)
    
    # Presiona Enter
    pyautogui.press('enter')
    
    # Espera X segundos antes de continuar
    time.sleep(0.3)
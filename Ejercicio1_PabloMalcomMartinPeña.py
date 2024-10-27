import psutil


blocnotas = False
# iteramos sobre los procesos y por cada iteracion imprimimos el pid, nombre y tiempo de reloj en el procesador, haciendo una suma sobre los datos que nos da cpu_times
for proc in psutil.process_iter(['pid', 'name', 'cpu_times', 'memory_percent']):   
    if(proc.name() == "notepad.exe"):
        blocnotasPID = proc.info['pid']
        blocnotas = True
    else:
        print(f''' 
        Nombre {proc.info['name']}
        PID    {proc.info['pid']}
        CPU    {sum(proc.info['cpu_times'][:2][-3:])}
        MEMORIA {proc.info['memory_percent']}
        ''')

# si blocnotas es true, imprimimos su PID para tenerlo localizado
if (blocnotas):
   print("")
   print(f"bloc de notas {blocnotasPID}")

# aqui le damos la opcion al usuario de poder terminar un proceso con su PID, para ello le pedimos un numero entero, y acontinuacion lo cerramos y si hay algun error lo dejamos
print("escribe 0 para salir")
PIDusuario = int(input("dame el PID del proceso: "))
while PIDusuario != 0:
    try: 
            proceso = psutil.Process(int(PIDusuario))
            proceso.terminate()
            print("proceso cerrado con exito")
    except Exception as e:
            print(f"error al cerrar el proceso: {e}")

    print("escribe 0 para salir")
    PIDusuario = int(input("dame el PID del proceso porfa: "))


    


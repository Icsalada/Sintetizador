import pyttsx3

# Creación del objeto
def configuracion(velocidad=125, volumen=1.0, voz_id=1):
    engine = pyttsx3.init()  # Creación del objeto

    # VELOCIDAD
    engine.setProperty("rate", velocidad)  # Configurando una nueva velocidad de voz

    # VOLUMEN
    engine.setProperty("volume", volumen)  # Estableciendo el nivel de volumen entre 0 y 1

    # VOZ
    voices = engine.getProperty("voices")  # Obteniendo detalles de la voz actual
    engine.setProperty("voice", voices[voz_id].id)  # Cambiando el índice, cambia las voces (0 para voz masculina, 1 para voz femenina)

    return engine

def vocalización_texto(engine, text):
    engine.say(text)
    engine.runAndWait()

def main():
    print("Hola esto es un programa de vocalizacion, escribe lo que te de la gana y el programa lo va a decir")
    text = input("Aqui escribe lo que quieres que la maquina diga --------->  ")
    velocidad = int(input("Para la velocidad dime un numero del 100 al 150 ---------> "))
    volumen = float(input("Aqui configura el volumen entre el 0.0 y 1.0--------->"))
    voz_id = int(input("Configura el genero de la voz(0 para hombre y 1 para mujer)---------> "))
    engine = configuracion(velocidad, volumen, voz_id)
    vocalización_texto(engine, text)
    engine.save_to_file( text, "Achivo.mp3")
    engine.runAndWait()
main()



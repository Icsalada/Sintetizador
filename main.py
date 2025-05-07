import pyttsx3

def configuracion(velocidad=135, volumen=1.0, voz_id=0):
    engine = pyttsx3.init()
    engine.setProperty("rate", velocidad)
    engine.setProperty("volume", volumen)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[voz_id].id)
    return engine

def vocalización_texto(engine, text):
    engine.say(text)
    engine.runAndWait()

def pedir_configuracion_con_voz():
    # Usamos voz por defecto para guiar al usuario
    engine = configuracion()
    
    vocalización_texto(engine, "Muy bien. Ahora dime cómo quieres que hable.")

    vocalización_texto(engine, "¿Qué velocidad quieres? Entre cien y ciento cincuenta.")
    velocidad = int(input("⚙️ Velocidad (100-150): "))

    vocalización_texto(engine, "¿Qué volumen debo usar? Entre cero punto cero y uno punto cero.")
    volumen = float(input("🔊 Volumen (0.0 - 1.0): "))

    vocalización_texto(engine, "¿Prefieres voz de hombre o de mujer? Escribe cero para hombre, uno para mujer.")
    voz_id = int(input("🎙️ Voz (0 = hombre, 1 = mujer): "))

    return configuracion(velocidad, volumen, voz_id)

def main():
    grabar_conversacion = []  # Lista para grabar todo lo hablado
    # Voz por defecto
    engine = configuracion()
    
    # 1. Pregunta inicial
    vocalización_texto(engine, "Hola. ¿Qué quieres que diga hoy?")
    texto = input("👉 Escribe lo que quieres que diga: ")

    # 2. Configuración personalizada
    engine = pedir_configuracion_con_voz()

    # 3. Decir el texto con nueva voz
    vocalización_texto(engine, texto, grabar_conversacion)

    # 4. Bucle interactivo
    while True:
        vocalización_texto(engine, "¿Quieres que diga algo más?")
        respuesta = input("🤖 ¿Quieres que diga algo más? (sí/no): ").strip().lower()

        if respuesta in ["no", "n"]:
            vocalización_texto(engine, "Ok bro. Hasta luego.")
            break
        if respuesta in ["tal vez", "nose","no lo se, tu dime",]:
            vocalización_texto(engine, "No me estes fastidiando, solo dime sí o no.")
        elif respuesta in ["sí", "si", "s"]:
            vocalización_texto(engine, "Ok, ¿qué quieres que diga?")
            texto = input("👉 Escribe lo que quieres que diga: ")
            vocalización_texto(engine, texto)
        else:
            vocalización_texto(engine,"Solo dime si o no,¿ acazo es tan dificil pensar? ")
        

main()
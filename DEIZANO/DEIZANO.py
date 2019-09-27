import time
import speech_recognition as sr

print('D.E.I.Z.A.N.O.')

r = sr.Recognizer()
#print(sr.Microphone.list_microphone_names())
mic = sr.Microphone(device_index=1)

while True:
    print('Fale um comando ...')
    with mic as source:
        audio = r.listen(source,timeout=5,phrase_time_limit=5)

    try:
        entrada = r.recognize_google(audio,language="pt-BR")
        #print("Você disse: " + entrada)
        if '10 anos' in entrada:
            #print('Trabalhando ...')
            if 'ligar a luz' in entrada:
                if 'quarto' in entrada:
                    print('Luz do quarto acesa') # comando NodeRED -> MQTT
                elif 'cozinha' in entrada:
                    print('Luz da cozinha acesa')
                elif 'terraço' in entrada:
                    print('Luz do terraço acesa')
                else:
                    print('Não sei onde é isso, Major')
            elif 'desligar a luz' in entrada:
                if 'quarto' in entrada:
                    print('Luz do quarto apagada') # comando NodeRED -> MQTT
                elif 'cozinha' in entrada:
                    print('Luz da cozinha apagada')
                elif 'terraço' in entrada:
                    print('Luz do terraço apagada')
                else:
                    print('Não sei onde é isso, Major')
            elif 'boa noite':
                print('Valeu, Major')
            else:
                print('Sei fazer isso não, Major')
        else:
            print("Como é, Major?")
    except:                                 # speech is unintelligible
        print("Como é, Major?")
    time.sleep(5)

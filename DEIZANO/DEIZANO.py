import time 
import speech_recognition as sr
import mysql.connector
import datetime
from google.cloud import texttospeech
from google.oauth2 import service_account

print('D.E.I.Z.A.N.O.')

r = sr.Recognizer()
#print(sr.Microphone.list_microphone_names())
mic = sr.Microphone(device_index=1)
lang = "pt"

# MySQL connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="deizanos"
)
mycursor = mydb.cursor()

# test

credential = service_account.Credentials.from_service_account_file('C:\infindtts-fdf80b4934dd.json')

texttospeech.TextToSpeechClient(credentials=credential)

client = texttospeech.TextToSpeechClient()

synthesis_input = texttospeech.types.SynthesisInput(text="Hello, World!")
voice = texttospeech.types.VoiceSelectionParams(
    language_code='pt-BR',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)

audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3)

response = client.synthesize_speech(synthesis_input, voice, audio_config)

with open('output.mp3', 'wb') as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')
# test

while True:
    flagMatch = False
    print('Fale um comando ...')
    with mic as source:
        audio = r.listen(source,timeout=5,phrase_time_limit=5)
    try:
        entrada = r.recognize_google(audio,language="pt-BR").lower()
        print("Você disse: " + entrada)
        if '10 anos' in entrada:            
            if 'ligar' in entrada:
                mycursor.execute("SELECT nomeEquipamento FROM equipamento")
                myresult = mycursor.fetchall()
                for x in myresult:
                    x = str(x)[:-3]
                    x = str(x)[+2:]
                    x = x.lower()
                    #print(x)
                    if x in entrada:
                        print(x, ' acesa') # comando NodeRED -> MQTT
                        flagMatch = True
                        break
                if flagMatch != True:
                    print('Não sei onde é isso, Major')
            elif 'desligar' in entrada:
                mycursor.execute("SELECT nomeEquipamento FROM equipamento")
                myresult = mycursor.fetchall()
                for x in myresult:
                    x = str(x)[:-3]
                    x = str(x)[+2:]
                    x = x.lower()
                    #print(x)
                    if x in entrada:
                        print(x, ' apagada') # comando NodeRED -> MQTT
                        flagMatch = True
                        break
                if flagMatch != True:
                    print('Não sei onde é isso, Major')
            elif 'boa noite' in entrada:
                print('valeu, major')
            elif 'fazer anotação' in entrada:
                print("Diga lá ...")

                with mic as source:
                    audio = r.listen(source,timeout=5,phrase_time_limit=5)
                try:
                    entradaAnot = r.recognize_google(audio,language="pt-BR").lower()
                    print("Você quer anotar: " + entradaAnot)

                    values = (time.strftime('%Y-%m-%d %H:%M:%S'), entradaAnot, 1)
                    commandSql = "INSERT INTO anotacao (dataCriacao, conteudo, idUsuarioFK) VALUES (%s, %s, %s)"
                    mycursor.execute(commandSql, values)

                    mydb.commit()

                    print("Anotado, Major")
                except:
                    print("Deu ruim, Major")
            elif 'ler anotações' in entrada:
                mycursor.execute("SELECT conteudo FROM anotacao WHERE idUsuarioFK = 1")
                myresult = mycursor.fetchall()
                print("Anotações:")
                for x in myresult:
                    x = str(x)[:-3]
                    x = str(x)[+2:]
                    print(x)
                
                tts = gTTS('hello')
            else:
                print('Sei fazer isso não, Major')
        else:
            print("Falou, Major?")
    except:                                 # speech is unintelligible
        print("Deu ruim, Major")

    time.sleep(5)
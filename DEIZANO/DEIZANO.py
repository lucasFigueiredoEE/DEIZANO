import time 
import speech_recognition as sr
import mysql.connector
import datetime

print('D.E.I.Z.A.N.O.')

r = sr.Recognizer()
#print(sr.Microphone.list_microphone_names())
mic = sr.Microphone(device_index=1)

# MySQL connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="deizanos"
)
mycursor = mydb.cursor()

# test

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
            else:
                print('Sei fazer isso não, Major')
        else:
            print("Falou, Major?")
    except:                                 # speech is unintelligible
        print("Deu ruim, Major")

    time.sleep(5)
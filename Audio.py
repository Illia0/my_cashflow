import os
import speech_recognition as sr
import pydub as pd
import wavio


language='ru_RU'
r = sr.Recognizer()

def recognise(filename):
    with sr.AudioFile(filename) as source:
        audio_text = r.listen(source)
        try:
            text = r.recognize_google(audio_text, language=language)
            print('Converting audio transcripts into text ...')
            print(text)
            return text
        except:
            print('Sorry.. run again...')
            return "Sorry.. run again..."

def audio_handler(bot, message):
    filename = str(message.from_user.id)
    file_name_full="./Audio/voice/"+filename+".ogg"
    file_name_full_converted="./Audio/ready/"+filename+".wav"
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name_full, 'wb') as new_file:
        new_file.write(downloaded_file)
    ttext="ffmpeg -i " + file_name_full + " -c:a pcm_f32le " + file_name_full_converted
    os.system(str(ttext))
    #data = pd.AudioSegment.from_ogg(file_name_full)
    #data.export(file_name_full_converted, format="wav")
    text = recognise(file_name_full_converted)
    os.remove(file_name_full)
    os.remove(file_name_full_converted)
    return text
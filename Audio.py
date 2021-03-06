import os
import speech_recognition as sr


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
    file_name_full=os.getcwd() + "\\Audio\\voice\\"+filename+".ogg"
    file_name_full_converted=os.getcwd() +"\\Audio\\ready\\"+filename+".wav"
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name_full, 'wb') as new_file:
        new_file.write(downloaded_file)
    os.system(os.getcwd() + "\\ffmpeg-5.0-full_build\\bin\\ffmpeg.exe"+" -i " + file_name_full + " " + file_name_full_converted)
    text = recognise(file_name_full_converted)
    os.remove(file_name_full)
    os.remove(file_name_full_converted)
    return text
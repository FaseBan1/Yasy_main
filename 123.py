import speech_recognition as sr
from gtts import gTTS
import openai

# Установите ваш API ключ от OpenAI
openai.api_key = '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'

# Функция для распознавания голоса
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Скажите что-то:")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="ru-RU")
        return text
    except sr.UnknownValueError:
        return "Извините, не могу распознать речь"
    except sr.RequestError:
        return "Проблема с подключением к сервису распознавания речи"

# Функция для взаимодействия с GPT-3 API
def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text

# Основной цикл для взаимодействия с помощником
while True:
    user_input = recognize_speech()
    print("Вы сказали:", user_input)

    if "стоп" in user_input.lower():
        print("Пока!")
        break

    gpt_response = chat_with_gpt(user_input)
    print("Помощник:", gpt_response)

    tts = gTTS(gpt_response, lang="ru")
    tts.save("assistant_response.mp3")

# загружаем модельку во время сборки докер образа
from transformers import pipeline

classifier = pipeline("text-classification", model="sismetanin/rubert-ru-sentiment-rusentiment")

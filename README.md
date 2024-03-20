## Описание решения

 - Для классификации использовался [https://github.com/velupanov/bert_rus_sentiment](sismetanin/rubert-ru-sentiment)
 - Для вебсервиса использовался фрэймворк [https://flask.palletsprojects.com/en/3.0.x/](Flask)

## Запуск

### Без docker-а

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Далее выведется ссылка, по которой нужно перейти. Будет показана страница:

![alt text](./assets/1.png)

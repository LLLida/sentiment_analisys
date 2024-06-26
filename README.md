## Описание решения

 - Для классификации использовался [sismetanin/rubert-ru-sentiment](https://github.com/velupanov/bert_rus_sentiment)
 - Для вебсервиса использовался фрэймворк [Flask](https://flask.palletsprojects.com/en/3.0.x/)

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

### С docker-ом

```bash
docker pull ghcr.io/lllida/sentiment_analisys:main
docker run -p 5000:5000 --name adil-sentiment-analysis sentiment_analisys:main
```

Далее заходим на [localhost:5000](localhost:5000).

from flask import Flask, request, jsonify, render_template
from transformers import pipeline

print('Starting...')

app = Flask(__name__)

classifier = pipeline("text-classification", model="sismetanin/rubert-ru-sentiment-rusentiment")

# text = "I really enjoyed this movie!"
# result = classifier(text)

# predicted_label = result[0]['label']
# confidence_score = result[0]['score']

# print(f"Predicted label: {predicted_label}")
# print(f"Confidence score: {confidence_score}")

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']

    prediction = classifier(text)[0]
    label = prediction['label']
    score = prediction['score']

    print('Predicted label:', label, 'with score:', score)
    if label == 'LABEL_2':
        template = 'positive.html'
    else:
        template = 'negative.html'
    return render_template(template, prediction=f'Уверенность {score:.2f}%')

@app.route('/')
def home():
    return render_template('index.html')

app.run(debug=True, host='0.0.0.0')

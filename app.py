import os

from argostranslate import translate, package
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

language_dir = './languages'

for language_file in os.listdir(language_dir):
    package.install_from_path(os.path.join(language_dir, language_file))


@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()

    source = data.get('source')
    target = data.get('target')
    elementsText = data.get('elementsText')

    languages = translate.load_installed_languages()
    source_lang = next((lang for lang in languages if lang.code == source), None)
    target_lang = next((lang for lang in languages if lang.code == target), None)

    translation = source_lang.get_translation(target_lang)

    return jsonify({'translated': [translation.translate(text) for text in elementsText]})

@app.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'Hello World!'})


if __name__ == '__main__':
    app.run()

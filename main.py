import os
import json

from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from argostranslate import translate, package

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

language_dir = './languages'

for language_file in os.listdir(language_dir):
    package.install_from_path(os.path.join(language_dir, language_file))


@app.post("/translate")
async def translate_text(request: Request):
    data = await request.json()

    source = data.get("source")
    target = data.get("target")
    elements_text = data.get("elementsText")

    languages = translate.load_installed_languages()

    source_lang = next((lang for lang in languages if lang.code == source), None)
    target_lang = next((lang for lang in languages if lang.code == target), None)

    if not source_lang or not target_lang:
        raise HTTPException(status_code=400, detail="Invalid source or target language code")

    translation = source_lang.get_translation(target_lang)
    translated_texts = [translation.translate(text) for text in elements_text]
    json_response = {"translated": translated_texts}

    print(json_response)

    return JSONResponse(content=json_response)

@app.get("/helloworld")
async def test():
    return {"message": "Hello World!"}

# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app, host="localhost", port=8080)

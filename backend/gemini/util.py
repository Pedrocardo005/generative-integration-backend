import google.generativeai as genai

from backend.settings import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)


class Util:
    @staticmethod
    def gemini_integration(text):
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(text)
        return response.text

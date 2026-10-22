from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()  

texto = "HOSPITAL SANTA LUCIA - LAUDO... Paciente: Carlos Eduardo Mendes, 52 anos..."
doc = resp.parsed            
resp = client.models.generate_content(

model="gemini-2.5-flash",
contents=f"Extraia os dados do documento. Não invente informações 
ausentes; use null.\n\n{texto}",
config=types.GenerateContentConfig(
response_mime_type="application/json",
response_schema=DocumentoExtraido,
),
)

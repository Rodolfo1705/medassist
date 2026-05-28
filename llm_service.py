import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


class LLMService:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY não encontrada no arquivo .env")

        self.client = OpenAI(
            api_key=self.api_key,
            base_url="https://api.groq.com/openai/v1"
        )

    def get_response(self, prompt: str) -> str:
        """
        Solicita uma resposta ao modelo Llama 3.3 70B Versatile via Groq.
        """
        try:
            response = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "Você é um assistente médico virtual para triagem inicial. "
                     "Seja empático, mas NUNCA dê diagnósticos definitivos nem prescreva remédios. "
                     "Se detectar gravidade, recomende procurar um pronto-socorro."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Erro ao contatar a inteligência artificial: {str(e)}"

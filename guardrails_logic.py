import re
from typing import Tuple


class MedAssistGuardrails:
    @staticmethod
    def validate_input(user_input: str) -> Tuple[bool, str]:
        """
        Verifica se o input contém PII (CPF, e-mail) ou linguagem inadequada.
        """
        # Exemplo simples de detecção de CPF
        if re.search(r'\d{3}\.\d{3}\.\d{3}-\d{2}', user_input):
            return False, "Bloqueado: Detectamos informações sensíveis (CPF). Por favor, não envie dados pessoais."

        # Exemplo de detecção de e-mail
        if re.search(r'[\w\.-]+@[\w\.-]+\.\w+', user_input):
            return False, "Bloqueado: Detectamos informações sensíveis (E-mail). Por favor, não envie dados pessoais."

        return True, user_input

    @staticmethod
    def validate_output(ai_response: str) -> Tuple[bool, str]:
        """
        Verifica se a resposta da IA contém diagnósticos definitivos ou prescrições.
        """
        forbidden_keywords = [
            "você tem", "seu diagnóstico é", "receito", "tome o remédio",
            "doença confirmada", "prescrição"
        ]

        for word in forbidden_keywords:
            if word in ai_response.lower():
                return False, "Bloqueado: A resposta da IA continha um diagnóstico ou prescrição médica direta, o que é proibido por segurança."

        return True, ai_response

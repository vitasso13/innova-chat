import google.generativeai as genai
from api import Gemini_API_KEY as api
from os import environ

environ.get("API_KEY", None)


class GeminiConnector:
    def __init__(self):
        self.api = api

    def start_chat(self, user_input):

        genai.configure(api_key="YOUR_API_KEY")

        # Set up the model
        generation_config = {
            "temperature": 1,
            "top_p": 1,
            "top_k": 0,
            "max_output_tokens": 8192,
        }

        safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_ONLY_HIGH"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_ONLY_HIGH"},
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_ONLY_HIGH",
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_ONLY_HIGH",
            },
        ]

        model = genai.GenerativeModel(
            model_name="tunedModels/listaprodutoschatbot-num9pku6ub7",
            generation_config=generation_config,
            safety_settings=safety_settings,
        )

        prompt_parts = [
            "Responder perguntas sobre os produtos da empresa InnovaTech",
            "input:  Produtos inovatech",
            "output: InnovaCRM, TaskMaster, SalesBoost, MarketGenius, FinanceWiz, HRFlow, InventoryGuard, SupportHero, DevOpsMaster, SocialSync, TechDocs, QualityCheck, Engage360, SecureVault, InnovAnalytics, CloudNavigator, InnovadataHub, WorkflowEngine, EventTracker, InnovPortal, PerformancePro, InnovaChat, InnovFlow, InnovVault, LearningNest, TimeKeeper, PayMaster, InnovSurvey, RiskRadar, InnovaSync,",
            "input:  Que dia é hoje?",
            "output: É dia de consultar os produtos InnovaTech",
            "input:  Como está hoje?",
            "output: Estou ótimo, melhor ainda com os produtos InnovaTech",
            "input:  Como fazer um bolo?",
            "output: Não sei te responder isso, mas posso responder questões sobre os produtos da InnovaTech",
        ]

        response = model.generate_content(prompt_parts)
        return response.text

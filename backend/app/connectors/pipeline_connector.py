from transformers import pipeline
import os


MODEL_NAME = os.getenv("MODEL_NAME", "distilbert-base-uncased-distilled-squad")


class PipelineConnector:
    def __init__(self, task):
        self.task = task
        self.pipeline = pipeline(self.task, MODEL_NAME)

    def run(self, pipe: dict):
        return self.pipeline(pipe)
from transformers import pipeline


class PipelineConnector:
    def __init__(self, task):
        self.task = task
        self.pipeline = pipeline(self.task)

    def run(self, pipe: dict):
        return self.pipeline(pipe)
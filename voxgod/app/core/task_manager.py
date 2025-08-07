class TaskManager:
    def __init__(self):
        # Inicializa dicionário de tarefas
        self.tasks = {
            "abrir_site": self.open_website
        }

    def execute(self, intent, entities):
        # Executa tarefa com base na intenção
        if intent in self.tasks:
            return self.tasks[intent](entities)
        return "Intenção não reconhecida"

    def open_website(self, entities):
        url = entities.get("url", "https://www.example.com")
        return f"Abrindo o site: {url}"
    
    def handle_task(intent_data: dict) -> str:
    """Executa ação baseada na intenção detectada."""

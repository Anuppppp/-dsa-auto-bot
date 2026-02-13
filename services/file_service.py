import os
import textwrap
from datetime import datetime
from core.config import Config
from schemas.dsa_schema import DSAResponse

class FileService:
    def __init__(self, config:Config, logger, progress_service):
        self.Config = config
        self.logger = logger
        self.progress_service = progress_service

        os.makedirs(self.Config.GENERATED_FILE, exist_ok=True)


    def create_solution_file(self, day:int, problem_text:str, data:DSAResponse)-> str:
        filename = f"Day_{str(day).zfill(3)}_{self._sanitize_filename(data.title)}.py"
        filepath = os.path.join(self.Config.GENERATED_FILE, filename)

        if os.path.exists(filepath):
            self.logger.warning("File already exists, Skipping creation for idempotency. ")
            return filepath
        
        content = self._build_file_content(day, problem_text, data)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        self.logger.info(f"Creation solution file: {filepath}")
        return filepath
    
    def update_readme(self, day:int, data:DSAResponse):
        entry = f"| {day} | {data.title} | {data.topic} | {data.difficulty} | {data.time_complexity}\n"
        if not os.path.exists(self.Config.README_FILE):
            with open(self.Config.README_FILE, "r+", encoding="utf-8") as f:
                f.write("| Day | Title | Topic | Difficulty | Time Complexity |\n")
                f.write("|-----|--------|--------|------------|----------------|\n")
        
        with open(self.Config.README_FILE, "r+", encoding="utf-8") as f:
            content = f.readlines()

            # Ensure header exists properly
            if len(content) < 2:
                content = [
                    "| Day | Title | Topic | Difficulty | Time Complexity |\n",
                    "|-----|-------|-------|------------|----------------|\n",
                ]

            # Insert after header (latest-first)
            header_end_index = 2
            content.insert(header_end_index, entry)

            f.seek(0)
            f.writelines(content)
            f.truncate()

        self.logger.info("README updated successfully.")

    
    def clear_input(self):
        with open(self.Config.INPUT_FILE, "w", encoding="utf-8",) as f:
            f.write("")

        self.logger.info("cleared input_problem.txt")\
        

    def _build_file_content(self, day: int, problem_text: str, data: DSAResponse) -> str:
        today = datetime.utcnow().strftime("%Y-%m-%d")

        formatted_problem = "\n".join(
            f"# {line.strip()}" for line in problem_text.strip().split("\n")
        )

        cleaned_code = textwrap.dedent(data.code).strip()

        header = f'''"""
    Day {str(day).zfill(3)}
    Title: {data.title}
    Topic: {data.topic}
    Difficulty: {data.difficulty}
    Date: {today}
    """'''

        footer = f"""
    # Time Complexity: {data.time_complexity}
    # Space Complexity: {data.space_complexity}
    """

        return (
                header
                + "\n\n"
                + "# Problem:\n"
                + formatted_problem
                + "\n\n"
                + cleaned_code
                + "\n\n"
                + footer.strip()
                + "\n"
                + "\n"
        )

    def _sanitize_filename(self, name: str) -> str:
        return name.replace(" ", "_").replace("/", "_")
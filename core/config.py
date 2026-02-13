from dataclasses import dataclass
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

@dataclass(frozen=True)
class Config:

    # OpenAI Configuration
    # MODEL_NAME: str ='gpt-4o-mini'
    MODEL_NAME: str = "gemini-2.5-flash"
    TEMPERATURE: float = 0
    MAX_RETRIES: int = 3

    # File Paths 
    INPUT_FILE: str = os.path.join(BASE_DIR, "input_problem.txt")
    PROGRESS_FILE: str = os.path.join(BASE_DIR, "progress.json")
    GENERATED_FILE: str = os.path.join(BASE_DIR, "generated")
    README_FILE: str = os.path.join(BASE_DIR, "README.md")

    # git configuration 
    GIT_BRANCH: str = 'main'

    # Environment
    OPENAI_API_KEY:str = os.getenv("OPENAI_API_KEY", "")
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")

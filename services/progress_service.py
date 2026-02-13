import json 
import os
from core.config import Config

class ProgressiveService:
    def __init__(self, config:Config):
        self.Config = config

    
    def get_next_day(self)-> int:
        if not os.path.exists(self.Config.PROGRESS_FILE):
            return 1

        try:
            with open(self.Config.PROGRESS_FILE, "r", encoding="utf-8") as f:
                content = f.read().strip()

                if not content:
                    return 1

                data = json.loads(content)

            return data.get("last_day", 0) + 1

        except Exception as e:
            # If corrupted or invalid JSON, reset safely
            print(e)
            return 1
    
    def update_day(self, day: int) -> None:
        with open(self.Config.PROGRESS_FILE, "w") as f:
            json.dump({"last_day": day}, f, indent=4)

            
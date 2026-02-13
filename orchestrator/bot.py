import os
import sys

from core.config import Config
from core.logger import get_logger

from services.ai_service import AIService
from services.progress_service import ProgressiveService
from services.file_service import FileService
from services.git_service import GitService


class Bot:
    def __init__(self):
        self.config = Config()
        self.logger = get_logger()

        self.progress_service = ProgressiveService(self.config)
        self.ai_service = AIService(self.config, self.logger)
        self.file_service = FileService(self.config, self.logger, self.progress_service)
        self.git_service = GitService(self.config, self.logger)

    def run(self):
        try:
            self.logger.info("Starting DSA automation bot...")

            if not os.path.exists(self.config.INPUT_FILE):
                self.logger.info("Input file not found. Exiting.")
                return

            with open(self.config.INPUT_FILE, "r", encoding="utf-8") as f:
                problem_text = f.read().strip()

            if not problem_text:
                self.logger.info("Input file is empty. Nothing to process.")
                return

            # Step 1: Generate AI solution
            solution_data = self.ai_service.generate_solution(problem_text)

            # Step 2: Get next day
            next_day = self.progress_service.get_next_day()

            # Step 3: Create file
            filepath = self.file_service.create_solution_file(
                next_day, problem_text, solution_data
            )

            # Step 4: Update README
            self.file_service.update_readme(next_day, solution_data)

            # Step 5: Update progress
            self.progress_service.update_day(next_day)

            # Step 6: Clear input
            self.file_service.clear_input()

            # Step 7: Commit & push
            commit_message = f"feat(dsa): day {next_day} {solution_data.title.lower()}"
            self.git_service.commit_and_push(commit_message)

            self.logger.info("DSA automation completed successfully.")

        except Exception as e:
            self.logger.error(f"Bot execution failed: {e}")
            sys.exit(1)


if __name__ == "__main__":
    bot = Bot()
    bot.run()

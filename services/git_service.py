import subprocess
from core.config import Config



class GitService:
    def __init__(self, config:Config, logger):
        self.Config = config
        self.logger = logger


    def commit_and_push(self, message: str):
        if not self._has_changes():
            self.logger.info("No changes detected. skipping commit. ")
            return
        
        self._run_git_command(["git", "add", "."])
        self._run_git_command(["git", "commit", "-m", message])
        self._run_git_command(["git", "push", "origin", self.Config.GIT_BRANCH])

        self.logger.info("changes commited and pushed successfully.")

    
    def _has_changes(self) -> bool:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True
        )

        return bool(result.stdout.strip())
    
    def _run_git_command(self, command):
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            self.logger.error(f"Git command failed: {' '.join(command)}")
            self.logger.error(result.stderr)
            raise RuntimeError("Git operation failed.")



                      

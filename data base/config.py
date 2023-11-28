import pydantic_settings

class Settings(BaseSettings):
    DB_Host: str
    DP_PORT: int
    DB_USER: str
    DP_PASS: str
    DB_NAME: str

    @property
    def DATABASE_URL (self):
        return f"postgresql+pycopg://{self.DB_USER}:{self.DP_PASS}@{self.DB_Host}:{self.DP_PORT}/{self.DB_NAME}"
import configparser
class Config:
    pass
class DatabaseConfig(Config):
    def load_config(self):

        config = configparser.ConfigParser()
        config.read("db.ini")

        if "DATABASE" not in config:
            print("DATABASE section not found")
            return

        required_keys = ["host", "user", "password"]
        for key in required_keys:
            if key not in config["DATABASE"]:
                print(f"Missing key: {key}")
                return

        print("Database Configuration")
        print("Host:", config["DATABASE"]["host"])
        print("User:", config["DATABASE"]["user"])
        print("Password:", config["DATABASE"]["password"])

db = DatabaseConfig()
db.load_config()
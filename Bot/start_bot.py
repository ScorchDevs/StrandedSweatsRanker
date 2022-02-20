from Main import *
from dotenv import load_dotenv, dotenv_values
from Handlers import *

load_dotenv()
config = dotenv_values(".env")


if __name__=="__main__":
    start_bot(config['DISCORD-TOKEN'])
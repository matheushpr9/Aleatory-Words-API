from dotenv import load_dotenv
import os
from database.Connector import Connector

load_dotenv()

connector = Connector(os.getenv('DATABASE_USER'),  os.getenv('DATABASE_PASSWORD'))
#a = connector.word_exists(connector.set_word("dependendo"), "portuguese")

b =connector.get_item_by_id("portuguese", 1)


print(b)


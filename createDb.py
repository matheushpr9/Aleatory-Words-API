from database.Connector import Connector

connector = Connector("matheushpr9", "bZw23JHQYa9OrXLm")
#a = connector.word_exists(connector.set_word("dependendo"), "portuguese")

b =connector.get_item_by_id("portuguese", 1)


print(b)


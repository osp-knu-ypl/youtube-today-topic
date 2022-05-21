import random

def data_processing(content, price, link):
    processed_data = {}
    processed_data["ID"] = random.randrange(1, 100000000000)
    processed_data["Classification"] = content.split()
    processed_data["Price"] = price
    processed_data["Link"] = link
    return processed_data

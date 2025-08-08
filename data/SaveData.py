import json
import os

data_file = "Data/db.json"

# Fayl mavjud bo'lmasa yoki bo'sh bo'lsa uni yaratish
def init_db():
    if not os.path.exists(data_file) or os.stat(data_file).st_size == 0:
        with open(data_file, "w") as f:
            json.dump({"users": {}}, f, indent=4)



# Ma'lumotni saqlash
def save_user_data(chat_id, key, value):
    with open(data_file, "r") as f:
        data = json.load(f)

    if str(chat_id) not in data["users"]:
        data["users"][str(chat_id)] = {
            "name": "",
            "gender": "",
            "location": {
                "longatute": 0.0,
                "latetute": 0.0
            },
            "number": ""
        }

    if key in ["name", "gender", "number"]:
        data["users"][str(chat_id)][key] = value
    elif key == "location":
        data["users"][str(chat_id)]["location"] = value

    with open(data_file, "w") as f:
        json.dump(data, f, indent=4)

# Foydalanuvchini olish
def get_user_data(chat_id):
    with open(data_file, "r") as f:
        data = json.load(f)
    return data["users"].get(str(chat_id), None)

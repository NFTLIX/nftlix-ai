import json
import io


def dump_to_json(description: str, image_url: str, name: str, token_id: str, effect: str):
    data = {
        "description": description,
        "image_url": image_url,
        "name": name,
        "token_id": token_id,
        "effect": effect
    }

    json_data = json.dumps(data, indent=4)
    return io.BytesIO(json_data.encode('utf-8'))

import json
from collections import defaultdict

document = {
    1 :  "a donut on a glass plate",
    2 :  "only the donut",
    3 : "Listen to the drum music"
}

def create_inverted_index():
    inv_idx = defaultdict(list)
    for _id, text in document.items():
        words = text.split(" ")
        for word in words:
            if _id not in inv_idx[word]:
                inv_idx[word].append(_id)
    return inv_idx


print(json.dumps(dict(create_inverted_index()), indent=4))

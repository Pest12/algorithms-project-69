def search(docs, word):
    result = []
    for doc in docs:
        text = doc['text'].split()
        if word in text:
            result.append(doc['id'])
    return result
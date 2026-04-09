def load_text(filepath):
    with open(filepath, "r") as file:
        return file.read()


def split_into_chunks(text):
    return text.split(".")


def normalize_text(text):
    return text.lower().strip()

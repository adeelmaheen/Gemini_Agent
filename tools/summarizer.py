def summarize_text(text):
    return text[:300] + "..." if len(text) > 300 else text

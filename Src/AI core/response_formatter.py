def format_for_ar(text, max_length=120):
    """
    Formats long AI responses into short AR-friendly text
    """
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."

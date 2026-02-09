def decide_execution(task_type, internet_available=True):
    """
    Decide where to process the task
    """
    if task_type == "heavy_reasoning" and internet_available:
        return "CLOUD"
    elif task_type in ["vision", "basic_qa"]:
        return "LOCAL"
    else:
        return "EDGE"

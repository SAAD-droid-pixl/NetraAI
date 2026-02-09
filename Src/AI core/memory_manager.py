class MemoryManager:
    def __init__(self):
        self.memory = []

    def store(self, item):
        """
        Store a memory item
        """
        self.memory.append(item)

    def recall(self, limit=3):
        """
        Recall last N memory items
        """
        return self.memory[-limit:]

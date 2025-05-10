
class Object:
    id: str
    is_local: bool
    x: int
    y: int
    updated: bool = False
    deleted: bool = False

    def __init__(self, is_local=True):
        self.id = random()
        self.is_local = is_local
        self.objects = []

    def update(self):
        if not self.is_local:
            return
        self.updated = False
        for obj in self.objects[:]:
            if obj.deleted:
                self.objects.remove(obj)
            else:
                obj.update()
        self._update()

    def serialize(self):
        return Event()

    def _update(self):
        pass

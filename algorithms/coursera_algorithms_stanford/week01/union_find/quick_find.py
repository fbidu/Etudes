class QuickFind:
    def __init__(self, size):
        self.id_array = list(range(size))

    def union(self, p, q):
        pid = self.id_array[p]
        qid = self.id_array[q]
        for idx, item in enumerate(self.id_array):
            if item == pid:
                self.id_array[item] = qid

    def connected(self, p, q):
        return self.id_array[p] == self.id_array[q]
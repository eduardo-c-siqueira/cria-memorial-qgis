class DataBaseManager:

    def __init__(self):
        self.db: dict = {} # data must be of type: dict

    def create(self, data, key: str):
        if self.db.keys().__contains__(key):
            print("Erro ao salvar: a chave informada já existe")
        else:
            self.db[key] = data
            print("Dado\"", key, "\" salvo com sucesso!")

    def update(self, key: str, data, attribute=None):
        self.db[key] = data

    def get(self, key: str):
        return self.db.get(key)
from qgis.PyQt import QtWidgets

class DialogBuilder:

    def __init__(self):
        self.pair_dict = {}

    def create_label_qline_pairs(self, key_label_pair: dict):

        for key, value in key_label_pair.items():
            self.pair_dict[key] = {
                "label": QtWidgets.QLabel(value),
                "input": QtWidgets.QLineEdit()
            }

    def add_label_qline_pairs_to_qvbox(self, qvbox: QtWidgets.QVBoxLayout, pairs: dict):
        for pair in self.pair_dict.values():
            qvbox.addWidget(pair["label"])
            qvbox.addWidget(pair["input"])
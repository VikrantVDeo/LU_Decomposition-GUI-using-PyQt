import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QIntValidator
import numpy as np
from scipy.linalg import lu


class LUApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create central widget
        central_widget = QWidget()

        # Create layout for central widget
        layout = QVBoxLayout()

        # Create input widgets
        size_label = QLabel("Enter the size of the square matrix:")
        self.size_input = QLineEdit(self)
        self.size_input.setValidator(QIntValidator())
        self.size_input.setPlaceholderText("Enter an integer")
        layout.addWidget(size_label)
        layout.addWidget(self.size_input)

        matrix_label = QLabel("Enter the matrix elements (separated by spaces):")
        self.matrix_input = QLineEdit(self)
        self.matrix_input.setPlaceholderText("e.g., 1 2 3 4 5 6 7 8 9")
        layout.addWidget(matrix_label)
        layout.addWidget(self.matrix_input)

        # Create button for LU decomposition
        lu_button = QPushButton("Perform LU Decomposition", self)
        lu_button.clicked.connect(self.perform_lu_decomposition)
        layout.addWidget(lu_button)

        # Create label for displaying the result
        self.result_label = QLabel(self)
        layout.addWidget(self.result_label)

        # Set layout for central widget
        central_widget.setLayout(layout)

        # Set central widget for the main window
        self.setCentralWidget(central_widget)

    def perform_lu_decomposition(self):
        size_text = self.size_input.text()
        matrix_text = self.matrix_input.text()

        try:
            size = int(size_text)
            matrix_elements = list(map(float, matrix_text.split()))
            matrix = np.array(matrix_elements).reshape((size, size))

            # Perform LU decomposition
            P, L, U = lu(matrix)

            result_text = f"LU Decomposition:\n\nP:\n{P}\n\nL:\n{L}\n\nU:\n{U}"
            self.result_label.setText(result_text)

        except ValueError as e:
            self.result_label.setText(f"Error: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LUApp()
    window.setGeometry(100, 100, 600, 400)
    window.setWindowTitle("LU Decomposition App by Vikrant Deo")
    window.show()
    sys.exit(app.exec_())

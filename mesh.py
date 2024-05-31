from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtCore import Qt
from OpenGL.GL import *
from OpenGL.GLU import *
import sys
from stl import mesh
import numpy as np

def load_stl(file_path):
    your_mesh = mesh.Mesh.from_file(file_path)
    vertices = your_mesh.vectors.reshape(-1, 3)
    return vertices

class MeshViewer(QOpenGLWidget):
    def __init__(self, vertices, parent=None):
        super(MeshViewer, self).__init__(parent)
        self.vertices = vertices

    def initializeGL(self):
        self.qglClearColor(Qt.black)
        glEnable(GL_DEPTH_TEST)
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointerf(self.vertices)

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, w / h, 1, 1000)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0, 0, -500)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glColor3f(1.0, 1.0, 1.0)
        glDrawArrays(GL_TRIANGLES, 0, len(self.vertices))

class MainWindow(QMainWindow):
    def __init__(self, vertices, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setCentralWidget(MeshViewer(vertices))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    vertices = load_stl('mesh.stl')
    window = MainWindow(vertices)
    window.show()
    sys.exit(app.exec())

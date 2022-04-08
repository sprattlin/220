from graphics import Circle, Line


class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

    def smile(self):
        size = self.head.getRadius()
        center = self.head.getCenter()

        mouth_size = 0.8 * size
        mouth_2 = size / 2.0

        point = center.clone()
        point.move(0, mouth_2 * 1.8)
        point_2 = center.clone()
        point_2.move(-mouth_size / 2, mouth_2)
        point_3 = center.clone()
        point_3.move(mouth_size / 2, mouth_2)

        line_1 = Line(point_2, point)
        line_2 = Line(point_3, point)
        line_1.draw(self.window)
        line_2.draw(self.window)

    def shock(self):
        size = self.head.getRadius()
        mouth_create = 0.20 * size
        mouth_mid = self.mouth.getCenter()
        mouth_shock = Circle(mouth_mid, mouth_create)
        self.mouth.undraw()
        self.mouth = mouth_shock
        self.mouth.draw(self.window)

    def wink(self):
        center = self.head.getCenter()
        size = self.head.getRadius()
        eye_create = size / 3.0
        point = center.clone()
        point.move(-eye_create / 1.6, - eye_create)
        point_2 = center.clone()
        point_2.move(eye_create / 2, - eye_create)
        eye_shape = Line(point, point_2)
        eye_shape.move(- eye_create, 0)
        self.left_eye.undraw()
        self.left_eye = eye_shape
        eye_shape.draw(self.window)
        self.smile(face)

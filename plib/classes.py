import Rhino as rh
import math
import itertools
import operator
import inspect

#https://contextmachine.jetbrains.space/oauth/auth/invite/2a13e0d73cadfb859b2b9f0e6a275549


class DetailBuild:
    def __init__(self):
        pass


class Pt:

    def __init__(self, vector):
        self.vector = vector
        self.point3d = rh.Geometry.Point3d(self.vector[0], self.vector[1], self.vector[2])

    def __str__(self):
        return 'Pt(point): {}'.format(self.vector)

    def __add__(self, other):
        return Pt(list(itertools.starmap(operator.add, zip(self.vector, other.vector))))

    def __sub__(self, other):
        return Pt(list(itertools.starmap(operator.sub, zip(self.vector, other.vector))))

    def __eq__(self, other):
        return Pt(list(itertools.starmap(operator.eq, zip(self.vector, other.vector))))

    def distance(self, other):

        x1 = self.vector[0]
        y1 = self.vector[1]
        z1 = self.vector[2]
        x2 = other.vector[0]
        y2 = other.vector[1]
        z2 = other.vector[2]
        d = 0.0
        d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
        return d




class Axis:
    def __init__(self, end, start):
        self.start = start
        self.end = end
        self.mtrx = [start.vector, end.vector]
        self.list = start.vector.extend(end.vector)
        self.len = self.start.distance(self.end)
        self.line = self.get_line()
    def __str__(self):
        return 'Axis:\n {}\n {}'.format(self.start.vector, self.end.vector)

    def __add__(self, other):
        return Pt(list(itertools.starmap(operator.add, zip(self.list, other.list))))

    def __sub__(self, other):
        return Pt(list(itertools.starmap(operator.sub, zip(self.list, other.list))))

    def __eq__(self, other):
        return Pt(list(itertools.starmap(operator.eq, zip(self.list, other.list))))

    def get_line(self):
        rh.Geometry.Line(self.start.point3d)


class P1:
    def __init__(self):
        pass

class P2:
    def __init__(self):
        pass

class K1:
    def __init__(self):
        pass

class Rig:
    def __init__(self):
        pass


__all__ = [DetailBuild, Pt, Axis, P1, P2, K1, Rig]

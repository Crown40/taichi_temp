import taichi as ti
from .configuration import Configuration

class FEMConfiguration(Configuration):
    # 'triangle', 'tetrahedron'
    element_type='triangle'
    element_verticesCount=3

    def __init__(self, element_type='triangle', dim=3, *args, **kwargs):
        self.dim=dim
        self.vecD_type=ti.types.vector(n=self.dim, dtype=self.ftype)
        self.matD_type=ti.types.matrix(n=self.dim,m=self.dim, dtype=self.ftype)
        #
        if element_type=='tetrahedron':
            self.element_type='tetrahedron'
            self.element_verticesCount=4
        else: # 'triangle'
            self.element_type='triangle'
            self.element_verticesCount=3
        #



def initialization(element_type='triangle'):
    return FEMConfiguration(element_type)

#configuration=FEMConfiguration(element_type)
configuration=initialization()


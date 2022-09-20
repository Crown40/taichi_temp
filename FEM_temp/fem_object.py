import taichi as ti
import meshio
from initialization import configuration


@ti.dataclass
class FEMvertexData:
    #mass: ti.f32
    position: ti.types.vector(n=configuration.dim, dtype=configuration.ftype)
    velocity: ti.types.vector(n=configuration.dim, dtype=configuration.ftype)
    acceleration: ti.types.vector(n=configuration.dim, dtype=configuration.ftype)


@ti.dataclass
class FEMelementData:
    vertices_IDs: ti.types.vector(n=configuration.element_verticesCount, dtype=configuration.ftype)


@ti.data_oriented
class FEMobject:
    def __init__(self, vertex_count=3, element_count=1,*args, **kwargs):
        #
        self.vertex_count=vertex_count
        self.element_count=element_count
        #
        self.vertices_data=ti.field(dtype=FEMvertexData, shape=self.vertex_count)
        self.elements_data=ti.field(dtype=FEMelementData, shape=self.element_count)
        # element_type: 'triangle', 'tetrahedron'
        #return super().__init__(*args, **kwargs)

    @staticmethod
    def loadMeshFromFile(file_name:str):
        
        pass

if __name__ == '__main__':
    #FEMobject.readFromFile('cube.obj')
    #FEMobject.readFromFile('cube.ply')
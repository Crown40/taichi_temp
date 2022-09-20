import taichi as ti
#import meshio
from .initialization import configuration


@ti.dataclass
class FEMvertexData:
    #mass: configuration.ftype
    position: configuration.vecD_type
    velocity: configuration.vecD_type
    acceleration: configuration.vecD_type


@ti.dataclass
class FEMelementData:
    vertices_IDs: ti.types.vector(n=configuration.element_verticesCount, dtype=configuration.ftype)


@ti.data_oriented
class FEMobject:
    def __init__(self, file_name=None,vertex_count=None, element_count=None, vertices_data:FEMvertexData.field =None, elements_data:FEMelementData.field =None,*args, **kwargs):
        #
        if file_name is not None:
            dot_index=-1
            for i in range(len(file_name)-1,-1,-1):
                if file_name[i]=='.':
                    dot_index=i
                if file_name[i]=='/':
                    break
            if dot_index>-1:
                file_format=file_name[dot_index+1:]
                #meshes=meshio.read(filename=file_name, file_format=file_format)
                #
            else:
                msg='file is not found or file_name is wrong!'
                raise FileNotFoundError(msg)
            #
        #
        elif (vertex_count is not None) and (element_count is not None) and (vertices_data is not None) and (elements_data is not None):
            #
            self.vertex_count=vertex_count
            self.element_count=element_count
            #
            self.vertices_data=vertices_data
            self.elements_data=elements_data
            # element_type: 'triangle', 'tetrahedron'
            #return super().__init__(*args, **kwargs)



if __name__ == '__main__':
    pass
    #fem_object=FEMobject(file_name='/models/bunny/bunny.obj')

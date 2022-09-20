from configuration import Configuration

class FEMConfiguration(Configuration):
    # 'triangle', 'tetrahedron'
    element_type='triangle'
    element_verticesCount=3

    def __init__(self, element_type='triangle'):
        #
        if element_type=='tetrahedron':
            self.element_type='tetrahedron'
            self.element_verticesCount=4
        else: # 'triangle'
            self.element_type='triangle'
            self.element_verticesCount=3
        #

#configuration=FEMConfiguration(element_type)
configuration=None
initialization()

def initialization(element_type='triangle'):
    configuration=FEMConfiguration(element_type)
    pass


import taichi as ti

class Configuration:
    ftype,itype=ti.f32, ti.i32
    dim, dt, sub_steps, steps= 2, 1/4096, 1, -1
    epsilon=1e-9
    low_bound,high_bound=epsilon, 1.0-epsilon



#configuration=Configuration()

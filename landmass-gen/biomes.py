biome = {
        'tropic': {
            'landscape':(116,180,114),
            'vegetation':(207,246,176),
            'mountain':(144,118,101),
            'water':(179,234,232),
            'dist':(0.68,0.12,0.18,0.12)
        },
        'temperate': {
            'landscape':(58,73,40),
            'vegetation':(75,105,60),
            'mountain':(144,122,72),
            'water':(207,246,176),
            'dist':(0.68,0.12,0.18,0.12)
        },
        'desert': {
            'landscape':(204,166,113),
            'vegetation':(242,203,138),
            'mountain':(103,76,14),
            'water':(179,234,232),
            'dist':(0.9,0.06,0.03,0.01)
        },
        'tundra': {
            'landscape':(233,239,248),
            'vegetation':(170,170,173),
            'mountain':(216,222,223),
            'water':(120,173,206),
            'dist':(0.75,0.1,0.12,0.03)
        },
        'grassland': {
            'landscape':(22,184,90),
            'vegetation':(120,238,140),
            'mountain':(119,191,128),
            'water':(102,216,162),
            'dist':(0.6,0.2,0.1,0.1)
        },
        'savanna': {
            'landscape':(208,121,68),
            'vegetation':(240,227,206),
            'mountain':(167,106,58),
            'water':(101,126,150),
            'dist':(0.78,0.12,0.05,0.05)
        },
        'none':None
}


def get_biome(b):
    if b == 'tropic':
        return biome['tropic']
    elif b == 'temperate':
        return biome['temperate']
    elif b == 'desert':
        return biome['desert']
    elif b == 'tundra':
        return biome['tundra']
    elif b == 'grassland':
        return biome['grassland']
    elif b == 'savanna':
        return biome['savanna']
    else:
        return biome['none']


class Biome:

    def __init__(self,biome):
        self.landscape_color = biome['landscape']
        self.vegetation_color = biome['vegetation']
        self.mountain_color = biome['mountain']
        self.water_color = biome['water']
        self.land_dist,self.veg_dist,self.mount_dist,self.water_dist = biome['dist']


    def get_landscape_color(self):
        return self.landscape_color


    def get_vegetation_color(self):
        return self.vegetation_color


    def get_mountain_color(self):
        return self.mountain_color


    def get_water_color(self):
        return self.water_color


    def get_landscape_distrib(self):
        return self.land_dist


    def get_vegetation_distrib(self):
        return self.veg_dist


    def get_mountain_distrib(self):
        return self.mount_dist


    def get_water_distrib(self):
        return self.water_dist

'Demonstrate how to implement the various choices that can be made for multiple inheritance'

class Automobile:
    trunk = []

    sw = 'change angle of front tires relative to centerline'

class Airplane:
    wings = []

    sw = 'increases or decrease camber on the wing by moving ailerons up or down'

class FlyingCar(Automobile, Airplane):

    def sw(self):
        switch = self.flight_status()
        if switch:
            Automobile.sw(self)
        else:
            Airplane.sw(self)

        # fly-by-wire
        wa, aa = self.figure_out_how_to_turn()
        Automobile.sw(self, wa)        
        Airplane.sw(self, aa)
'''

1. Do car SW only.
2. Do airplane SW only.
3. Do both.
4. User switch
5. Automated switch
6. Fly by wire

'''

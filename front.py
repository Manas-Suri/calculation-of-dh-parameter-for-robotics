import math
import numpy

class Number:
        def numberstodirection(self,direct,elf,value_of_a,value_of_b,value_of_c,angle):
        # instead of using switch case,if case is used in python
            self.angle_1 = int(angle)
            if direct == 3:
                # these are angles for rotation along z axis
                self.cos_a = round(math.cos(math.radians(self.angle_1)),2)
                self.sin_a = round(math.sin(math.radians(self.angle_1)),2)
                # these are for values in x,y,z axis respectively
                self.a_Qz = value_of_a
                self.b_Qz = value_of_b
                self.c_Qz = value_of_c
                # For Translation and rotation along Z axis
                self.Qz = [[self.cos_a, -self.sin_a, 0, self.a_Qz],
                      [self.sin_a, self.cos_a, 0, self.b_Qz],
                      [0, 0, 1, self.c_Qz],
                      [0, 0, 0, 1]]
                elf = self.Qz
            # For Translation and rotation along Y axis
            if direct == 2:
                # angle_2 = 0
                # these are angles for rotation along y axis
                self.cos_b = round(math.cos(math.radians(self.angle_1)),2)
                self.sin_b = round(math.sin(math.radians(self.angle_1)),2)
                # these are for values in x,y,z axis respectively
                self.a_Qyp = value_of_a
                self.b_Qyp = value_of_b
                self.c_Qyp = value_of_c

                self.Qy = [[self.cos_b, 0, self.sin_b, self.a_Qyp],
                      [0, 1, 0, self.b_Qyp],
                      [-self.sin_b, 0, self.cos_b, self.c_Qyp],
                      [0, 0, 0, 1]]
                elf = self.Qy
            # For Translation and rotation along Y axis
            if direct == 1:
                # these are angles for rotation along z axis
                self.cos_c = round(math.cos(self.angle_1),2)
                self.sin_c = round(math.sin(self.angle_1),2)
                # these are for values in x,y,z axis respectively
                self.a_Qx = value_of_a
                self.b_Qx = value_of_b
                self.c_Qx = value_of_c

                Qx = [[1, 0, 0, self.a_Qx],
                      [0, self.cos_c, -self.sin_c, self.b_Qx],
                      [0, self.sin_c, self.cos_c, self.c_Qx],
                      [0, 0, 0, 1]]
                elf = Qx

            return elf


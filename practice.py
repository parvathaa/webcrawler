class Gym:
    def __init__ (self, day, musclegroup):
        self.day = day
        self.musclegroup = musclegroup

    def abc (self):
        print (f"Today is {self.day} and I am working on {self.musclegroup}.")

gym1 = Gym("Mon", "lower body")
gym2 = Gym("Wed", "upper body")

gym1.abc()
gym2.abc()
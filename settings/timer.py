
class Timer():
    def __init__(self):
        self.timer_10 = True
        self.timer_9 = True
        self.timer_8 = True
        self.timer_7 = True
        self.timer_6 = True
        self.timer_5 = True
        self.timer_4 = True
        self.timer_3 = True
        self.timer_2 = True
        self.timer_1 = True

    def timeCheck(self, sounds, playTime):
        if playTime == 90:
            return 1

        elif 90 - playTime == 10 and self.timer_10:
            sounds.timeRunning.play()
            self.timer_10 = False

        elif 90 - playTime == 9 and self.timer_9:
            sounds.timeRunning.play()
            self.timer_9 = False

        elif 90 - playTime == 8 and self.timer_8:
            sounds.timeRunning.play()
            self.timer_8 = False

        elif 90 - playTime == 7 and self.timer_7:
            sounds.timeRunning.play()
            self.timer_7 = False

        elif 90 - playTime == 6 and self.timer_6:
            sounds.timeRunning.play()
            self.timer_6 = False

        elif 90 - playTime == 5 and self.timer_5:
            sounds.timeRunning.play()
            self.timer_5 = False

        elif 90 - playTime == 4 and self.timer_4:
            sounds.timeRunning.play()
            self.timer_4 = False

        elif 90 - playTime == 3 and self.timer_3:
            sounds.timeRunning.play()
            self.timer_3 = False

        elif 90 - playTime == 2 and self.timer_2:
            sounds.timeRunning.play()
            self.timer_2 = False

        elif 90 - playTime == 1 and self.timer_1:
            sounds.timeRunning.play()
            self.timer_1 = False

# src/agents/AlarmTrigger.py

import time

class AlarmTrigger:
    def __init__(self):
        self.is_triggered = False

    def trigger_alarm(self):
        self.is_triggered = True
        print("Alarm triggered!")
        return self.is_triggered


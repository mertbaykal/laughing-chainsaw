# src/agents/AlarmLogger.py

import time

class AlarmLogger:
    def log(self, is_triggered):
        if is_triggered:
            with open("alarm_log.txt", "a") as log_file:
                log_file.write("Alarm triggered at time: {}\n".format(time.ctime()))

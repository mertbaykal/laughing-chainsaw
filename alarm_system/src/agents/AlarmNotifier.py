# src/agents/AlarmNotifier.py

class AlarmNotifier:
    def notify(self, is_triggered):
        if is_triggered:
            print("Notification: Alarm has been triggered!")

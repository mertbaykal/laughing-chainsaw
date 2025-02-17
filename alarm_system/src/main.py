# src/main.py

from agents.AlarmTrigger import AlarmTrigger
from agents.AlarmNotifier import AlarmNotifier
from agents.AlarmLogger import AlarmLogger
from agents.AlarmReseter import AlarmReseter

def main():
    # Create instances of each agent
    trigger = AlarmTrigger()
    notifier = AlarmNotifier()
    logger = AlarmLogger()
    reseter = AlarmReseter()
    
    # Trigger the alarm
    is_triggered = trigger.trigger_alarm()
    
    # Notify the user
    notifier.notify(is_triggered)
    
    # Log the event
    logger.log(is_triggered)
    
    # Reset the alarm
    is_triggered = reseter.reset()

if __name__ == "__main__":
    main()

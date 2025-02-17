# src/main.py

from agents.AlarmTrigger import AlarmTrigger
from agents.AlarmNotifier import AlarmNotifier
from agents.AlarmLogger import AlarmLogger
from agents.AlarmReseter import AlarmReseter

def main():
    # Ajanları başlat
    trigger = AlarmTrigger()
    notifier = AlarmNotifier()
    logger = AlarmLogger()
    reseter = AlarmReseter()
    
    # Alarmı tetikle
    is_triggered = trigger.trigger_alarm()
    
    # Bildirim gönder
    notifier.notify(is_triggered)
    
    # Olayı kaydet
    logger.log(is_triggered)
    
    # Alarmı sıfırla
    is_triggered = reseter.reset()

if __name__ == "__main__":
    main()

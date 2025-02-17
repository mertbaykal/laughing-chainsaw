# tests/test_alarm_notifier.py

from src.agents.AlarmNotifier import AlarmNotifier

def test_alarm_notify():
    notifier = AlarmNotifier()
    notifier.notify(True)
    # Eğer bu satır çalışıyorsa, çıktı alacağınız için test başarılı demektir.

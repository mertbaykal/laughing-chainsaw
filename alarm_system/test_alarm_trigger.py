# tests/test_alarm_trigger.py

from src.agents.AlarmTrigger import AlarmTrigger

def test_alarm_trigger():
    trigger = AlarmTrigger()
    assert trigger.trigger_alarm() == True


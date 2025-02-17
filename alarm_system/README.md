# Alarm System Project

## Overview
This project simulates a simple alarm system with Event-Driven Programming (EDP). The system consists of 4 agents:
1. AlarmTrigger: Triggers the alarm at a specific time.
2. AlarmNotifier: Sends notifications when the alarm is triggered.
3. AlarmLogger: Logs the alarm event to a file.
4. AlarmReseter: Resets the alarm to prepare for the next trigger.

## How to Run
1. Clone the repository.
2. Navigate to the `src` folder.
3. Run the `main.py` file.

### Running the Python Program:

Navigate to the project root directory and use the following command to run the `src/main.py` file:

```bash
python src/main.py
```

### Running the Tests:

To run the test files, you can use the following commands:

```bash
python -m unittest tests/test_alarm_trigger.py
python -m unittest tests/test_alarm_notifier.py
```

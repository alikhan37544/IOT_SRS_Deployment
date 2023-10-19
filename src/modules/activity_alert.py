# activity_alert.py

class ActivityAlertSystem:
    def __init__(self):
        self.alert_subscribers = []

    def subscribe(self, subscriber):
        self.alert_subscribers.append(subscriber)

    def notify_subscribers(self, message):
        for subscriber in self.alert_subscribers:
            subscriber.notify(message)

# Example subscriber
class AlertSubscriber:
    def __init__(self, name):
        self.name = name

    def notify(self, message):
        print(f"{self.name} received alert: {message}")

# Example usage
if __name__ == "__main__":
    activity_alert_system = ActivityAlertSystem()

    # Creating subscribers
    subscriber1 = AlertSubscriber("Subscriber 1")
    subscriber2 = AlertSubscriber("Subscriber 2")

    # Subscribing subscribers to the alert system
    activity_alert_system.subscribe(subscriber1)
    activity_alert_system.subscribe(subscriber2)

    # Notifying subscribers
    activity_alert_system.notify_subscribers("Activity detected in Room 1")

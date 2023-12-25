import threading
import time
import queue
import random
from discord_webhook import DiscordWebhook, DiscordEmbed
import datetime

class Classifier:
    def __init__(self, name, queue_size=30):
        self.name = name
        self.queue = queue.Queue(maxsize=queue_size)
        self.semaphore = threading.Semaphore(1)  # Semaphore to control access to the classifier
        self.in_failure = False  # Flag to indicate if the classifier is in failure

    def process_invoices(self):
        while True:
            invoices = self.queue.get()
            if invoices is None:
                break  # Exit the loop if None is encountered in the queue

            if not self.in_failure:
                print(f"{self.name} processing invoices: {invoices}")
                time.sleep(random.uniform(0.5, 1.5))  # Simulate processing time
            else:
                print(f"{self.name} is in failure. Redirecting invoices to the backup classifier.")

    def start_processing(self):
        self.processing_thread = threading.Thread(target=self.process_invoices, name=f"{self.name}_Thread")
        self.processing_thread.start()


class AlertSystem:
    def __init__(self):
        self.alert_semaphore = threading.Semaphore(1)

    def send_alert(self, message):
        with self.alert_semaphore:
            print(f"Failure in {message} classifier. Please investigate.")
            nome = 'Erro obtido em'
            agora = datetime.datetime.now()
            formato_personalizado = "%Y-%m-%d %H:%M:%S"
            data = agora.strftime(formato_personalizado)


            webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1173468933488123954/eRl4pxQsICmOLnV_fxXON9MLFegUJDYwHpUyefGDQhR9rsmE14hnN22VFEQO7qmW3wpk')
            embed = DiscordEmbed(title='ALERT', description='%s em %s' %(nome, data), color='03b2f8')
            embed.set_author(name='System Classifier Meta', icon_url='https://cdn-icons-png.flaticon.com/512/6033/6033716.png')
            embed.add_embed_field(name='Failure in',value=message)
            embed.add_embed_field(name='Instance reservation',value='active')
            embed.add_embed_field(name='Last activity',value='Invoice process')

            webhook.add_embed(embed)
            response = webhook.execute(embed)


def simulate_classifier(classifier, invoices):
    print(f"Sending invoices to {classifier.name} classifier: {invoices}")
    classifier.queue.put(invoices)

def simulate_failure(classifier, alert_system, duration):
    print(f"Simulating failure in {classifier.name} classifier.")
    classifier.in_failure = True
    alert_system.send_alert(f"{classifier.name}")
    time.sleep(duration)  # Simulate the duration of the failure
    classifier.in_failure = False
    print(f"{classifier.name} failure resolved. Resuming normal operation.")

def main():
    classifier1 = Classifier("Classifier1")
    classifier2 = Classifier("Classifier2")
    alert_system = AlertSystem()

    classifier1.start_processing()
    classifier2.start_processing()

    # Simulate sending invoices to classifiers
    for i in range(1, 101):
        simulate_classifier(classifier1 if i % 2 == 1 else classifier2, f"Invoice_{i}")

        if i % 30 == 0:
            # Simulate the time it takes to fill the queue
            time.sleep(2)
            # Simulate failure in Classifier1 for 5 seconds
            simulate_failure(classifier1, alert_system, duration=5)

    # Wait for processing threads to finish
    classifier1.queue.put(None)
    classifier2.queue.put(None)
    classifier1.processing_thread.join()
    classifier2.processing_thread.join()

if __name__ == "__main__":
    main()
import time
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import transaction

# Signal for Question 1: Synchronous Signal
@receiver(post_save, sender=User)
def synchronous_signal(sender, **kwargs):
    print("Signal received")
    time.sleep(5)  # Simulate delay
    print("Signal processing completed")


# Signal for Question 2: Check if Signal Runs in the Same Thread
@receiver(post_save, sender=User)
def thread_signal(sender, **kwargs):
    print(f"Signal received in thread: {threading.current_thread().name}")


# Signal for Question 3: Signal in the Same Transaction
@receiver(post_save, sender=User)
def transaction_signal(sender, **kwargs):
    print("Signal received")
    raise Exception("Simulate failure in signal")

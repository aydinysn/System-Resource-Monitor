import platform


class NotificationSystem:
    def __init__(self):
        self.system = platform.system()
        
        if self.system == "Windows":
            try:
                from win10toast import ToastNotifier
                self.toaster = ToastNotifier()
            except ImportError:
                self.toaster = None
        elif self.system == "Linux":
            try:
                import notify2
                notify2.init("System Monitor")
                self.notifier = notify2
            except ImportError:
                self.notifier = None

    def send(self, message):
        print(f"NOTIFICATION: {message}")  
        
        try:
            if self.system == "Windows" and self.toaster:
                self.toaster.show_toast("System Monitor", 
                                      message,
                                      duration=5,
                                      threaded=True)
            
            elif self.system == "Linux" and self.notifier:
                self.notifier.Notification("System Monitor", message).show()
                
        except Exception as e:
            print(f"Notification error: {str(e)}")


_notifier = NotificationSystem()

def send_notification(message):
    _notifier.send(message)




class Subscriber:
    def notify(self, event):
        pass


class Publisher:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, sub: Subscriber):
        self.subscribers.append(sub)

    def notify(self, event):
        for sub in self.subscribers:
            sub.notify(event)


sub1 = Subscriber()
sub2 = Subscriber()
sub3 = Subscriber()

pub = Publisher()
pub.subscribe(sub1)
pub.subscribe(sub2)
pub.subscribe(sub3)

pub.notify("NEW VIDEO")

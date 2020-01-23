class Linked_list:

    def __init__(self):
        self.head = None

    def list_search(self, k):
        x = self.head
        while x is not None and not (x.key == k):
            x = x.next
        #Denne metode skal returnere None
        # hvis k ikke findes i listen.
        # eller skal den returnere x
        return x

    def list_insert(self, k):
        k.next = self.head
        if not (self.head == None):
            self.head.prev = k
        self.head = k
        k.prev = None

    def list_delete(self, x):
        #Denne linje sammenkæder de to elementer omkring x
        if not (x.prev == None):
            x.prev.next = x.next
        else:
            #Hvis x ikke har en prev, må den være vores head.
            #Derfor sætter vi head til at være den x.next
            self.head = x.next
        #Hvis x har en next, skal dens prev sættes til x's gamle prev,
        if not (x.next == None):
            x.next.prev = x.prev

    def print_list(self):
        x = self.head
        while not (x is None):
            print(x.key)
            x = x.next

class List_element:

    def __init__(self, k):
        self.next = None
        self.prev = None
        self.key = k

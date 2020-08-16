#  Hint:  You may not need all of these.  Remove the unused functions.

# input: list of tickets, each with source and destination attributes
# output: array of strings with the correct ordered route
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # store tickets in dict
    # key: ticket source
    # value: ticket destination
    ticket_dict = {ticket.source: ticket.destination for ticket in tickets}
    route = [None] * length
    # the first ticket will have a source of "NONE"
    route[0] = ticket_dict["NONE"]
    # for the remaining tickets, route[i] = ticket_dict[i-1]
    for i in range(length - 1):
        route[i+1] = ticket_dict[route[i]]

    return route


# test
ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
           ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

print(reconstruct_trip(tickets, 10))

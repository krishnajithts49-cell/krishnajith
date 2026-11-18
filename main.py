from ticketscript import Ticket, StudentsTicket,GroupTickets


def show_all(tickets):
    for t in tickets:
        print(f"{t.get_name()}:rs {t.price():.2f}")


def main():
    tickets=[Ticket("Concert",200),StudentTicket("Museum",150)
             show_all(ticket_list)

main()             

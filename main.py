"""
Entry point for the Personal Assistant application.

Responsibilities:
- Display the welcome message and main input loop.
- Parse user input using `parse_input()` from `assistant.core`.
- Route commands to the appropriate functions (contacts or notes modules).
- Manage application lifecycle (start, exit, etc.).
"""
from assistant.contacts.address_book import AddressBook
from assistant.core import parse_input
from assistant.contacts.commands import register_contact_commands
from assistant.notes.commands import register_note_commands
from assistant.commands_enum import Command, COMMAND_HELP
from assistant.notes.notebook import Notebook


    
COMMANDS = {
    Command.Contacts.ADD: None,
    Command.Contacts.CHANGE: None,
    Command.Contacts.PHONE: None,
    Command.Contacts.ALL: None,
    Command.Contacts.ADD_BIRTHDAY: None,
    Command.Contacts.SHOW_BIRTHDAY: None,
    Command.Contacts.BIRTHDAYS: None,
    # додав команду пошуку контактів до реєстру команд
    Command.Contacts.SEARCH: None,
    Command.Notes.ADD_NOTE: None,
    Command.Notes.EDIT_NOTE: None,
    Command.Notes.DELETE_NOTE: None,
    Command.Notes.SEARCH_NOTE: None,
    Command.Notes.SHOW_NOTES: None,
}


def show_help():
    """Display help with all commands, parameters, and descriptions."""
    print("\n" + "=" * 70)
    print(" Personal Assistant - Available Commands")
    print("=" * 70)

    print("\n Contact Management:")
    for cmd in Command.Contacts:
        help_info = COMMAND_HELP[cmd]
        print(help_info.format(cmd.value, width=45))

    print("\n📝 Note Management:")
    for cmd in Command.Notes:
        help_info = COMMAND_HELP[cmd]
        print(help_info.format(cmd.value, width=45))

    print("\n General:")
    for cmd in Command.General:
        help_info = COMMAND_HELP[cmd]
        print(help_info.format(cmd.value, width=45))

    print("\n" + "=" * 70)
    print("Legend:")
    print("  <parameter>  Required parameter")
    print("  [parameter]  Optional parameter")
    print("=" * 70 + "\n")


def main():
    # додав привітання та список команд при старті
    print("Ласкаво просимо до Персонального помічника!")
    print("Доступні команди:")
    
    # виведення всіх доступних команд
    for command in Command:
        print(f"  {command.value}: {COMMAND_HELP[command].description}")
    
    print("\nПочніть роботу ввівши команду...")

    contacts = AddressBook()
    notes = Notebook()

    register_contact_commands(COMMANDS)
    register_note_commands(COMMANDS)

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command == Command.General.CLOSE:
            print("Good bye!")
            break

        elif command == Command.General.HELLO:
            print("How can I help you?")
            continue

        elif command == Command.General.HELP:
            show_help()
            continue

        if command in COMMANDS:
            handler = COMMANDS[command]
            if handler is None:
                print("⚠️ Command not implemented yet.")
            else:
                if isinstance(command, Command.Contacts):
                    print(handler(args, contacts))
                elif isinstance(command, Command.Notes):
                    print(handler(args, notes))
        else:
            print("Invalid command.")


if __name__ == '__main__':
    main()
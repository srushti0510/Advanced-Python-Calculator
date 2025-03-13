# app/commands.py
import cmd
from app.arithmetic import add, subtract, multiply, divide
from app.history import load_history, save_history, print_history, clear_history
from app.plugins import list_plugins, load_plugin  # Import the functions from plugins.py

class CalculatorREPL(cmd.Cmd):
    prompt = 'calc> '

    def preloop(self):
        """Display a welcome message and show the main menu."""
        self.display_menu()

    def display_menu(self):
        """Display the main menu options."""
        print("\nWelcome to the Advanced Python Calculator!\n")
        print("Select an option from the menu below:")
        print("1. Basic Arithmetic Operations")
        print("2. View History")
        print("3. Advanced Features")  # "Advanced Features" includes plugins
        print("4. Clear History")
        print("5. Exit\n")

    def default(self, line):
        """Override the default behavior to handle menu choices."""
        if line == '1':
            self.show_arithmetic_menu()  # Show arithmetic menu
        elif line == '2':
            self.view_history()
        elif line == '3':
            self.load_plugins()  # Allow loading advanced features (plugins)
        elif line == '4':
            clear_history()
            print("History cleared.")
            self.display_menu()
        elif line == '5':
            print("Exiting calculator. Thank you for using!")
            return True
        else:
            print("Invalid choice, please select a valid option.")
            self.display_menu()

    def show_arithmetic_menu(self):
        """Display the arithmetic operations menu."""
        print("\nSelect an arithmetic operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Back to Main Menu")

        operation = input("Choose an operation (1-5): ")
        if operation == '1':
            self.do_add(input("Enter two numbers separated by space: "))
        elif operation == '2':
            self.do_subtract(input("Enter two numbers separated by space: "))
        elif operation == '3':
            self.do_multiply(input("Enter two numbers separated by space: "))
        elif operation == '4':
            self.do_divide(input("Enter two numbers separated by space: "))
        elif operation == '5':
            self.display_menu()
        else:
            print("Invalid choice, going back to main menu.")
            self.display_menu()

    def do_add(self, arg):
        """Perform addition operation."""
        try:
            x, y = map(float, arg.split())
            result = add(x, y)
            print(f"Result: {result}")
            save_history('add', x, y, result)
        except Exception as e:
            print(f"Error: {e}")
        self.display_menu()

    def do_subtract(self, arg):
        """Perform subtraction operation."""
        try:
            x, y = map(float, arg.split())
            result = subtract(x, y)
            print(f"Result: {result}")
            save_history('subtract', x, y, result)
        except Exception as e:
            print(f"Error: {e}")
        self.display_menu()

    def do_multiply(self, arg):
        """Perform multiplication operation."""
        try:
            x, y = map(float, arg.split())
            result = multiply(x, y)
            print(f"Result: {result}")
            save_history('multiply', x, y, result)
        except Exception as e:
            print(f"Error: {e}")
        self.display_menu()

    def do_divide(self, arg):
        """Perform division operation."""
        try:
            x, y = map(float, arg.split())
            result = divide(x, y)
            print(f"Result: {result}")
            save_history('divide', x, y, result)
        except Exception as e:
            print(f"Error: {e}")
        self.display_menu()

    def view_history(self):
        """Display the calculation history."""
        print("\nCalculation History:")
        print_history()
        self.display_menu()

    def do_exit(self, arg):
        """Exit the calculator."""
        print("Thank you for using the Advanced Python Calculator!")
        return True

    def load_plugins(self):
        """Display available plugins and allow the user to select one."""
        print("\nThese are the advanced features (plugins) you can use:")
        plugins_list = list_plugins()  # Use the imported function
        if not plugins_list:
            print("No advanced features available.")
        else:
            for idx, plugin in enumerate(plugins_list, 1):
                # Provide a brief description of the plugin
                print(f"{idx}. {plugin} - {self.get_plugin_description(plugin)}")

            plugin_choice = input("Enter the number of the advanced feature you want to use: ")
            try:
                plugin_name = plugins_list[int(plugin_choice) - 1]
                load_plugin(plugin_name)  # Use the imported function
            except (IndexError, ValueError):
                print("Invalid plugin choice.")
        self.display_menu()

    def get_plugin_description(self, plugin_name):
        """Provide a description for the plugin."""
        descriptions = {
            'square_root': 'Calculates the square root of a given number.',
            'factorial': 'Calculates the factorial of a given number.',
            # Add descriptions for other plugins here
        }
        return descriptions.get(plugin_name, "No description available.")
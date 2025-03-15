# Advanced Calculator

## Table of Contents
- [Project Overview](#project-overview)
- [Core Functionalities](#core-functionalities)
- [Plugin System](#plugin-system)
- [Calculation History Management](#calculation-history-management)
- [Professional Logging Practices](#professional-logging-practices)
- [Advanced Data Handling with Pandas](#advanced-data-handling-with-pandas)
- [Design Patterns for Scalable Architecture](#design-patterns-for-scalable-architecture)
- [Testing and Code Quality](#testing-and-code-quality)
- [Version Control Best Practices](#version-control-best-practices)
- [Documentation](#documentation)
- [Video Showcase](#video-showcase)

## Project Overview
This advanced calculator provides a command-line interface (REPL) that supports basic arithmetic operations, manages calculation history, and allows for plugin integration. It utilizes **Pandas** for efficient data management and includes professional logging practices to track application behavior.

## Core Functionalities
The application features a **REPL** that enables users to:

- Execute arithmetic operations: addition, subtraction, multiplication, and division.
- Manage calculation history through commands to show, save, clear, and delete history entries.
- Access extended functionalities via dynamically loaded plugins.

## Plugin System
A flexible plugin system has been implemented to facilitate seamless integration of new commands or features. This allows developers to create plugins that can be dynamically loaded without altering the core application code. The application includes a "Advanced Features" option in the REPL to list all available plugin commands, enhancing user discoverability.

## Calculation History Management
**Pandas** is utilized to manage calculation history effectively. Users can:

- Load and display history from CSV file.
- Save the current history to CSV file.
- Clear the current thistory from CSV file
- Delete all or specific history entries, with these changes reflected in the CSV file.

## Professional Logging Practices
A comprehensive logging system is established to record:

- Detailed application operations and data manipulations.
- Errors and informational messages.
- Different log message severity levels (INFO, WARNING, ERROR) for effective monitoring.

Dynamic logging configuration is supported through environment variables, allowing customization of logging levels and output destinations.

## Advanced Data Handling with Pandas
**Pandas** is employed for:

- Efficient data reading and writing to CSV files.
- Management of calculation history, ensuring robust data handling.

## Design Patterns for Scalable Architecture
Key design patterns are incorporated to address software design challenges:

- **Facade Pattern**: Simplifies the interaction with the complex Pandas data management system. Instead of directly interacting with Pandas, users interact with a simple set of functions to save, load, and manage calculation history. This hides the complexity of data manipulation, making the code easier to use and maintain.
- **Command Pattern**: The Command Pattern structures commands (like arithmetic operations and history management) as objects. This allows the REPL (Read-Eval-Print Loop) to handle each operation independently, making the system more flexible and scalable. New commands can be added without altering the existing code, adhering to the Open/Closed Principle.

## Testing and Code Quality
The application achieves **92% test coverage** in VSCode using **Pytest**. Code quality is maintained and verified against **PEP 8** standards using **Pylint** with a **score 7.80/10**.

## Version Control Best Practices
Logical commits are utilized to clearly group feature development and corresponding tests, evidencing clear development progression. Commits follow a consistent structure.

## Documentation
Comprehensive documentation is compiled in this **README.md**, covering usage examples and an in-depth analysis of architectural decisions, with emphasis on the implementation and impact of chosen design patterns and logging strategy.

## Video Showcase
A video has been created to demonstrate the features and functionalities of this **Advanced Calculator**. You can view the video [here](https://drive.google.com/file/d/1EGbfYImeCyu5r0VWrh-FLz0FZ3h-ZA92/view?usp=sharing).


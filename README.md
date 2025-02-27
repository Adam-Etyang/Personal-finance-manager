# Personal Finance Tracker

A comprehensive command-line tool for tracking personal finances, managing budgets, and monitoring financial goals.

## Overview

This Personal Finance Tracker is a database-driven application that helps users manage their financial information through a simple command-line interface. The application allows users to track accounts, transactions, categories, budgets, and financial goals in one centralized system.

## Technologies Used

- **Database**: MySQL for data storage and management
- **Interface**: Python with mysql.connector for database interactions
- **DBMS**: DBeaver for database administration and management
- **Operating Systems**: Cross-platform support (Windows, macOS, Linux)

## Features

- **Account Management**
  - Add new bank accounts, credit cards, or savings accounts
  - View all accounts with current balances
  - Track account institutions
  
- **Transaction Tracking**
  - Record income and expenses
  - Categorize transactions
  - View transaction history by account
  
- **Budgeting Tools**
  - Create category-based budgets with timeframes
  - Track spending against budgets
  
- **Financial Goals**
  - Set savings goals with target amounts and due dates
  - Track progress toward financial goals
  
- **Categorization System**
  - Create hierarchical categories for better organization
  - Parent-child category relationships
  
## Database Structure

The application uses the following tables:

1. **Accounts** - Stores information about bank accounts, credit cards, etc.
2. **Categories** - Maintains a hierarchical categorization system
3. **Transactions** - Records all financial transactions
4. **Budgets** - Tracks spending limits by category
5. **Goals** - Manages financial targets and progress

## Getting Started

### Prerequisites

- Python 3.x
- MySQL Server
- `mysql-connector-python` package

### Installation

1. Clone this repository

2. Create the database using the provided schema file:

   mysql -u username -p < schema.sql

3. (Optional) Load sample data:
   
   mysql -u username -p < queries.sql

4. Run the application:

   python DB-interface.py

### Database Setup

The database schema is defined in `schema.sql`. This file creates:
- The `PersonalFinanceDB` database
- All necessary tables with appropriate relationships
- Required constraints and data types

## Usage

The application provides a simple menu-driven interface with the following options:

1. Add Account
2. View Accounts
3. Add Transaction
4. View Transactions
5. Add Category
6. View Categories
7. Add Budget
8. View Budgets
9. Add Goal
10. View Goals
11. Exit

To use the application, follow the on-screen prompts after selecting an option.

### Example Workflow

1. Add accounts (checking, savings, credit cards)
2. Create expense categories (e.g., Food, Entertainment)
3. Record transactions as they occur
4. Set up monthly budgets for categories
5. Create financial goals (e.g., Emergency Fund, Vacation)
6. View reports to track your financial progress

## Sample Data

The `queries.sql` file contains sample data that can be used to populate the database for testing or demonstration purposes. This includes:
- 4 sample accounts across different banks
- 5 expense/income categories
- 3 financial goals
- 11 sample transactions
- 3 budget allocations

## Future Enhancements

Potential future improvements:
- Recurring transaction support
- Data visualization and reports
- Import/export functionality
- Multi-user support
- Mobile application interface


## License

This project is available for personal use.

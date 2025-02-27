-- Create the database if it doesn't exist
USE PersonalFinanceDB;

-- Create table to store accounts

CREATE TABLE accounts (
    account_id INT AUTO_INCREMENT PRIMARY KEY,
    account_name VARCHAR(100) NOT NULL,
    account_type ENUM('savings', 'current', 'credit card') NOT NULL,
    balance DECIMAL(15,2) NOT NULL DEFAULT 0.00,
    institution VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store categories
CREATE TABLE Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL,
    parent_category_id INT,
    FOREIGN KEY (parent_category_id) REFERENCES Categories(category_id) ON DELETE SET NULL
);

-- Table to record transactions
CREATE TABLE Transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT NOT NULL,
    date DATE NOT NULL,
    amount DECIMAL(15,2) NOT NULL,
    description VARCHAR(255),
    category_id INT,
    transaction_type ENUM('income', 'expense') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_id) REFERENCES accounts (account_id),
    FOREIGN KEY (category_id) REFERENCES Categories (category_id)
);

-- Table to store budgets
CREATE TABLE budgets (
    budget_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    amount DECIMAL(15,2) NOT NULL,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);

-- Table to store finance goals
CREATE TABLE goals (
    goal_id INT AUTO_INCREMENT PRIMARY KEY,
    goal_name VARCHAR(100) NOT NULL,
    target_amount DECIMAL(15,2) NOT NULL,
    current_amount DECIMAL(15,2) NOT NULL DEFAULT 0.00,
    due_date DATE,
    category_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);

show tables;
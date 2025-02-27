use personalfinancedb;

-- insert sample data into the accounts table
INSERT INTO Accounts (account_name, account_type, balance, institution) VALUES ('current', 'current', 2500.00, 'KCB');
INSERT INTO Accounts (account_name, account_type, balance, institution) VALUES ('Emergency Savings', 'Savings', 3000.00, 'Equity Bank');
INSERT INTO Accounts (account_name, account_type, balance, institution) VALUES ('Credit Card', 'credit card', -500.00, 'Visa');
INSERT INTO Accounts (account_name, account_type, balance, institution) VALUES ('Travel Fund', 'Savings', 1200.00, 'Co-operative Bank');


-- inserting sample data into the budgets table
INSERT INTO Budgets (category_id, start_date, end_date, amount) 
VALUES (1, '2025-03-01', '2025-03-31', 300.00);

INSERT INTO Budgets (category_id, start_date, end_date, amount) 
VALUES (3, '2025-03-01', '2025-03-31', 150.00);

INSERT INTO Budgets (category_id, start_date, end_date, amount) 
VALUES (5, '2025-03-01', '2025-03-31', 200.00);

-- inserting sample data into the categories table
INSERT INTO Categories (category_name, parent_category_id) 
VALUES ('Food', NULL);

INSERT INTO Categories (category_name, parent_category_id) 
VALUES ('Groceries', 1);

INSERT INTO Categories (category_name, parent_category_id) 
VALUES ('Entertainment', NULL);

INSERT INTO Categories (category_name, parent_category_id) 
VALUES ('Salary', NULL);

INSERT INTO Categories (category_name, parent_category_id) 
VALUES ('Travel', NULL);

-- inserting sample data into the goals table
INSERT INTO Goals (goal_name, target_amount, current_amount, due_date, category_id) 
VALUES ('New Laptop', 1500.00, 500.00, '2025-06-30', NULL);

INSERT INTO Goals (goal_name, target_amount, current_amount, due_date, category_id) 
VALUES ('Vacation', 3000.00, 100.00, '2025-12-31', 5);

INSERT INTO Goals (goal_name, target_amount, current_amount, due_date, category_id) 
VALUES ('Emergency Fund', 5000.00, 2000.00, '2026-01-01', NULL);

-- inserting sample data into the transaction table
INSERT INTO Transactions (account_id, date, amount, description, category_id, transaction_type) 
VALUES (1, '2025-02-20', 2000.00, 'Monthly Salary', 4, 'income');

INSERT INTO Transactions (account_id, date, amount, description, category_id, transaction_type) 
VALUES (1, '2025-02-21', 50.00, 'Coffee Shop', 1, 'expense');

INSERT INTO Transactions (account_id, date, amount, description, category_id, transaction_type) 
VALUES (2, '2025-02-22', 100.00, 'Grocery Shopping', 2, 'expense');

INSERT INTO Transactions (account_id, date, amount, description, category_id, transaction_type) 
VALUES (3, '2025-02-23', 75.00, 'Dinner Out', 1, 'expense');

INSERT INTO Transactions (account_id, date, amount, description, category_id, transaction_type) 
VALUES (1, '2025-02-24', 30.00, 'Movie Tickets', 3, 'expense');

INSERT INTO Transactions (account_id, date, amount, description, category_id, transaction_type) 
VALUES (4, '2025-02-25', 150.00, 'Flight Booking', 5, 'expense');

INSERT INTO Transactions (account_id, date, amount, description, category_id, transaction_type) 
VALUES (2, '2025-02-26', 500.00, 'Savings Deposit', NULL, 'income');

INSERT INTO Transactions (account_id, date, amount, description, category_id, transaction_type) 
VALUES (1, '2025-02-27', 20.00, 'Bus Fare', NULL, 'expense');

INSERT INTO Transactions (account_id, date, amount, description, category_id, transaction_type) 
VALUES (3, '2025-02-28', 60.00, 'Online Subscription', 3, 'expense');

INSERT INTO Transactions (account_id, date, amount, description, category_id, transaction_type) 
VALUES (1, '2025-03-01', 80.00, 'Supermarket', 2, 'expense');

INSERT INTO Transactions (account_id, date, amount, description, category_id, transaction_type) 
VALUES (4, '2025-03-02', 25.00, 'Travel Snacks', 5, 'expense');

select * from Transactions;
select * from accounts;
select * from goals;
select * from categories;
select * from budgets;



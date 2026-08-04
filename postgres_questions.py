# PostgreSQL interview questions and queries.
# Each item: (question, answer)  -- answers often contain SQL.

POSTGRES_SECTIONS = [
    ("PostgreSQL Concepts", [
        ("What is PostgreSQL?",
         "PostgreSQL is a powerful open-source object-relational database management system (ORDBMS) known "
         "for standards compliance, extensibility, ACID transactions, and advanced features like JSONB, "
         "window functions, CTEs, and full-text search."),
        ("What are ACID properties?",
         "Atomicity (all-or-nothing transactions), Consistency (valid state transitions), Isolation "
         "(concurrent transactions don't interfere), Durability (committed data survives crashes)."),
        ("What is the difference between PostgreSQL and MySQL?",
         "PostgreSQL is object-relational, more standards-compliant, supports advanced types (JSONB, arrays, "
         "custom types), richer concurrency (MVCC), and more complex queries. MySQL is traditionally simpler "
         "and was historically faster for read-heavy simple workloads."),
        ("What is a primary key?",
         "A column (or set of columns) that uniquely identifies each row. It is NOT NULL and UNIQUE; a table "
         "can have only one primary key."),
        ("What is a foreign key?",
         "A column that references the primary key of another table, enforcing referential integrity between "
         "related tables."),
        ("What is the difference between DELETE, TRUNCATE, and DROP?",
         "DELETE removes rows (can use WHERE, logged, can be rolled back). TRUNCATE quickly removes all rows "
         "(faster, resets identity, minimal logging). DROP removes the entire table definition."),
        ("What is an index and why use it?",
         "An index is a data structure (B-tree by default) that speeds up lookups and ordering at the cost of "
         "extra storage and slower writes."),
        ("What index types does PostgreSQL support?",
         "B-tree (default), Hash, GIN (full-text/JSONB/arrays), GiST (geometric/range), BRIN (large ordered "
         "tables), and SP-GiST."),
        ("What is MVCC?",
         "Multi-Version Concurrency Control: PostgreSQL keeps multiple row versions so readers don't block "
         "writers and vice versa, providing snapshot isolation."),
        ("What is VACUUM and why is it needed?",
         "VACUUM reclaims storage from dead tuples left by MVCC updates/deletes, prevents transaction-ID "
         "wraparound, and updates statistics (with ANALYZE). Autovacuum automates this."),
        ("What is the difference between a clustered and non-clustered index?",
         "PostgreSQL has no permanent clustered index; CLUSTER physically reorders a table by an index once. "
         "Indexes are otherwise secondary (non-clustered) structures pointing to heap tuples."),
        ("What are the different types of JOINs?",
         "INNER JOIN (matching rows), LEFT/RIGHT OUTER JOIN (all rows from one side + matches), FULL OUTER "
         "JOIN (all rows both sides), CROSS JOIN (cartesian product), and SELF JOIN."),
        ("What is a view and a materialized view?",
         "A view is a stored query that runs each time it is referenced. A materialized view stores the "
         "result physically and must be refreshed with REFRESH MATERIALIZED VIEW."),
        ("What is a CTE (Common Table Expression)?",
         "A named temporary result set defined with WITH that improves readability and enables recursion "
         "(WITH RECURSIVE)."),
        ("What is normalization?",
         "Organizing tables to reduce redundancy and improve integrity, through normal forms (1NF: atomic "
         "values; 2NF: no partial dependency; 3NF: no transitive dependency; BCNF)."),
        ("What is the difference between WHERE and HAVING?",
         "WHERE filters rows before grouping; HAVING filters groups after GROUP BY (it can use aggregates)."),
        ("What is a transaction and how do you control it?",
         "A unit of work executed atomically. Controlled with BEGIN, COMMIT, ROLLBACK, and SAVEPOINT for "
         "partial rollbacks."),
        ("What are isolation levels in PostgreSQL?",
         "READ COMMITTED (default), REPEATABLE READ, and SERIALIZABLE. (READ UNCOMMITTED behaves like READ "
         "COMMITTED.) They control visibility of concurrent changes."),
        ("What is the difference between UNION and UNION ALL?",
         "UNION combines result sets and removes duplicates (sorts); UNION ALL keeps all rows including "
         "duplicates and is faster."),
        ("What is a sequence and SERIAL/IDENTITY?",
         "A sequence generates unique numbers. SERIAL is shorthand creating an integer column backed by a "
         "sequence; GENERATED AS IDENTITY is the SQL-standard, preferred modern approach."),
        ("What is EXPLAIN / EXPLAIN ANALYZE?",
         "EXPLAIN shows the query planner's chosen execution plan and cost estimates; EXPLAIN ANALYZE "
         "actually runs the query and reports real timing and row counts."),
        ("What is a trigger?",
         "A function automatically executed in response to INSERT/UPDATE/DELETE events on a table, defined "
         "with CREATE TRIGGER calling a trigger function."),
        ("What is the difference between CHAR, VARCHAR, and TEXT?",
         "CHAR(n) is fixed-length (blank-padded); VARCHAR(n) is variable with a length limit; TEXT is "
         "unlimited variable length. In PostgreSQL all perform similarly; TEXT/VARCHAR are usually preferred."),
        ("What is JSONB and how does it differ from JSON?",
         "JSON stores raw text (preserves formatting, slower to query). JSONB stores a decomposed binary "
         "form that is faster to query and supports indexing (GIN), at slightly higher write cost."),
    ]),
    ("Basic Queries", [
        ("Select all employees from the employees table.",
         "SELECT * FROM employees;"),
        ("Select only name and salary columns.",
         "SELECT name, salary FROM employees;"),
        ("Find employees with salary greater than 50000.",
         "SELECT * FROM employees WHERE salary > 50000;"),
        ("Find employees in the 'Sales' or 'Marketing' department.",
         "SELECT * FROM employees WHERE department IN ('Sales', 'Marketing');"),
        ("Find employees whose name starts with 'A'.",
         "SELECT * FROM employees WHERE name LIKE 'A%';"),
        ("Find employees with no manager (NULL manager_id).",
         "SELECT * FROM employees WHERE manager_id IS NULL;"),
        ("Sort employees by salary descending.",
         "SELECT * FROM employees ORDER BY salary DESC;"),
        ("Return the 5 highest-paid employees.",
         "SELECT * FROM employees ORDER BY salary DESC LIMIT 5;"),
        ("Return rows 11-20 (pagination).",
         "SELECT * FROM employees ORDER BY id LIMIT 10 OFFSET 10;"),
        ("Find employees hired between two dates.",
         "SELECT * FROM employees\nWHERE hire_date BETWEEN '2023-01-01' AND '2023-12-31';"),
        ("Select distinct department names.",
         "SELECT DISTINCT department FROM employees;"),
        ("Find employees with salary NOT between 30000 and 60000.",
         "SELECT * FROM employees WHERE salary NOT BETWEEN 30000 AND 60000;"),
    ]),
    ("Aggregations & Grouping", [
        ("Count the total number of employees.",
         "SELECT COUNT(*) FROM employees;"),
        ("Find the average salary per department.",
         "SELECT department, AVG(salary) AS avg_salary\n"
         "FROM employees\n"
         "GROUP BY department;"),
        ("Find departments with more than 10 employees.",
         "SELECT department, COUNT(*) AS cnt\n"
         "FROM employees\n"
         "GROUP BY department\n"
         "HAVING COUNT(*) > 10;"),
        ("Find the highest and lowest salary in the company.",
         "SELECT MAX(salary) AS highest, MIN(salary) AS lowest FROM employees;"),
        ("Find total salary expense per department, highest first.",
         "SELECT department, SUM(salary) AS total\n"
         "FROM employees\n"
         "GROUP BY department\n"
         "ORDER BY total DESC;"),
        ("Count employees per department, only departments starting with 'S'.",
         "SELECT department, COUNT(*)\n"
         "FROM employees\n"
         "WHERE department LIKE 'S%'\n"
         "GROUP BY department;"),
        ("Find the number of distinct departments.",
         "SELECT COUNT(DISTINCT department) FROM employees;"),
        ("Round the average salary to 2 decimals per department.",
         "SELECT department, ROUND(AVG(salary), 2) AS avg_salary\n"
         "FROM employees\n"
         "GROUP BY department;"),
    ]),
    ("Joins & Subqueries", [
        ("Join employees with their department names.",
         "SELECT e.name, d.dept_name\n"
         "FROM employees e\n"
         "JOIN departments d ON e.dept_id = d.id;"),
        ("List all departments, including those with no employees.",
         "SELECT d.dept_name, e.name\n"
         "FROM departments d\n"
         "LEFT JOIN employees e ON e.dept_id = d.id;"),
        ("Find employees earning more than the company average.",
         "SELECT * FROM employees\n"
         "WHERE salary > (SELECT AVG(salary) FROM employees);"),
        ("Find employees who earn more than their department's average.",
         "SELECT e.* FROM employees e\n"
         "WHERE salary > (\n"
         "    SELECT AVG(salary) FROM employees\n"
         "    WHERE dept_id = e.dept_id\n"
         ");"),
        ("Find departments that have no employees.",
         "SELECT d.* FROM departments d\n"
         "LEFT JOIN employees e ON e.dept_id = d.id\n"
         "WHERE e.id IS NULL;"),
        ("Self join: list employees with their manager's name.",
         "SELECT e.name AS employee, m.name AS manager\n"
         "FROM employees e\n"
         "LEFT JOIN employees m ON e.manager_id = m.id;"),
        ("Find employees who work on at least one project (EXISTS).",
         "SELECT * FROM employees e\n"
         "WHERE EXISTS (\n"
         "    SELECT 1 FROM projects p WHERE p.emp_id = e.id\n"
         ");"),
        ("Find customers who never placed an order.",
         "SELECT c.* FROM customers c\n"
         "WHERE c.id NOT IN (SELECT customer_id FROM orders);"),
        ("Total order amount per customer (join + group).",
         "SELECT c.name, SUM(o.amount) AS total\n"
         "FROM customers c\n"
         "JOIN orders o ON o.customer_id = c.id\n"
         "GROUP BY c.name;"),
    ]),
    ("Advanced Queries", [
        ("Find the second highest salary.",
         "SELECT MAX(salary) FROM employees\n"
         "WHERE salary < (SELECT MAX(salary) FROM employees);\n\n"
         "-- Or with a window function:\n"
         "SELECT DISTINCT salary FROM (\n"
         "    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk\n"
         "    FROM employees\n"
         ") t WHERE rnk = 2;"),
        ("Find the Nth highest salary using OFFSET.",
         "SELECT DISTINCT salary FROM employees\n"
         "ORDER BY salary DESC\n"
         "LIMIT 1 OFFSET (N - 1);"),
        ("Rank employees by salary within each department.",
         "SELECT name, department, salary,\n"
         "       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rnk\n"
         "FROM employees;"),
        ("Find the top earner in each department.",
         "SELECT * FROM (\n"
         "    SELECT *, ROW_NUMBER() OVER (\n"
         "        PARTITION BY department ORDER BY salary DESC) AS rn\n"
         "    FROM employees\n"
         ") t WHERE rn = 1;"),
        ("Calculate a running total of salaries ordered by id.",
         "SELECT id, salary,\n"
         "       SUM(salary) OVER (ORDER BY id) AS running_total\n"
         "FROM employees;"),
        ("Find duplicate emails in a users table.",
         "SELECT email, COUNT(*) AS cnt\n"
         "FROM users\n"
         "GROUP BY email\n"
         "HAVING COUNT(*) > 1;"),
        ("Delete duplicate rows keeping the lowest id.",
         "DELETE FROM users a\n"
         "USING users b\n"
         "WHERE a.id > b.id AND a.email = b.email;"),
        ("Use a CTE to find above-average earners.",
         "WITH avg_cte AS (\n"
         "    SELECT AVG(salary) AS avg_sal FROM employees\n"
         ")\n"
         "SELECT e.* FROM employees e, avg_cte\n"
         "WHERE e.salary > avg_cte.avg_sal;"),
        ("Recursive CTE: generate numbers 1 to 10.",
         "WITH RECURSIVE nums AS (\n"
         "    SELECT 1 AS n\n"
         "    UNION ALL\n"
         "    SELECT n + 1 FROM nums WHERE n < 10\n"
         ")\n"
         "SELECT n FROM nums;"),
        ("Pivot: count employees by department using FILTER.",
         "SELECT\n"
         "    COUNT(*) FILTER (WHERE department = 'Sales') AS sales,\n"
         "    COUNT(*) FILTER (WHERE department = 'IT') AS it\n"
         "FROM employees;"),
        ("Use COALESCE to replace NULL commissions with 0.",
         "SELECT name, COALESCE(commission, 0) AS commission\n"
         "FROM employees;"),
        ("Use CASE to bucket salaries into bands.",
         "SELECT name,\n"
         "  CASE\n"
         "    WHEN salary < 30000 THEN 'Low'\n"
         "    WHEN salary < 70000 THEN 'Mid'\n"
         "    ELSE 'High'\n"
         "  END AS band\n"
         "FROM employees;"),
        ("Find the difference between each employee's salary and the previous one.",
         "SELECT name, salary,\n"
         "       salary - LAG(salary) OVER (ORDER BY id) AS diff\n"
         "FROM employees;"),
        ("Get the most recent order per customer.",
         "SELECT DISTINCT ON (customer_id) *\n"
         "FROM orders\n"
         "ORDER BY customer_id, order_date DESC;"),
    ]),
    ("DDL, DML & Administration", [
        ("Create an employees table.",
         "CREATE TABLE employees (\n"
         "    id SERIAL PRIMARY KEY,\n"
         "    name VARCHAR(100) NOT NULL,\n"
         "    department VARCHAR(50),\n"
         "    salary NUMERIC(10,2),\n"
         "    hire_date DATE DEFAULT CURRENT_DATE\n"
         ");"),
        ("Add a new column to a table.",
         "ALTER TABLE employees ADD COLUMN email VARCHAR(255);"),
        ("Insert a new employee.",
         "INSERT INTO employees (name, department, salary)\n"
         "VALUES ('Asha', 'IT', 65000);"),
        ("Update an employee's salary by 10%.",
         "UPDATE employees SET salary = salary * 1.10\n"
         "WHERE id = 5;"),
        ("Upsert (insert or update on conflict).",
         "INSERT INTO employees (id, name, salary)\n"
         "VALUES (5, 'Asha', 70000)\n"
         "ON CONFLICT (id)\n"
         "DO UPDATE SET salary = EXCLUDED.salary;"),
        ("Create an index on the department column.",
         "CREATE INDEX idx_emp_dept ON employees(department);"),
        ("Add a foreign key constraint.",
         "ALTER TABLE employees\n"
         "ADD CONSTRAINT fk_dept\n"
         "FOREIGN KEY (dept_id) REFERENCES departments(id);"),
        ("Create a view of high earners.",
         "CREATE VIEW high_earners AS\n"
         "SELECT name, salary FROM employees\n"
         "WHERE salary > 80000;"),
        ("Grant SELECT on a table to a user.",
         "GRANT SELECT ON employees TO analyst_user;"),
        ("Write a simple trigger function and trigger.",
         "CREATE OR REPLACE FUNCTION set_updated()\n"
         "RETURNS TRIGGER AS $$\n"
         "BEGIN\n"
         "    NEW.updated_at = NOW();\n"
         "    RETURN NEW;\n"
         "END;\n"
         "$$ LANGUAGE plpgsql;\n\n"
         "CREATE TRIGGER trg_updated\n"
         "BEFORE UPDATE ON employees\n"
         "FOR EACH ROW EXECUTE FUNCTION set_updated();"),
    ]),
]

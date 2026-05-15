-- REPORT: Outstanding Student Balances
-- AREA: Finance
-- PURPOSE: Identifies active students with balances due for finance follow-up.
-- PARAMETERS: :minimum_balance
-- SENSITIVITY: FERPA/financial data - restricted audience

SELECT
    stu.id AS student_id,
    stu.first_name,
    stu.last_name,
    COALESCE(acct.balance_due, 0) AS balance_due,
    acct.last_statement_date
FROM SC_ERP.STUDENTS stu
JOIN SC_ERP.FINANCIAL_ACCOUNTS acct
  ON stu.id = acct.student_id
WHERE stu.status = 'ACTIVE'
  AND COALESCE(acct.balance_due, 0) >= :minimum_balance
ORDER BY acct.balance_due DESC, stu.last_name, stu.first_name;

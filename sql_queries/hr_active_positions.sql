-- REPORT: Active Positions by Department
-- AREA: Human Resources
-- PURPOSE: Gives HR a governed view of active employee position counts by department.
-- PARAMETERS: none
-- SENSITIVITY: employee data - internal use

SELECT
    dept.department_name,
    COUNT(emp.employee_id) AS active_employee_count,
    SUM(CASE WHEN emp.position_type = 'FULL_TIME' THEN 1 ELSE 0 END) AS full_time_count,
    SUM(CASE WHEN emp.position_type = 'PART_TIME' THEN 1 ELSE 0 END) AS part_time_count
FROM SC_ERP.EMPLOYEES emp
JOIN SC_ERP.DEPARTMENTS dept
  ON emp.department_id = dept.id
WHERE emp.employment_status = 'ACTIVE'
GROUP BY dept.department_name
ORDER BY dept.department_name;

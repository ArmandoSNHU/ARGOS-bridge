-- REPORT: Active Registration by Department
-- AREA: Student
-- PURPOSE: Helps student services and academic leaders monitor active registrations by department.
-- PARAMETERS: :term_code
-- SENSITIVITY: FERPA - aggregated student data

WITH active_enrollments AS (
    SELECT
        enr.student_id,
        enr.dept_id,
        enr.credit_hours
    FROM SC_ERP.ENROLLMENT enr
    WHERE enr.academic_term = :term_code
      AND enr.registration_status = 'ACTIVE'
)
SELECT
    dept.department_name,
    COUNT(DISTINCT active_enrollments.student_id) AS active_students,
    SUM(active_enrollments.credit_hours) AS registered_credit_hours
FROM active_enrollments
JOIN SC_ERP.DEPARTMENTS dept
  ON active_enrollments.dept_id = dept.id
GROUP BY dept.department_name
ORDER BY dept.department_name;

-- REPORT: Financial Aid Missing Requirements
-- AREA: Financial Aid
-- PURPOSE: Finds active aid applicants with incomplete requirements for outreach.
-- PARAMETERS: :aid_year
-- SENSITIVITY: FERPA/financial aid data - restricted audience

SELECT
    stu.id AS student_id,
    stu.first_name,
    stu.last_name,
    req.requirement_code,
    req.requirement_description,
    req.status AS requirement_status
FROM SC_ERP.STUDENTS stu
JOIN SC_ERP.FINANCIAL_AID_REQUIREMENTS req
  ON stu.id = req.student_id
WHERE req.aid_year = :aid_year
  AND req.status IN ('MISSING', 'INCOMPLETE')
ORDER BY stu.last_name, stu.first_name, req.requirement_code;

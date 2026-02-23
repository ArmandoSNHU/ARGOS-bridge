-- PROJECT: ARGOS-bridge
-- TARGET: Sample College ERP (Generic)

/* 1. Enrollment Analytics */
-- Summary of registration by department
SELECT 
    dept_name, 
    COUNT(student_id) as total_enrolled,
    SUM(credit_hours) as total_credits
FROM SC_ERP.ENROLLMENT_VIEW
WHERE term_code = '202510'
GROUP BY dept_name;

/* 2. Security Audit */
-- Find active users with administrative database access
SELECT 
    user_id, 
    role_name, 
    last_login 
FROM SC_ERP.SYSTEM_ACCESS 
WHERE is_active = 'Y' 
  AND role_name LIKE '%ADMIN%';
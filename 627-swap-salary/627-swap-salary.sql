UPDATE salary
SET sex = case sex
WHEN 'm' then 'f'
WHEN 'f' then 'm'
END 

# UPDATE employee 
# SET StateCode  = CASE StateCode
#  WHEN 'Ar' THEN 'FL' 
#  WHEN 'GE' THEN 'AL' 
#   ELSE  'IN' 
#  END
# UPDATE salary
# SET sex =
# case sex
# WHEN 'm' then 'f'
# WHEN 'f' then 'm'
# END 

# UPDATE employee 
# SET StateCode  = CASE StateCode
#  WHEN 'Ar' THEN 'FL' 
#  WHEN 'GE' THEN 'AL' 
#   ELSE  'IN' 
#  END


Update salary
set sex = CASE sex when 'm' then 'f'
when 'f' then 'm'
END
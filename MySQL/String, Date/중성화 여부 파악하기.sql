# https://school.programmers.co.kr/learn/courses/30/lessons/59409
# SELECT ANIMAL_ID, NAME,
# CASE
#     WHEN SEX_UPON_INTAKE LIKE "Neutered%" THEN 'O'
#     WHEN SEX_UPON_INTAKE LIKE "SPAYED%" THEN 'O'
#     ELSE 'X'
# END AS "중성화"
# FROM ANIMAL_INS
# order by ANIMAL_ID

SELECT ANIMAL_ID, NAME, if(SEX_UPON_INTAKE like 'Intact%', 'X', 'O') as '중성화'
from ANIMAL_INS
order by ANIMAL_ID

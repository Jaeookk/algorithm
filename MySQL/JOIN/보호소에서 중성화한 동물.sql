# https://school.programmers.co.kr/learn/courses/30/lessons/59045
SELECT O.ANIMAL_ID, O.ANIMAL_TYPE, O.NAME from ANIMAL_INS I
left join ANIMAL_OUTS O
on I.ANIMAL_ID = O.ANIMAL_ID
where left(SEX_UPON_INTAKE,6) NOT IN ('Spayed', 'Neuter')
    and left(SEX_UPON_OUTCOME,6) IN ('Spayed', 'Neuter')
order by O.ANIMAL_ID

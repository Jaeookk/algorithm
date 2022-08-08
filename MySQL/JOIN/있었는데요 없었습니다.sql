# https://school.programmers.co.kr/learn/courses/30/lessons/59043
SELECT I.ANIMAL_ID, I.NAME from ANIMAL_INS I
join ANIMAL_OUTS O
on O.ANIMAL_ID = I.ANIMAL_ID
where O.DATETIME < I.DATETIME
order by I.DATETIME

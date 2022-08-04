-- SHOW DATABASES : 현재 서버에 어떤 DB가 있는지 보기

-- USE : 사용할 데이터베이스 지정
-- 		   지정해 놓은 후 특별히 다시 USE문 사용하거나 다른 DB를 사용하겠다고 명시하지 않는 이상 모든 SQL문은 지정 DB에서 수행
USE world;

-- SHOW TABLES : 데이터베이스의 테이블 이름 보기
SHOW TABLES; 

-- SHOW TABLE STATUS : 데이터베이스의 테이블 정보 조회
SHOW TABLE STATUS;

-- DESCRIBE(DESC) : 테이블에 무슨 열이 있는지 확인
DESC city;

-- LAB #01
-- country 테이블과 countrylanguage 테이블 정보 보기
DESC country;
DESC countrylanguage;

-- SELECT ... FROM : 요구하는 데이터를 가져오는 구문 / 데이터베이스 내 테이블에서 원하는 정보를 추출
-- SELECT의 구문 형식
-- SELECT FROM table_references
-- 	      WHERE where_condition
--    	  GROUP BY {col_name | expr | position}
--        HAVING where_condition
--        ORDER BY {col_name | expr | position}

-- SELECT * FROM ...
-- SELECT 열 이름 FROM ... : 테이블에서 필요로 하는 열만 가져오기 가능 / 여러 개의 열을 가져오고 싶을 때는 콤마로 구분 / 열 이름의 순서는 출력하고 싶은 순서대로 배열 가능

-- SELECT 필드이름 FROM 테이블 이름 WHERE 조건식 : 조회하는 결과에 특정한 조건으로 원하는 데이터만 보고 싶을 때 사용 
SELECT * FROM city
WHERE Population > 8000000;


-- 관계 연산자의 사용
-- OR / AND / 조건(=,<,>,<=,>=,<>,!= 등) / 관계(NOT, AND, OR 등) 
-- https://dev.mysql.com/doc/refman/8.0/en/functions.html
SELECT * FROM city
WHERE Population > 7000000 AND Population < 8000000;


-- LAB #02
-- 한국에 있는 도시들 보기
-- 미국에 있는 도시들 보기
-- 한국에 있는 도시들 중에 인구 수가 1,000,000 이상인 도시 보기
SELECT * FROM city
WHERE CountryCode = 'KOR'
AND Population >= 1000000;


-- BETWEEN : 데이터가 숫자로 구성되어 있어 연속적인 값은 BETWEEN ... AND 사용 가능
SELECT * FROM city
WHERE Population BETWEEN 7000000 AND 8000000;

-- IN : 이산적인 값의 조건에서는 IN() 사용 가능
SELECT * FROM city
WHERE NAME IN("Seoul", "New York", "Tokyo");


# LAB #03
# 한국, 미국, 일본의 도시들 보기
SELECT * FROM city
WHERE CountryCode IN("KOR" , "USA", "JPN");


-- LIKE : 문자열의 내용 검색 / 문자 뒤에 % --> 무엇이든 허용 / 한 글자와 매치하기 위해서는 언더바 (_) 사용
SELECT * FROM city
WHERE CountryCode LIKE "KO_";

SELECT * FROM city
WHERE NAME LIKE "TEL %";


-- Sub Query : 쿼리문 안에 또 쿼리문이 들어 있는 것 / 서브 쿼리의 결과가 둘 이상이 되면 에러 발생
SELECT * FROM city
WHERE CountryCode = (	SELECT CountryCode FROM city
						WHERE NAME = 'SEOUL'	);
-- 서브 쿼리의 결과가 2개 이상이므로 에러 발생
SELECT * FROM city
WHERE Population = (	SELECT Population FROM city
						WHERE District = 'New York'	);
                
                
-- ANY : 서브쿼리의 여러 개의 결과 중 한 가지만 만족해도 가능 / =ANY 구문은 IN과 동일한 의미
SELECT * FROM city
WHERE Population > ANY (	SELECT Population FROM city
							WHERE District = 'New York'	);
             
             
-- ALL : 서브쿼리의 여러 개의 결과를 모두 만족 시켜야 함
SELECT * FROM city
WHERE Population > ALL (	SELECT Population FROM city
							WHERE District = 'New York'	);                            
               
               
-- ORDER BY : 결과가 출력되는 순서를 조절하는 구문 / Default는 오름차순 / 내림차순은 열 이름 뒤에 DESC 적ㅇ어주면 됨
SELECT * FROM city
ORDER BY Population DESC;
-- ORDER BY 구문을 혼합해 사용하는 구문도 가능!!  
SELECT * FROM city
ORDER BY CountryCode ASC, Population DESC;


# LAB #04
# 인구수로 내림차순하여 한국에 있는 도시 보기
# 국가 면적 크기로 내림차순 하여 나라 보기 (country table)
SELECT * FROM city
WHERE CountryCode = "KOR"
ORDER BY Population DESC;

SELECT * FROM country
ORDER BY SurfaceArea DESC;


-- DISTINCT
-- 중복된 것은 1개씩만 보여주면서 출력, 테이블의 크기가 클수록 효율적
select countrycode from city; -- 중복 o
select distinct countrycode from city; -- 중복 x


-- LIMIT
-- 출력 개수를 제한 / 상위의 N개만 출력하는 'LIMIT N' 구문 / 서버의 처리량을 많이 사용해 서버의 전반적인 성능을 나쁘게 하는 악성 쿼리문 개선할 때 사용
select * from city
order by Population desc
limit 10;


-- GROUP BY
-- 그룹으로 묶어주는 역할 
-- 집계함수(Aggregate Function)을 함께 사용
-- AVG():평균 / MIN():최소값 / MAX():최대값 / COUNT():행의 개수 / COUNT(DISTINCT):중복 제외된 행의 개수 / STDEV():표준편차 / VARIANCE():분산
-- 읽기 좋게 하기 위해 별칭(Alias) 사용
select CountryCode, MAX(Population) from city
group by CountryCode;

select CountryCode, MIN(Population) from city
group by CountryCode;

select CountryCode, AVG(Population) as 'Average' from city
group by CountryCode;


-- LAB #05
-- 도시는 몇개인가?
-- 도시들의 평균인구수는? 
select count(*) from city;

select avg(population) from city;


-- HAVING
-- WHERE과 비슷한 개념으로 조건 제한
-- 집계 함수에 대해서 조건 제한하는 편리한 개념
-- HAVING절은 반드시 GROUP BY 절 다음에 나와야함.
select CountryCode, max(population) from city
group by CountryCode
having max(population) > 8000000;


-- ROLLUP
-- 총합 또는 중간합계가 필요한 경우 사용
-- GROUP BY 절과 함께 WITH ROLLUP문 사용
select CountryCode, Name, sum(population) from city
group by CountryCode, Name with rollup;


-- JOIN
-- JOIN은 데이터베이스 내의 여러 테이블에서 가져온 레코드를 조합하여 하나의 테이블이나 결과 집합으로 표현
select * from city
join country on city.CountryCode = country.Code;


-- LAB #06
-- city, country, countrylanguage 테이블 3개를 JOIN 하기
select * from city
join country on city.CountryCode = country.Code
join countrylanguage on city.CountryCode = countrylanguage.CountryCode;


-- MySQL 내장함수
-- 사용자의 편의를 위해 다양한 기능의 내장 함수를 미리 정의하여 제공
-- 대표적인 내장함수의 종류 : 문자열 함수 / 수학 함수 / 날짜와 시간 함수

-- LENGTH() : 전달받은 문자열의 길이를 반환
select length('asdafasf');

-- CONCAT() : 전달받은 문자열을 모두 결합하여 하나의 문자열로 반환 / 전달받은 문자열 중 하나라고 NULL이 존재하면 NULL 반환
select concat('MY', 'sql dd', 'asfeme');

-- LOCATE() : 문자열 내에서 찾는 문자열이 처음으로 나타나는 위치를 찾아서 해당 위치를 반환 / 찾는 문자열이 문자열 내에 존재하지 않으면 0을 반환 / MySQL에서는 문자열의 시작 인덱스를 1부터 계산
select locate('abc', 'absadasacsascabcsda');

-- LEFT(), RIGHT() : 문자열의 왼쪽/오른쪽 부터 지정한 개수만큼의 문자를 반환
select 
left('MySQL is an open source relational database management system', 5),
right('MySQL is an open source relational database management system', 6);

-- LOWER(), UPPER() : 문자열의 문자를 모두 소문자/대문자로 변경
select 
lower('MySQL is an open source relational database management system'),
upper('MySQL is an open source relational database management system');

-- REPLACE() : 문자열에서 특정 문자열을 대체 문자열로 교체
select replace('MSSQL', 'MS', "MY");

-- TRIM() : 문자열의 앞이나 뒤, 또는 양쪽 모두에 있는 특정 문자를 제거
-- TRIM() 함수에서 사용할 수 있는 지정자
-- 		* BOTH : 전달받은 문자열의 양 끝에 존재하는 특정 문자를 제거 (기본 설정)
-- 		* LEADING : 전달받은 문자열 앞에 존재하는 특정 문자를 제거
-- 		* TRAILING : 전달받은 문자열 뒤에 존재하는 특정 문자를 제거
-- 만약 지정자를 명시하지 않으면, 자동으로 BOTH 설정.
-- 제거할 문자를 명시하지 않으면, 자동으로 공백을 제거.
select
trim('           MySQL         '),
trim(leading '#' from '###MySQL##'),
trim(trailing '#' from '###MySQL##');

-- FORMAT() : 숫자 타입의 데이터를 세 자리마다 쉼표(,)를 사용하는 '#,###,###' 형식을 변환 / 반환되는 데이터의 형식은 문자열 타입 / 두 번째 인수는 반올림할 소수 부분의 자릿수
select format(123456789.4567, 3),
format(123456789.4567, 1);

-- FLOOR():내림 / CEIL():올림 / ROUND():반올림
select
floor(1.95),
ceil(1.95),
round(1.95);

-- SQRT():양의 제곱근 / POW():첫 번째 인수로는 밑수를 전달, 두 번째 인수로는 지수를 전달 / EXP():인수로 지수를 전달받아, e의 거듭제곱 계산 / LOG():자연로그 값을 계산
select
sqrt(4),
pow(2,3),
exp(2),
log(3);

-- SIN(), COS(), TAN()
select
sin(PI()/2),
cos(PI()),
tan(PI()/4);

-- ABS(X):절대값 / RAND():0이상 1미만의 하나의 실수를 무작위로 생성
select
abs(-2),
rand(),
round(rand()*100, 0);

-- NOW():현재 날짜와 시간을 반환, 반환되는 값은 'YYYY-MM-DD HH:MM:SS' 또는 YYYYMMDDHHMMSS 형태로 반환
-- CURDATE(): 현재 날짜를 반환 YYYY-MM-DD or YYYYMMDD
-- CURTIME()
select
now(),
curdate(),
curtime();

-- DATE():전달받은 값에 해당하는 날짜 정보를 반환
-- MONTH():월에 해당하는 값을 반환 / DAY():일에 해당하는 값을 반환 / HOUR():시간에 해당하는 값을 반환 / MINUTE():분에 해당하는 값을 반환 / SECOND():초에 해당하는 값을 반환
select
NOW(),
DATE(NOW()),
MONTH(NOW()),
day(NOW()),
hour(NOW()),
minute(NOW()),
second(NOW());

-- MONTHNAME() / DAYNAME() : 월/요일에 해당하는 이름을 반환
select
now(),
monthname(now()),
dayname(now());

-- DAYOFWEEK():일자가 해당 주에서 몇 번째 날인지를 반환, 1부터 7사이의 값을 반환 (일요일=1, 토요일=7)
-- DAYOFMONTH():일자가 해당 월에서 몇 번째 날인지를 반환, 0부터 31사이의 값
-- DAYOFYEAR():일자가 해당 연도에서 몇 번째 날인지를 반환, 1부터 366사이의 값
select
now(),
dayofweek(now()),
dayofmonth(now()),
dayofyear(now());

-- DATE_FORMAT() : 전달받은 형식에 맞춰 날짜와 시간 정보를 문자열로 반환
select 
now(),
date_format(now(), '%D %y %a %d %m %n %j');


-- **************SQL 고급*************** -- 

-- CREATE TABLE AS SELECT : city 테이블과 똑같은 city2 테이블 생성
create table city2 as select * from city;
select * from city2;

-- CREATE DATABASE : 새로운 데이터베이스를 생성 / USE문으로 새 데이터베이스를 사용
create database jaewook;
use jaewook;

-- CREATE TABLE
-- 데이터 타입 : https://dev.mysql.com/doc/refman/8.0/en/data-types.html
-- 첫번째 방법 : GUI로 생성
select * from test;

-- 두번째 방법
CREATE TABLE test2 (
	id  INT NOT NULL PRIMARY KEY,
    col1 INT NULL,
    col2 FLOAT NULL,
    col3 VARCHAR(45) NULL
);
select * from test2;

-- ALTER TABLE : ADD문과 함께 사용하면, 테이블에 컬럼을 추가할 수 있다.
ALTER TABLE test2
ADD col4 INT NUll;

select * from test2;
DESC test2;

-- ALTER TABLE : MODIFY문과 함께 사용하면, 테이블의 컬럼 타입을 변경할 수 있다.
ALTER TABLE test2
MODIFY col4 VARCHAR(20) NULL;

DESC test2;

-- ALTER TABLE : DROP문과 함께 사용하면, 테이블에 컬럼을 제거할 수 있다.
ALTER TABLE test2
DROP col4;

DESC test2;

-- INDEX 인덱스
-- 테이블에서 원하는 데이터를 빠르게 찾기 위해 사용
-- 일반적으로 데이터를 검색할 때 순서대로 테이블 전체를 검색하므로 데이터가 많으면 많을수록 탐색하는 시간이 늘어남
-- 검색과 질의를 할 대 테이블 전체를 읽지 않기 때문에 빠름
-- 설정된 컬럼 값을 포함한 데이터의 삽입, 삭제, 수정 작업이 원본 테이블에서 이루어질경우, 인덱스도 함께 수정되어야함
-- 인덱스가 있는 테이블은 처리 속도가 느려질 수 있으므로 수정보다는 검색이 자주 사용되는 테이블에서 사용하는 것이 좋음

-- CREATE INDEX : 인덱스를 생성
CREATE INDEX Col1IDX
ON test (col1);

-- SHOW INDEX : 인덱스 정보 보기
SHOW INDEX FROM test;

-- CREATE UNIQUE INDEX : 중복 값을 허용하지 않는 인덱스
CREATE UNIQUE INDEX Col2IDX
ON test (col1);

SHOW INDEX FROM test;

-- FULTEXT INDEX: 일반적인 인덱스와는 달리 매우 빠르게 테이블의 모든 텍스트 컬럼을 검색
ALTER TABLE test
ADD FULLTEXT Col3IDX(col3);

SHOW INDEX FROM test; -- Index_type이 FULLTEXT로 되어 있는거 볼 수 있다.

-- INDEX 삭제 (ALTER): ALTER문을 사용하여 테이블에 추가된 인덱스 삭제
ALTER TABLE test
DROP INDEX Col3IDX;

SHOW INDEX FROM test;

-- INDEX 삭제 (DROP INDEX): DROP문을 사용하여 해당 테이블에서 명시된 인덱스를 삭제. DROP문은 내부적으로 ALTER문으로 자동 변환되여 명시된 이름의 인덱스를 삭제.
DROP INDEX Col2IDX ON test;
SHOW INDEX FROM test;

-- VIEW
-- 뷰는 데이터베이스에 존재하는 일종의 가상 테이블
-- 실제 테이블처럼 행과 열을 가지고 있지만, 실제로 데이터를 저장하진 않음
-- MySQL에서 뷰는 다른 테이블이나 다른 뷰에 저장되어 있는 데이터를 보여주는 역할만 수행
-- 뷰를 사용하려면 여러 테이블이나 뷰를 하나의 테이블처럼 볼 수 있음
-- 뷰의 장점
-- 		특정 사용자에게 테이블 전체가 아닌 필요한 컬럼만 보여줄 수 있음
-- 		복잡한 쿼리를 단순화해서 사용
--      쿼리 재사용 가능
-- 뷰의 단점
-- 		한 번 정의된 뷰는 변경할 수 없음
--      삽입, 삭제, 갱신 작업에 많은 제한사항을 가짐
--      자신만의 인덱스를 가질 수 없음

-- CREATE VIEW : 뷰 생성
CREATE VIEW testView AS
SELECT Col1, Col2
FROM test;

SELECT * FROM testView;

-- ALTER VIEW : 뷰를 수정
ALTER VIEW testView AS
SELECT Col1, Col2, Col3
FROM test;

SELECT * FROM testView;

-- DROP VIEW : 뷰 삭제
DROP VIEW testView;

-- LAB #07
-- city, country, countrylanguage 테이블을 JOIN하고, 한국에 대한 정보만 뷰 생성하기
USE world;

CREATE VIEW allView AS
SELECT city.Name, country.SurfaceArea, city.Population, countrylanguage.Language FROM city
JOIN country ON city.countryCode = country.Code
JOIN countrylanguage ON city.CountryCode = countrylanguage.CountryCode
WHERE city.CountryCode = 'KOR';

SELECT * FROM allView;

-- INSERT : 테이블 이름 다음에 나오는 열 생략 가능
-- 생략한 경우에 VALUE 다음에 나오는 값들의 순서 및 개수가 테이블이 정의된 열 순서 및 개수와 동일해야함
USE jaewook;

INSERT INTO test
VALUE(1, 123, 1.1, "TEST");

SELECT * FROM test;
DESC test;

-- INSERT INTO SELECT : test 테이블에 있는 내용을 test2 테이블에 삽입
INSERT INTO test2 SELECT * FROM test;
SELECT * FROM test2;

-- UPDATE : 기존에 입력되어 있는 값 변경하는 구문.
-- 			WHERE절 생략 가능하나 테이블의 전체 행의 내용이 변경된다.
UPDATE test
SET col1 = 1, col2 = 1.0, col3 = 'test'
WHERE id = 1;
SELECT * FROM test;

-- DELETE : 행 단위로 데이터 삭제
-- 			DELETE FROM 테이블이름 WHERE 조건;
-- 			데이터는 지워지지만 테이블 용량은 줄어들지 않음
-- 			원하는 데이터만 지울 수 있음
--          삭제 후 잘못 삭제한 것은 되돌릴 수 있음
DELETE FROM test
WHERE id = 1;
SELECT * FROM test;

-- TRUNCATE : 용량이 줄어 들고, 인덱스 등도 모두 삭제
-- 			테이블은 삭제하지는 않고, 데이터만 삭제
-- 			한꺼번에 다 지워야함
-- 			절대 되돌릴 수 없음
TRUNCATE TABLE test2;
SELECT * FROM test;

-- DROP TABLE : 테이블 전체(공간, 객체)를 삭제
-- 				절대 되돌릴 수 없음
DROP TABLE test;
SELECT * FROM test;

-- DROP DATABASE
DROP DATABASE jaewook;

-- LAB #08
-- 자신만의 연락처 테이블 만들기
-- 이름, 전화번호, 주소, 이메일, ...

-- ▶섹션 1. SELECT 기초 - 원하는 정보 찾기
-- 📌Lesson 1. SELECT 전반 기능 흝어보기

-- 1. 테이블의 모든 내용 보기
SELECT * FROM Customers;

-- 2. 원하는 column(열)만 골라서 보기
SELECT CustomerName FROM Customers;

SELECT CustomerName, ContactName, Country
FROM Customers;
---- 테이블의 컬럼이 아닌 값도 선택할 수 있습니다.
SELECT
  CustomerName, 1, 'Hello', NULL
FROM Customers;

-- 3. 원하는 조건의 row(행)만 걸러서 보기
-- WHERE 구문 뒤에 조건을 붙여 원하는 데이터만 가져올 수 있습니다.
SELECT * FROM Orders
WHERE EmployeeID = 3;

SELECT * FROM OrderDetails 
WHERE Quantity < 5;

-- 4. 원하는 순서로 데이터 가져오기
-- ORDER BY 구문을 사용해서 특정 컬럼을 기준으로 데이터를 정렬할 수 있습니다.
-- ASC	오름차순	✔️
-- DESC	내림차순	
SELECT * FROM Customers
ORDER BY ContactName;

SELECT * FROM OrderDetails
ORDER BY ProductID ASC, Quantity DESC;

-- 5. 원하는 만큼만 데이터 가져오기
-- LIMIT {가져올 갯수} 또는 LIMIT {건너뛸 갯수}, {가져올 갯수} 를 사용하여, 원하는 위치에서 원하는 만큼만 데이터를 가져올 수 있습니다.
SELECT * FROM Customers
LIMIT 10;

SELECT * FROM Customers
LIMIT 30, 10;

-- 6. 원하는 별명(alias)으로 데이터 가져오기
-- AS를 사용해서 컬럼명을 변경할 수 있습니다.
SELECT
  CustomerId AS ID,
  CustomerName AS NAME,
  Address AS ADDR
FROM Customers;



-- 📌Lesson 2. 각종 연산자들

-- 1. 사칙연산
-- +, -, *, /	각각 더하기, 빼기, 곱하기, 나누기
-- %, MOD	나머지
-- ❗ 문자열에 사칙연산을 가하면 0으로 인식

-- 2. 참/거짓 관련 연산자
-- 💡 MySQL에서는 TRUE는 1, FALSE는 0으로 저장됩니다.

-- IS	    양쪽이 모두 TRUE 또는 FALSE
-- IS NOT	한쪽은 TRUE, 한쪽은 FALSE

-- AND, &&	양쪽이 모두 TRUE일 때만 TRUE
-- OR, ||	한쪽은 TRUE면 TRUE

-- =	    양쪽 값이 같음
-- !=, <>	양쪽 값이 다름
-- >, <	    (왼쪽, 오른쪽) 값이 더 큼
-- >=, <=	(왼쪽, 오른쪽) 값이 같거나 더 큼
-- ❗ MySQL의 기본 사칙연산자는 대소문자 구분을 하지 않습니다.


-- 💡 테이블의 컬럼이 아닌 값으로 선택하기. 
 SELECT
  ProductName, Price,
  Price > 20 AS EXPENSIVE 
FROM Products;

-- BETWEEN {MIN} AND {MAX}	    두 값 사이에 있음
-- NOT BETWEEN {MIN} AND {MAX}	두 값 사이가 아닌 곳에 있음
 
-- IN (...)	    괄호 안의 값들 가운데 있음
-- NOT IN (...)	괄호 안의 값들 가운데 없음
 
-- LIKE '... % ...'	  0~N개 문자를 가진 패턴
-- LIKE '... _ ...'	  _ 갯수만큼의 문자를 가진 패턴
 
-- 총정리

-- +, -, *, /	  각각 더하기, 빼기, 곱하기, 나누기
-- %, MOD	      나머지
-- IS	    양쪽이 모두 TRUE 또는 FALSE
-- IS NOT	한쪽은 TRUE, 한쪽은 FALSE
-- AND, &&	양쪽이 모두 TRUE일 때만 TRUE
-- OR, ||	한쪽은 TRUE면 TRUE
-- =	    양쪽 값이 같음
-- !=, <>	양쪽 값이 다름
-- >, <	    (왼쪽, 오른쪽) 값이 더 큼
-- >=, <=	(왼쪽, 오른쪽) 값이 같거나 더 큼
-- BETWEEN {MIN} AND {MAX}	    두 값 사이에 있음
-- NOT BETWEEN {MIN} AND {MAX}	두 값 사이가 아닌 곳에 있음
-- IN (...)	    괄호 안의 값들 가운데 있음
-- NOT IN (...)	괄호 안의 값들 가운데 없음
-- LIKE '... % ...'	0~N개 문자를 가진 패턴
-- LIKE '... _ ...'	_ 갯수만큼의 문자를 가진 패턴





-- 📌Lesson 3. 숫자와 문자열을 다루는 함수들
-- 1. 숫자 관련 함수
-- ROUND	반올림
-- CEIL	    올림
-- FLOOR	내림
-- ABS	    절대값
-- GREATEST	(괄호 안에서) 가장 큰 값
-- LEAST	(괄호 안에서) 가장 작은 값

-- 집계함수
-- MAX	    가장 큰 값
-- MIN	    가장 작은 값
-- COUNT	갯수 (NULL값 제외)
-- SUM	    총합
-- AVG	    평균 값

-- POW(A, B)	A를 B만큼 제곱
-- SQRT	        제곱근

-- TRUNCATE(N, n)	N을 소숫점 n자리까지 선택
SELECT
  TRUNCATE(1234.5678, 1),
  TRUNCATE(1234.5678, 2),
  TRUNCATE(1234.5678, 3),
  TRUNCATE(1234.5678, -1),
  TRUNCATE(1234.5678, -2),
  TRUNCATE(1234.5678, -3);

-- 2. 문자열 관련 함수
-- UCASE, UPPER	        모두 대문자로
-- LCASE, LOWER	        모두 소문자로
-- CONCAT(...)	        괄호 안의 내용 이어붙임
-- CONCAT_WS(S, ...)	괄호 안의 내용 S로 이어붙임
SELECT CONCAT('HELLO', ' ', 'THIS IS ', 2021)
SELECT CONCAT_WS('-', 2021, 8, 15, 'AM')

-- SUBSTR	주어진 값에 따라 문자열 자름
-- LEFT	    왼쪽부터 N글자
-- RIGHT	오른쪽부터 N글자
SELECT
  SUBSTR('ABCDEFG', 3),
  SUBSTR('ABCDEFG', 3, 2),
  SUBSTR('ABCDEFG', -4),
  SUBSTR('ABCDEFG', -4, 2);

SELECT
  OrderDate,
  LEFT(OrderDate, 4) AS Year,
  SUBSTR(OrderDate, 6, 2) AS Month,
  RIGHT(OrderDate, 2) AS Day
FROM Orders;

-- LENGTH	    문자열의 바이트 길이
-- CHAR_LENGTH	문자열의 문자 길이

-- TRIM	    양쪽 공백 제거
-- LTRIM	왼쪽 공백 제거
-- RTRIM	오른쪽 공백 제거

-- LPAD(S, N, P)	S가 N글자가 될 때까지 P를 이어붙임
-- RPAD(S, N, P)	S가 N글자가 될 때까지 P를 이어붙임

-- REPLACE(S, A, B)	  S중 A를 B로 변경
-- INSTR(S, s)	      S중 s의 첫 위치 반환, 없을 시 0
-- CAST(A, T)	      A를 T 자료형으로 변환


-- 📌Lesson 4. 시간/날짜 관련 및 기타 함수
-- 1. 시간/날짜 관련 함수들

-- CURDATE	현재 날짜 반환
-- CURTIME	현재 시간 반환
-- NOW	    현재 시간과 날짜 반환

-- DATE	문자열에 따라 날짜 생성
-- TIME	문자열에 따라 시간 생성
SELECT
  '2021-6-1' = '2021-06-01',
  DATE('2021-6-1') = DATE('2021-06-01'),
  '1:2:3' = '01:02:03',
  TIME('1:2:3') = TIME('01:02:03');

-- YEAR	        주어진 DATETIME값의 년도 반환
-- MONTHNAME	주어진 DATETIME값의 월(영문) 반환
-- MONTH	    주어진 DATETIME값의 월 반환
-- WEEKDAY	    주어진 DATETIME값의 요일값 반환(월요일: 0)
-- DAYNAME	    주어진 DATETIME값의 요일명 반환
-- DAY	        주어진 DATETIME값의 날짜(일) 반환

-- HOUR	    주어진 DATETIME의 시 반환
-- MINUTE	주어진 DATETIME의 분 반환
-- SECOND	주어진 DATETIME의 초 반환

-- ADDDATE	시간/날짜 더하기
-- SUBDATE	시간/날짜 빼기

-- DATE_DIFF	두 시간/날짜 간 일수차
-- TIME_DIFF	두 시간/날짜 간 시간차

-- LAST_DAY	    해당 달의 마지막 날짜

-- DATE_FORMAT	시간/날짜를 지정한 형식으로 반환
-- %Y	    년도 4자리
-- %y	    년도 2자리
-- %M	    월 영문
-- %m	    월 숫자
-- %D	    일 영문(1st, 2nd, 3rd...)
-- %d, %e	일 숫자 (01 ~ 31)
-- %T	    hh:mm:ss
-- %r	    hh:mm:ss AM/PM
-- %H, %k	시 (~23)
-- %h, %l	시 (~12)
-- %i	    분
-- %S, %s	초
-- %p	    AM/PM
SELECT
  DATE_FORMAT(NOW(), '%M %D, %Y %T'),
  DATE_FORMAT(NOW(), '%y-%m-%d %h:%i:%s %p'),
  DATE_FORMAT(NOW(), '%Y년 %m월 %d일 %p %h시 %i분 %s초');

-- STR _ TO _ DATE(S, F)	S를 F형식으로 해석하여 시간/날짜 생성

-- 2. 기타 함수들
-- IF(조건, T, F)	조건이 참이라면 T, 거짓이면 F 반환
SELECT IF (1 > 2, '1는 2보다 크다.', '1은 2보다 작다.');

-- 보다 복잡한 조건은 CASE문을 사용합니다.
SELECT
CASE
  WHEN -1 > 0 THEN '-1은 양수다.'
  WHEN -1 = 0 THEN '-1은 0이다.'
  ELSE '-1은 음수다.'
END;

SELECT
  Price,
  IF (Price > 30, 'Expensive', 'Cheap'),
  CASE
    WHEN Price < 20 THEN '저가'
    WHEN Price BETWEEN 20 AND 30 THEN '일반'
    ELSE '고가'
  END
FROM Products;

-- IFNULL(A, B)	  A가 NULL일 시 B 출력
SELECT
  IFNULL('A', 'B'),
  IFNULL(NULL, 'B');



-- 📌Lesson 5. 조건에 따라 그룹으로 묶기
-- 1. GROUP BY - 조건에 따라 집계된 값을 가져옵니다.
-- 즉, 테이블의 행(row)를 특정 열(column)에 따라 집계
SELECT Country FROM Customers
GROUP BY Country;

-- 여러 컬럼을 기준으로 그룹화할 수도 있습니다.
SELECT 
  Country, City,
  CONCAT_WS(', ', City, Country)
FROM Customers
GROUP BY Country, City;

-- 그룹 함수 활용하기
SELECT
  COUNT(*), OrderDate
FROM Orders
GROUP BY OrderDate;

SELECT
  ProductID,
  SUM(Quantity) AS QuantitySum
FROM OrderDetails
GROUP BY ProductID
ORDER BY QuantitySum DESC;

SELECT
  CategoryID,
  MAX(Price) AS MaxPrice, 
  MIN(Price) AS MinPrice,
  TRUNCATE((MAX(Price) + MIN(Price)) / 2, 2) AS MedianPrice,
  TRUNCATE(AVG(Price), 2) AS AveragePrice
FROM Products
GROUP BY CategoryID;

SELECT 
  CONCAT_WS(', ', City, Country) AS Location,
  COUNT(CustomerID)
FROM Customers
GROUP BY Country, City;

-- WITH ROLLUP - 전체의 집계값
SELECT
  Country, COUNT(*)
FROM Suppliers
GROUP BY Country
WITH ROLLUP;
-- 위의 각 집계함수 쿼리 끝에 WITH ROLLUP 을 추가해보세요.
-- ⚠️ ORDER BY 와는 함께 사용될 수 없습니다.

-- HAVING - 그룹화된 데이터 걸러내기
SELECT
  Country, COUNT(*) AS Count
FROM Suppliers
GROUP BY Country
HAVING Count >= 3;

-- WHERE는 그룹하기 전 데이터, HAVING은 그룹 후 집계에 사용합니다.
SELECT
  COUNT(*) AS Count, OrderDate
FROM Orders
WHERE OrderDate > DATE('1996-12-31')
GROUP BY OrderDate
HAVING Count > 2;

-- 2. DISTINCT - 중복된 값들을 제거합니다.
-- GROUP BY 와 달리 집계함수가 사용되지 않습니다.
-- GROUP BY 와 달리 정렬하지 않으므로 더 빠릅니다.
SELECT DISTINCT CategoryID
FROM Products;
-- 위의 GROUP BY를 사용한 쿼리와 결과 비교

SELECT COUNT DISTINCT CategoryID
FROM Products;
-- 오류 발생

SELECT DISTINCT Country
FROM Customers
ORDER BY Country;

SELECT DISTINCT Country, City
FROM Customers
ORDER BY Country, City;

-- GROUP BY와 DISTINCT 함께 활용하기
SELECT
  Country,
  COUNT(DISTINCT CITY)
FROM Customers
GROUP BY Country;




-- ▶Section 2. Select 더 깊이 파보기

-- 📌Lesson 1. 쿼리 안에 서브쿼리
-- 1. 비상관 서브쿼리
SELECT
  CategoryID, CategoryName, Description,
  (SELECT ProductName FROM Products WHERE ProductID = 1)
FROM Categories;

SELECT * FROM Products
WHERE Price < (
  SELECT AVG(Price) FROM Products
);

SELECT
  CategoryID, CategoryName, Description
FROM Categories
WHERE
  CategoryID =
  (SELECT CategoryID FROM Products
  WHERE ProductName = 'Chais');

SELECT
  CategoryID, CategoryName, Description
FROM Categories
WHERE
  CategoryID IN
  (SELECT CategoryID FROM Products
  WHERE Price > 50);

-- ~ ALL	서브쿼리의 모든 결과에 대해 ~하다
-- ~ ANY	서브쿼리의 하나 이상의 결과에 대해 ~하다
SELECT * FROM Products
WHERE Price > ALL (
  SELECT Price FROM Products
  WHERE CategoryID = 2
);

SELECT
  CategoryID, CategoryName, Description
FROM Categories
WHERE
  CategoryID = ANY
  (SELECT CategoryID FROM Products
  WHERE Price > 50);

-- 2. 상관 서브쿼리
SELECT
  ProductID, ProductName,
  (
    SELECT CategoryName FROM Categories C
    WHERE C.CategoryID = P.CategoryID
  ) AS CategoryName
FROM Products P;

SELECT
  SupplierName, Country, City,
  (
    SELECT COUNT(*) FROM Customers C
    WHERE C.Country = S.Country
  ) AS CustomersInTheCountry,
  (
    SELECT COUNT(*) FROM Customers C
    WHERE C.Country = S.Country 
      AND C.City = S.City
  ) AS CustomersInTheCity
FROM Suppliers S;

SELECT
  CategoryID, CategoryName,
  (
    SELECT MAX(Price) FROM Products P
    WHERE P.CategoryID = C.CategoryID
  ) AS MaximumPrice,
  (
    SELECT AVG(Price) FROM Products P
    WHERE P.CategoryID = C.CategoryID
  ) AS AveragePrice
FROM Categories C;

SELECT
  ProductID, ProductName, CategoryID, Price
  -- ,(SELECT AVG(Price) FROM Products P2
  -- WHERE P2.CategoryID = P1.CategoryID)
FROM Products P1
WHERE Price < (
  SELECT AVG(Price) FROM Products P2
  WHERE P2.CategoryID = P1.CategoryID
);

-- EXISTS / NOT EXISTS 연산자
SELECT
  CategoryID, CategoryName
  -- ,(SELECT MAX(P.Price) FROM Products P
  -- WHERE P.CategoryID = C.CategoryID
  -- ) AS MaxPrice
FROM Categories C
WHERE EXISTS (
  SELECT * FROM Products P
  WHERE P.CategoryID = C.CategoryID
  AND P.Price > 80
);


-- 📌Lesson 2. JOIN - 여러 테이블 조립하기
-- 1. JOIN(INNER JOIN) - 내부 조인
--   양쪽 모두에 값이 있는 행(NOT NULL) 반환
--   'INNER '는 선택사항
SELECT * FROM Categories C
JOIN Products P 
  ON C.CategoryID = P.CategoryID; 

SELECT C.CategoryID, C.CategoryName, P.ProductName
FROM Categories C
JOIN Products P 
  ON C.CategoryID = P.CategoryID; 
-- ambiguous 주의! --> CategoryID는 Categories와 Products 테이블 둘 다에 존재하기 때문에 별명을 써주지 않으면 에러남.

SELECT
  CONCAT(
    P.ProductName, ' by ', S.SupplierName
  ) AS Product,
  S.Phone, P.Price
FROM Products P
JOIN Suppliers S
  ON P.SupplierID = S.SupplierID
WHERE Price > 50
ORDER BY ProductName;

-- 여러 테이블을 JOIN할 수 있습니다.
SELECT 
  C.CategoryID, C.CategoryName, 
  P.ProductName, 
  O.OrderDate,
  D.Quantity
FROM Categories C
JOIN Products P 
  ON C.CategoryID = P.CategoryID
JOIN OrderDetails D
  ON P.ProductID = D.ProductID
JOIN Orders O
  ON O.OrderID = D.OrderID;

-- JOIN한 테이블 GROUP하기
SELECT 
  C.CategoryName,
  MIN(O.OrderDate) AS FirstOrder,
  MAX(O.OrderDate) AS LastOrder,
  SUM(D.Quantity) AS TotalQuantity
FROM Categories C
JOIN Products P 
  ON C.CategoryID = P.CategoryID
JOIN OrderDetails D
  ON P.ProductID = D.ProductID
JOIN Orders O
  ON O.OrderID = D.OrderID
GROUP BY C.CategoryID;

SELECT 
  C.CategoryName, P.ProductName,
  MIN(O.OrderDate) AS FirstOrder,
  MAX(O.OrderDate) AS LastOrder,
  SUM(D.Quantity) AS TotalQuantity
FROM Categories C
JOIN Products P 
  ON C.CategoryID = P.CategoryID
JOIN OrderDetails D
  ON P.ProductID = D.ProductID
JOIN Orders O
  ON O.OrderID = D.OrderID
GROUP BY C.CategoryID, P.ProductID;

-- SELF JOIN - 같은 테이블끼리
SELECT
  E1.EmployeeID, CONCAT_WS(' ', E1.FirstName, E1.LastName) AS Employee,
  E2.EmployeeID, CONCAT_WS(' ', E2.FirstName, E2.LastName) AS NextEmployee
FROM Employees E1 JOIN Employees E2
ON E1.EmployeeID + 1 = E2.EmployeeID;
-- 1번의 전, 마지막 번호의 다음은?


-- 2. LEFT/RIGHT OUTER JOIN - 외부 조인
--   반대쪽에 데이터가 있든 없든(NULL), 선택된 방향에 있으면 출력 - 행 수 결정
--   'OUTER '는 선택사항
SELECT
  E1.EmployeeID, CONCAT_WS(' ', E1.FirstName, E1.LastName) AS Employee,
  E2.EmployeeID, CONCAT_WS(' ', E2.FirstName, E2.LastName) AS NextEmployee
FROM Employees E1
LEFT JOIN Employees E2
ON E1.EmployeeID + 1 = E2.EmployeeID
ORDER BY E1.EmployeeID;
-- LEFT를 RIGHT로 바꿔서도 실행해 볼 것

SELECT
  C.CustomerName, S.SupplierName,
  C.City, C.Country
FROM Customers C
LEFT JOIN Suppliers S
ON C.City = S.City AND C.Country = S.Country;
-- LEFT를 RIGHT로 바꿔서도 실행해 볼 것

SELECT
  IFNULL(C.CustomerName, '-- NO CUSTOMER --'),
  IFNULL(S.SupplierName, '-- NO SUPPLIER --'),
  IFNULL(C.City, S.City),
  IFNULL(C.Country, S.Country)
FROM Customers C
LEFT JOIN Suppliers S
ON C.City = S.City AND C.Country = S.Country;
-- LEFT를 RIGHT로 바꿔서도 실행해 볼 것

-- 3. CROSS JOIN - 교차 조인
-- 조건 없이 모든 조합 반환(A * B)
SELECT
  E1.LastName, E2.FirstName
FROM Employees E1
CROSS JOIN Employees E2
ORDER BY E1.EmployeeID;


-- 📌Lesson 3. UNION - 조합으로 다루기


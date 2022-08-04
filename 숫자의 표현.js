function solution(n) {
  let answer = 0;

  const makeNum = (num, sum) => {
    sum += num;
    if (sum === n) {
      answer++;
      return;
    }
    if (sum > n) {
      return;
    }
    makeNum(num + 1, sum);
  };

  for (let i = 1; i <= n; i++) {
    makeNum(i, 0);
  }

  return answer;
}

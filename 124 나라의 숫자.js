function solution(n) {
  let ans = "";
  const num = [4, 1, 2];

  while (n) {
    ans = num[n % 3] + ans;
    n = n % 3 === 0 ? n / 3 - 1 : Math.floor(n / 3);
  }
  return ans;
}

console.log(solution(10));

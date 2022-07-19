function solution(numbers, target) {
  let count = 0;
  const dfs = (numbers, target, num) => {
    if (numbers.length === 0) {
      if (target === num) {
        count++;
      }
      return;
    }
    const arr = [...numbers];
    const calcNum = arr.shift();
    dfs(arr, target, num + calcNum);
    dfs(arr, target, num - calcNum);
  };
  dfs(numbers, target, 0);
  return count;
}

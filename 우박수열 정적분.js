const makeArr = (n) => {
  const arr = [];
  while (n > 1) {
    arr.push(n);
    if (n % 2 === 0) {
      n /= 2;
    } else {
      n = n * 3 + 1;
    }
  }
  return [...arr, 1];
};

const solution = (k, ranges) => {
  const arr = makeArr(k);
  console.log(arr);

  return ranges.map((range) => {
    let start = range[0];
    let end = arr.length - 1 + range[1];

    if (start > end) {
      return -1.0;
    } else if (start === end) {
      return 0.0;
    }

    let sum = 0;
    while (start < end) {
      sum += (arr[start] + arr[start + 1]) / 2;
      start++;
    }
    return sum;
  });
};

console.log(
  solution(5, [
    [0, 0],
    [0, -1],
    [2, -3],
    [3, -3],
  ])
);

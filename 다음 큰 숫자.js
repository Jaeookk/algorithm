function solution(n) {
  const makeTwo = (num) => {
    let res = "";
    while (num > 0) {
      res = (num % 2) + res;
      num = parseInt(num / 2);
    }
    return res;
  };

  const len = makeTwo(n)
    .split("")
    .filter((el) => el === "1").length;

  while (true) {
    n++;
    if (
      makeTwo(n)
        .split("")
        .filter((el) => el === "1").length === len
    ) {
      return n;
    }
  }
}

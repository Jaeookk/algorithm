function solution(s) {
  let answer = [];
  s = s
    .substring(2, s.length - 2)
    .split("},{")
    .map((array) => {
      return array.split(",").map((element) => {
        return parseInt(element);
      });
    })
    .sort(function (a, b) {
      return a.length - b.length;
    })
    .forEach((array) => {
      array.forEach((num) => {
        if (!answer.includes(num)) {
          answer.push(num);
        }
      });
    });

  return answer;
}

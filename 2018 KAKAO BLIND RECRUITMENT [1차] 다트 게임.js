function solution(dartResult) {
  var answer = 0;
  let arr = [];
  for (let i = 0; i < dartResult.length; i++) {
    if ("1234567890".includes(dartResult[i])) {
      if (dartResult[i + 1] === "0") {
        arr.push(10);
        i++;
      } else arr.push(Number(dartResult[i]));
    } else if (dartResult[i] === "D") {
      arr[arr.length - 1] *= arr[arr.length - 1];
    } else if (dartResult[i] === "T") {
      arr[arr.length - 1] *= arr[arr.length - 1] * arr[arr.length - 1];
    } else if (dartResult[i] === "*") {
      if (arr.length > 1) {
        arr[arr.length - 1] *= 2;
        arr[arr.length - 2] *= 2;
      } else {
        arr[arr.length - 1] *= 2;
      }
    } else if (dartResult[i] === "#") {
      arr[arr.length - 1] *= -1;
    }
  }
  for (let i = 0; i < arr.length; i++) {
    answer += arr[i];
  }
  return answer;
}

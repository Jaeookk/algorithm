function solution(progresses, speeds) {
  let answer = [];
  while (progresses.length > 0) {
    let count = 0;
    while (progresses[0] >= 100) {
      speeds.shift();
      progresses.shift();
      count++;
    }
    if (count > 0) {
      answer.push(count);
    }

    for (let i = 0; i < progresses.length; i++) {
      progresses[i] += speeds[i];
    }
  }
  return answer;
}

function solution(record) {
  let answer = [];
  let ansMap = {};
  for (let i = 0; i < record.length; i++) {
    const id = record[i].split(" ")[1];
    const name = record[i].split(" ")[2];
    if (name) ansMap[id] = name;
  }
  for (let i = 0; i < record.length; i++) {
    const flag = record[i].split(" ")[0];
    const id = record[i].split(" ")[1];
    if (flag === "Enter") {
      answer.push(`${ansMap[id]}님이 들어왔습니다.`);
    } else if (flag === "Leave") {
      answer.push(`${ansMap[id]}님이 나갔습니다.`);
    }
  }
  return answer;
}

function solution(id_list, report, k) {
  let answer = [];
  const obj = {};
  const count = {};
  const ansObj = {};
  for (let i = 0; i < id_list.length; i++) {
    count[id_list[i]] = 0;
    ansObj[id_list[i]] = 0;
    obj[id_list[i]] = [];
  }
  report.forEach((el) => {
    const [user, warn] = el.split(" ");
    if (!obj[user].includes(warn)) {
      count[warn] += 1;
    }
    obj[user] = [...obj[user], warn];
  });
  for (let i = 0; i < id_list.length; i++) {
    if (count[id_list[i]] >= k) {
      for (let key in obj) {
        if (obj[key].includes(id_list[i])) {
          ansObj[key]++;
        }
      }
    }
  }
  for (let key in ansObj) {
    answer.push(ansObj[key]);
  }
  console.log(obj);
  console.log(count);
  console.log(ansObj);
  return answer;
}

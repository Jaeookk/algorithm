function solution(n, k) {
  // k진법으로 나눈 후 split
  const candidates = n.toString(k).split("0");
  // 소수 개수 세기
  return candidates.filter((v) => isPrime(+v)).length;
}

function isPrime(n) {
  if (n <= 1) {
    return false;
  }
  let i = 2;
  while (i * i <= n) {
    if (n % i === 0) {
      return false;
    }
    i++;
  }
  return true;
}

// function solution(n, k) {
//   let ans = 0;

//   const knum = [];
//   while (n > 0) {
//     knum.unshift(n % k);
//     n = parseInt(n / k);
//   }

//   let num = knum.join("").split("0");

//   let max = Math.max(...num.map((el) => +el));

//   const primes = new Array(max + 1).fill(1);
//   primes[0] = 0;
//   primes[1] = 0;

//   for (let i = 2; i * i <= max; i++) {
//     if (primes[i] === 1) {
//       for (let j = i + i; j <= max; j += i) {
//         primes[j] = 0;
//       }
//     }
//   }

//   for (let i = 0; i < num.length; i++) {
//     if (primes[+num[i]] === 1) {
//       ans++;
//     }
//   }

//   return ans;
// }

function solution(w, h) {
  const gcd = (a, b) => (a % b === 0 ? b : gcd(b, a % b));
  return w * h - (w + h - gcd(w, h));
}

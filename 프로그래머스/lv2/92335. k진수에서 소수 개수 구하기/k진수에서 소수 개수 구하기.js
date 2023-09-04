function isPrimeNumber(num) {
    if(num === 2) return true;
    if(num % 2 === 0 || num < 2) return false;
    for(var i=3; i<=Math.floor(Math.sqrt(num)); i++) {
        if(num % i === 0) return false;
    }
    return true;
}

function solution(n, k) {
    var numbers = n.toString(k).split('0').filter(e => (e !== '')).map(e => Number(e)).filter(e => isPrimeNumber(e));
    return numbers.length;
}
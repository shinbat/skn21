//script.js - JavaScript 모듈. 확장자를 .js

document.write("안녕하세요");//화면에 출력
console.log("개발자 도구 console에 출력");
//변수 선언
let name = "홍길동";
name = "이순신";
console.log(name);
const age = 30; // 상수
// age = 50;       // 재할당이 안된다.

let info = `이름: ${name}
나이:${age}`;
console.log(info);
let a = 20;
let b = "20";
console.log(typeof a);
console.log(typeof b);
console.log(a == b);//타입을 맞춘뒤 비교
console.log(a === b);//타입이 다르면 false
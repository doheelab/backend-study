## 1. Nesting loop를 줄이기 (else 쓰지 않기)

## 2. 길이가 긴 컴포넌트(함수)는 분리하기

## 3. const를 let 보다 위에 선언한다.

```javascript
// Bad - 그룹화 없음
let foo;
let i = 0;
const len = this._array.length;
let bar;

// Good
const len = this._array.length;
const len2 = this._array2.length;
let i = 0;
let j = 0;
let foo, bar;
```

## 4. 외부 모듈과 내부 모듈을 구분하여 사용한다.

```javascript
const lodash = require('lodash');
const $ = require(jquery);
const handlebars = require('handlebars');
const d3 = require('d3');

const pluginFactory from '../../factories/pluginFactory';
const predicate from '../../helpers/predicate';
const raphaelRenderUtil from '../../plugins/raphaelRenderUtil';
```

## 5. 배열 복사 시 순환문을 사용하지 않는다.
```javascript
const len = items.length;
let i;

// Bad
for (i = 0; i < len; i++) {
  itemsCopy[i] = items[i];
}

// Good
const itemsCopy = [...items];
```

## 6. wildcard import는 사용하지 않는다.

이름을 지정하지 않으면 모듈이 변경될 때마다 식별자 충돌이 발생할 수 있다.

```javascript
// Bad
import * from './AirbnbStyleGuide';

// Good
import * as AirbnbStyleGuide from './AirbnbStyleGuide';
```

## 7. 삼중 등호 연산자인 ===, !==만 사용한다.

==이나 !=는 암묵적 캐스팅으로 타입에 관계없이 판단되어 조건문의 의도를 파악하기 어렵고 버그로 이어진다.

```javascript
const numberB = 777;

// Bad
if (numberB == '777') {
  ...
}

// Good
if (numberB === 777) {
  ...
}
```

## 8. return문 바로 위는 한 칸 비워 놓는다.

다른 명령과 return문이 붙어있으면 가독성이 좋지 않으므로 return문 전에 한 줄 띄운다.

```javascript
// Bad
function getResult() {
  ...
  return someDataInFalse;
}

// Good
function getResult() {
  ...

  return someDataInFalse;
}
```

## 9. 지역 변수는 그 변수를 포함하는 블록 시작에서 선언하지 않고, 사용 범위를 최소화하기 위해 사용되는 지점과 가장 가까운 곳에서 선언한다.

```javascript

// bad - 함수 호출의 부적절한 위치
function(hasName) {
  const name = getName();

  if (!hasName) {
    return false;
  }

  this.setFirstName(name);

  return true;
}

// good
function(hasName) {
  if (!hasName) {
    return false;
  }

  const name = getName();
  this.setFirstName(name);

  return true;
}
```

## 10. 배열을 선언할 때는 Array 생성자가 아닌 리터럴 구문을 사용한다.

```javascript
// bad
const items = new Array();

// good
const items = [];
```

## 11. 속성 단축 구문을 사용한다.

```javascript
const testUser = 'Nuvilabs';

// bad
const obj = {
  testUser: testUser,
};

// good
const obj = {
  testUser,
};

// bad
const obj = {
  userId: 1,
  testUser,
  departmentId: 2,
  loginDate,
};

// good
const obj = {
  testUser,
  loginDate,
  userId: 1,
  departmentId: 2,
};
```
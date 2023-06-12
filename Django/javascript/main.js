'use strict';

function isEmpty(obj) {
    return Object.keys(obj).length === 0 && obj.constructor === Object;
}

console.log(isEmpty({}))

let sum = 0;

let salaries = {
    John: 100,
    Ann: 160,
    Pete: 130,
}

for (let key in salaries) {
    sum += salaries[key]
}

console.log(sum)

let menu = {
    width: 200,
    height: 300,
    title: "My Menu",
};

function multiplyNumeric(menu) {
    for (let key in menu) {
        if (typeof menu[key] === "number") {
            menu[key] *= 2
        }
    }
    return menu;
}

console.log(multiplyNumeric(menu))

function makeUser() {
    return {
        name: "john",
        ref: this,
    }
}


let ladder = {
    step: 0,
    up() {
        this.step++;
        return this;
    },
    down() {
        this.step--;
        return this;
    },
    showStep() {
        console.log(this.step)
        return this;
    },
}

console.log(ladder.up().down().showStep())

let k = {};

function A() {
    return k;
}
function B() {
    return k;
}

let a = new A;
let b = new B;
console.log(a===b);
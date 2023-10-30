let p = ["polozka1", "polozka2"];
console.log("definice", p, p.length);
p[15] = "skok";
console.log("skok   ", p,p.length);
p.push("push");
console.log("push", p,p.length);
p.pop();
console.log("pop", p,p.length);
p.unshift("unshift");
console.log("unshift", p,p.length);
p.shift();
console.log("shift", p,p.length);

p[-1]= "prvek mimo povolene index";
console.log("-1   ",p,p.length);

p.forEach((item, idx) => {
    console.log(idx, item);
});

p[-1]= undefined;
console.log("-1 undef  ",p, p.length);
p.pop();
console.log("-1 pop   ", p, p.length);
console.log(Object.keys(p));

delete p[-1];
console.log ("-1 delete ", p, p.length);

p[10]= undefined;
console.log ("10 index  ", p, p.length);

p.forEach((item, idx) => {
    console.log(idx, item);
});

p.fill(null, 2, 15);
console.log("fill   ",p,p.length);

console.log("Object");

let o1 = {
    a1: 1,
    "1a": 58,
    1: 1,
    "1": 2
};
console.log(o1);
console.log(o1.a1);
console.log(o1["1"]);
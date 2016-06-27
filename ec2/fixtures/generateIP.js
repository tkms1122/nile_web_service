var a = [];
var pk = 1;
for(var i = 113; i < 120; i++) {
a[a.length] = {model: "ec2.ip", pk: pk++, fields: {address: i, is_used: false}};
}
console.log(JSON.stringify(a, null, 2));

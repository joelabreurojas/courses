
/*
const client = {
    name :  'Joel',
    money : 1500,
    type : function() {
        let type;

        if(money > 1000) {
            type = 'Gold';
        } else {
            type = 'Normal';
        }

        return type;
    }
}

console.log(client.type)
*/

function Client(name, money) {
    this.name = name;
    this.money = money;
    this.type = function() {
        let type;
        
        if(this.money > 1000) {
            type = 'Gold';
        } else {
            type = 'Normal';
        }

        return type;
    }
}
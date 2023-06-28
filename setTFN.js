//8 digit one has a fail rate of around 17%, so not great. Since some numbers just don't have a valid last digit.
//so leaving the code here in case I need it, but its not used anywhere atm
function set8DigitTFN() {
    var randomTFN = "";
    var tfnWeighting = [10,7,8,4,6,3,5,1]
    var tfnSum = 0;
    var randomNo = 0; 

    for (var i = 0; i < 7; i++) {
        randomNo = Math.floor(Math.random() * 10);
        randomTFN += randomNo;
        tfnSum += randomNo * tfnWeighting[i];
    }
    
    for (var i = 0; i < 10; i++) {
        tfnSum += i;
        if (tfnSum % 11 == 0) {
            return randomTFN += i;
        }
        tfnSum -= i;
    }

    return "failed Mod 11 check with " + randomTFN;
}

function set9DigitTFN() {
    var randomTFN = "";
    var tfnWeighting = [10,7,8,4,6,3,5,2,1]
    var tfnSum = 0;
    var randomNo = 0; 

    for (var i = 0; i < 8; i++) {
        randomNo = Math.floor(Math.random() * 10);
        randomTFN += randomNo;
        tfnSum += randomNo * tfnWeighting[i];
    }
    
    for (var i = 0; i < 10; i++) {
        tfnSum += i;
        if (tfnSum % 11 == 0) {
            return randomTFN += i;
        }
        tfnSum -= i;
    }

    return "failed Mod 11 check with " + randomTFN;
}
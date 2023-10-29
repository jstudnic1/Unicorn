function decimalToHexadecimal (decimalValue) {
    let decimalValueCopy = decimalValue;
    if (typeof decimalValueCopy !== "number" || !Number.isInteger(decimalValueCopy))
        throw new Error("Input musí bý číslice.")

    const hexDigits = "0123456789ABCDEF";
    let hexadecimal = "";

    if (decimalValueCopy === 0)
        return "0";

    let isNegative = false;
    if (decimalValue < 0)
        isNegative = true;

    while (decimalValueCopy !== 0){
        let remainder = decimalValueCopy % 16;
        const hexDigit = hexDigits[remainder];
        hexadecimal += hexDigit;
        decimalValueCopy = Math.floor(decimalValueCopy/16);
    }

    if (isNegative)
        hexadecimal = "-" + hexadecimal;
    
    hexadecimal = hexadecimal.split("").reverse().join("")

    return(hexadecimal);
}

function main() {
    const decimalValue = -984;

    try {
        const hexadecimal = decimalToHexadecimal(decimalValue);
        console.log(hexadecimal);
    } catch (error) {
        console.error(error.message);
    }
}

main();
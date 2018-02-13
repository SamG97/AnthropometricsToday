import { forEach, replace, split } from 'lodash';

const measurementLength = 2;
const multiplier = Math.pow(10, measurementLength - 1);

const compress = (name, measurements) => {
    let compressed = replace(name, ' ', '_') + '&&';
    if (measurements) {
        forEach(measurements, (value) => compressed += decimalToB64(Math.floor(value * multiplier)));
    }
    return compressed;
};

const uncompress = (compressed) => {
    const parts = split(compressed, '&&');
    if (parts.length !== 2 || parts[1].length % measurementLength !== 0) {
        return null; // Invalid string
    }
    let cursor = 0;
    const measurements = [];
    while (cursor < parts[1].length) {
        measurements.push(b64ToDecimal(parts[1].substring(cursor, cursor + measurementLength)) / multiplier);
        cursor += measurementLength;
    }
    return { name: replace(parts[0], '_', ' '), measurements: measurements };
};

const decimalToB64 = (n) => {
    let result = '';
    while (n > 0) {
        const remainder = n % 64;
        result = numToSymbol(remainder) + result;
        n = Math.floor(n / 64);
    }
    while (result.length < measurementLength) {
        result = 'A' + result;
    }
    return result;
};

const b64ToDecimal = (n) => {
    let result = 0;
    if (n) {
        const charArray = split(n, '');
        forEach(charArray, (char) => result = result * 64 + symbolToNum(char));
    }
    return result;
};

const numToSymbol = (n) => {
    switch (true) {
        case n < 0:
            return '?'; // Should be impossible to return
        case n < 26:
            return String.fromCharCode(65 + n);
        case n < 52:
            return String.fromCharCode(97 + (n - 26));
        case n < 62:
            return (n - 52).toString();
        case n === 62:
            return '+';
        case n === 63:
            return '=';
        default:
            return '?'; // Should be impossible to return
    }
};

const symbolToNum = (n) => {
    if (n.length !== 1) {
        return -1;
    }
    const ascii = n.charCodeAt(0);
    switch (true) {
        case n === '+':
            return 62;
        case n === '=':
            return 63;
        case ascii > 64 && ascii < 91:
            return ascii - 65;
        case ascii > 96 && ascii < 123:
            return ascii - 71; // -97 for the ASCII offset + 26 for the Base64 offset
        case ascii > 47 && ascii < 58:
            return ascii + 4; // -48 for the ASCII offset + 52 for the Base64 offset
        default:
            return -1; // Should be impossible to return
    }
};

// Only compress and uncompress should ever be called directly; the other functions are only exported for testing
export { b64ToDecimal, compress, decimalToB64, numToSymbol, symbolToNum, uncompress }

import { b64ToDecimal, compress, decimalToB64, numToSymbol, symbolToNum, uncompress } from './urlCompress';

describe('urlCompress', () => {
    describe('numToSymbol', () => {
        it('returns correct uppercase letter at lower bound', () => {
            expect(numToSymbol(0)).toBe('A');
        });

        it('returns correct uppercase letter at upper bound', () => {
            expect(numToSymbol(25)).toBe('Z');
        });

        it('returns correct lowercase letter at lower bound', () => {
            expect(numToSymbol(26)).toBe('a');
        });

        it('returns correct lowercase letter at upper bound', () => {
            expect(numToSymbol(51)).toBe('z');
        });

        it('returns correct number at lower bound', () => {
            expect(numToSymbol(52)).toBe('0');
        });

        it('returns correct number at upper bound', () => {
            expect(numToSymbol(61)).toBe('9');
        });

        it('returns special symbol for 62', () => {
            expect(numToSymbol(62)).toBe('+');
        });

        it('returns returns special symbol for 63', () => {
            expect(numToSymbol(63)).toBe('=');
        });

        it('returns error symbol for invalid input above max input', () => {
            expect(numToSymbol(64)).toBe('?');
        });

        it('returns error symbol for invalid input below min input', () => {
            expect(numToSymbol(-1)).toBe('?');
        });

        it('returns error symbol for invalid input for non-number input', () => {
            expect(numToSymbol('one')).toBe('?');
        });
    });

    describe('symbolToNum', () => {
        it('returns correct number from uppercase letter at lower bound', () => {
            expect(symbolToNum('A')).toBe(0);
        });

        it('returns correct number from uppercase letter at upper bound', () => {
            expect(symbolToNum('Z')).toBe(25);
        });

        it('returns correct number from lowercase letter at lower bound', () => {
            expect(symbolToNum('a')).toBe(26);
        });

        it('returns correct number from lowercase letter at upper bound', () => {
            expect(symbolToNum('z')).toBe(51);
        });

        it('returns correct number from number at lower bound', () => {
            expect(symbolToNum('0')).toBe(52);
        });

        it('returns correct number from number at upper bound', () => {
            expect(symbolToNum('9')).toBe(61);
        });

        it('returns correct number from special symbol +', () => {
            expect(symbolToNum('+')).toBe(62);
        });

        it('returns correct number from special symbol =', () => {
            expect(symbolToNum('=')).toBe(63);
        });

        it('returns error for invalid input for unknown symbol', () => {
            expect(symbolToNum('?')).toBe(-1);
        });

        it('returns error for invalid input for multiple chars', () => {
            expect(symbolToNum('Aa')).toBe(-1);
        });

        it('returns error for invalid input for no char', () => {
            expect(symbolToNum('')).toBe(-1);
        });
    });

    describe('decimalToB64', () => {
        it('handles typical input', () => {
            expect(decimalToB64(123)).toBe('B7');
        });

        it('handles small input', () => {
            expect(decimalToB64(12)).toBe('AM');
        });

        it('handles zero input', () => {
            expect(decimalToB64(0)).toBe('AA');
        });

        it('handles max input', () => {
            expect(decimalToB64(4095)).toBe('==');
        });
    });

    describe('b64ToDecimal', () => {
        it('handles typical input', () => {
            expect(b64ToDecimal('B7')).toBe(123);
        });

        it('handles small input', () => {
            expect(b64ToDecimal('AM')).toBe(12);
        });

        it('handles zero input', () => {
            expect(b64ToDecimal('AA')).toBe(0);
        });

        it('handles max input', () => {
            expect(b64ToDecimal('==')).toBe(4095);
        });
    });

    describe('compress', () => {
        it('handles typical input', () => {
            expect(compress('John Smith', [12.3, 1.2])).toBe('John_Smith&&B7AM');
        });

        it('handles input with no measurements', () => {
            expect(compress('John Smith', [])).toBe('John_Smith&&');
        });

        it('handles input where measurements is null', () => {
            expect(compress('John Smith')).toBe('John_Smith&&');
        });
    });

    describe('uncompress', () => {
        it('handles typical input', () => {
            expect(uncompress('John_Smith&&B7AM')).toEqual({ name: 'John Smith', measurements: [12.3, 1.2] });
        });

        it('handles input with no measurements', () => {
            expect(uncompress('John_Smith&&')).toEqual({ name: 'John Smith', measurements: [] });
        });

        it('rejects input with no separator symbols', () => {
            expect(uncompress('John_Smith')).toBe(null);
        });

        it('rejects input with malformed measurements', () => {
            expect(uncompress('John_Smith&&B7A')).toBe(null);
        });
    });
});
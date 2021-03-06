import capitalise from './formatFieldName';

describe('formatFieldName', () => {
    it('correctly capitalises one word', () => {
        expect(capitalise('test')).toBe('Test');
    });

    it('correctly capitalises multiple words', () => {
        expect(capitalise('test1_test2')).toBe('Test1 Test2');
    });

    it('correctly capitalises no words', () => {
        expect(capitalise('')).toBe('');
    });

    it('correctly capitalises a word which does not start with a letter', () => {
        expect(capitalise('1test')).toBe('1test');
    });
});

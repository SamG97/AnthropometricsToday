import { map, split } from 'lodash';

const capitalise = (sentence) => {
    const wordArray = split(sentence, ' ');
    const capitalisedArray = map(wordArray, (word) => word.charAt(0).toUpperCase() + word.slice(1));
    return capitalisedArray.join(' ');
};

export default capitalise;

import { map, split } from 'lodash';

const formatFieldName = (sentence) => {
    const wordArray = split(sentence, '_');
    const capitalisedArray = map(wordArray, (word) => word.charAt(0).toUpperCase() + word.slice(1));
    return capitalisedArray.join(' ');
};

export default formatFieldName;

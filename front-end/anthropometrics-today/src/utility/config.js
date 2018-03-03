const config = {
    backEndBaseUrl: 'http://localhost:5002',
    webBaseUrl: 'http://localhost',

    historicSuffix: '/student',
    analysisSuffix: '/image_to_student',

    fieldOrdering: ['Name', 'Face_breadth', 'Face_iobreadth', 'Head_length'],
    twinOrdering: ['Name', 'Age', 'DoB', 'College', 'Hair_Colour', 'Eye_Colour', 'Sex']
};

export default config;

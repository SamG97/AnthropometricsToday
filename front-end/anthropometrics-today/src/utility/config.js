const config = {
    // TODO: Replace with real URLs
    baseUrl: 'http://localhost:5002',
    historicSuffix: '/student',
    analysisSuffix: '/image_to_student',

    webBaseUrl: 'http://localhost:3000',

    fieldOrdering: ['Name', 'Face_breadth', 'Face_iobreadth', 'Head_length'],
    twinOrdering: ['Name', 'Age', 'DoB', 'College', 'Hair_Colour', 'Eye_Colour', 'Sex']
};

export default config;

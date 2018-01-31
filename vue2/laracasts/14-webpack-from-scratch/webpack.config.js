let webpack = require('webpack');
let path = require('path');

module.exports = {
    entry: "./assets/js/app.js",
    output: {
        path: path.resolve(__dirname, 'public/js'),
        filename: 'app.js',
        publicPath: './public'
    },

    module: {
        rules: [{
            test: /\.js$/,
            exclude: /node_modules/,
            loader: "babel-loader"
        }]
    },

    resolve: {
        alias: {
            'vue$': 'vue/dist/vue.esm.js'
        }
    },

    plugins: []
};

if (process.env.NODE_ENV === 'production') {
    module.exports.plugins.push(
        new webpack.optimize.UglifyJsPlugin({
            sourceMap: true,
            compress: {
                warnings: false
            }
        })
    )
}
const path = require('path');

module.exports = {
  entry: './Frontend/src/index.js',
  output: {
    path: path.resolve(__dirname, 'DataForge', 'static', 'frontend'),
    filename: 'bundle.js',
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
        options: {
          presets: ['@babel/preset-env', '@babel/preset-react'],
        },
      },
    ],
  },
  devServer: {
    contentBase: path.join(__dirname, 'Frontend', 'src'),
    publicPath: '/static/frontend/',
    proxy: {
      '/api': 'http://localhost:8000',
    },
  },
};
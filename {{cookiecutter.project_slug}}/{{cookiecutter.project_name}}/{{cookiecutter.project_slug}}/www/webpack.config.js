const path = require("path");
const webpack = require('webpack');

const CSS_DIR = path.resolve(__dirname, './static/{{cookiecutter.project_slug}}/css');
const JS_DIR = path.resolve(__dirname, './static/{{cookiecutter.project_slug}}/js');
const BUILD_DIR = path.resolve(__dirname, './static/{{cookiecutter.project_slug}}/dist');

module.exports = {
  resolve: {
    extensions: ['.js', '.jsx']
  },
  entry: {
    index: [`${JS_DIR}/index.jsx`]

  },
  output: {
    path: BUILD_DIR,
    filename: '[name].js'
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: ["babel-loader"]
      },
      {
        test: /\.jsx$/,
        exclude: /node_modules/,
        use: ["babel-loader"]
      },
      {
        test: /\.css$/,
        use: ["style-loader", "css-loader"]
      }
    ]
  },

  plugins: [],

};

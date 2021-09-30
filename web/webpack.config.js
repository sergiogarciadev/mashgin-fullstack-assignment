const webpack = require("webpack");
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CompressionPlugin = require("compression-webpack-plugin");
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const { VueLoaderPlugin } = require('vue-loader');
const { BundleAnalyzerPlugin } = require('webpack-bundle-analyzer');

module.exports = (env = {}) => {
  const config = {
    mode: env.WEBPACK_BUNDLE ? 'production' : 'development',
    devtool: env.WEBPACK_SERVE ? 'eval-cheap-source-map' : 'source-map',
    target: 'browserslist',
    entry: {
      main: {
        import: './src/index',
        dependOn: 'vue-shared',
      },
      'vue-shared': ['vue', 'vuex', 'vue-router']
    },
    output: {
      publicPath: '/',
      path: path.resolve(__dirname, 'dist'),
      filename: env.WEBPACK_SERVE ? '[name].js' : '[name].[chunkhash].js',
    },
    resolve: {
      alias: {
        // required for dynamic templates
        vue: 'vue/dist/vue.esm-bundler.js',
      },
    },
    module: {
      rules: [
        {
          test: /\.vue$/,
          loader: 'vue-loader',
          options: {
            postcss: {},
          },
        },
        {
          test: /\.js$/,
          loader: 'babel-loader',
        },
        {
          test: /\.css$/,
          use: [
            'vue-style-loader',
            // MiniCssExtractPlugin.loader,
            {
              loader: 'css-loader',
              options: { importLoaders: 1 },
            },
            'postcss-loader',
          ],
        },
      ],
    },
    plugins: [
      new MiniCssExtractPlugin({
        filename: env.WEBPACK_SERVE ? "[name].css" : "[name].[contenthash].css",
        chunkFilename: env.WEBPACK_SERVE ? "[id].css" : "[id].[contenthash].css",
      }),
      new HtmlWebpackPlugin({
        title: 'Shopping App',
      }),
      new VueLoaderPlugin(),
      new CompressionPlugin(),
    ],
    optimization: {
      minimize: true,
      usedExports: true,
    },
    devServer: {
      historyApiFallback: true,
      proxy: {
        '/api': 'http://api:5000',
        '/swaggerui': 'http://api:5000',
      }
    },
  };

  if (env.WEBPACK_SERVE) {
    config.plugins.push(new BundleAnalyzerPlugin());
  }

  return config;
};

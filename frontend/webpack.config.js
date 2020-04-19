module.exports = {
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: ["babel-loader"],
      },
    ],
  },
  resolve: {
    extensions: ["*", ".js", ".jsx"],
  },
  devtool: "source-map",
  entry: "./src/index.js",
  output: {
    path: __dirname + "/public",
    publicPath: "/",
    filename: "bundle.js",
  },
  devServer: {
    contentBase: "./public",
    port: 3000,
    host: "localhost",
    historyApiFallback: {
      disableDotRule: true,
    },
    disableHostCheck: true,
    hot: true,
  },
};

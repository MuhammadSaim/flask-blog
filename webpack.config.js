const Encore = require("@symfony/webpack-encore");

Encore.setOutputPath("application/assets")
    .setPublicPath("/assets")
    .addEntry("app", "./src/js/app.js")
    .cleanupOutputBeforeBuild()
    .disableSingleRuntimeChunk()
    .enableSassLoader();


module.exports = Encore.getWebpackConfig();
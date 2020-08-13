const purgecss = require('@fullhuman/postcss-purgecss')({
  content: ['./makemeshort/templates/**/*.html'],
  whitelist: ['bg-red-600', 'bg-green-600', 'bg-blue-600'],
  defaultExtractor: content => content.match(/[A-Za-z0-9-_:/]+/g) || []
})

module.exports = {
  plugins: [
    require('tailwindcss'),
    require('autoprefixer'),
    ...process.env.NODE_ENV === 'production'
      ? [purgecss, require('cssnano')]
      : []
  ]
}
        
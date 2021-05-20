const { fontSize, height, width } = require('tailwindcss/defaultTheme');
module.exports = {
  purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
        colors: {
          primary: '#ff6363',
          secondary: {
              100: '#e2e2d5',
              200: '#888883',
              300: '#95D6A4',
              400: '#D7E9FF',
          },
      },
      fontSize: {
          francos: '8rem',
          small: '4rem',
          medium: '2rem',
          large: '12rem'
      },
      height: {
          small: '200px',
      },
      width: {
          small: '20%',
          medium: '60%',
          large: '80%',
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [require('@tailwindcss/forms')],
}

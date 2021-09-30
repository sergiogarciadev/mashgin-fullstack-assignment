module.exports = {
  darkMode: "class", // 'media' or 'class'
  purge: {
    enabled: true,
    content: ["./src/**/*.{js,jsx,ts,tsx,vue}"],
    options: {
      safelist: ["dark"],
    },
  },
  variants: {
    extend: {
      filter: ['hover', 'focus'],
      transform: ['hover', 'focus'],
      zIndex: ['hover', 'active'],
    }
  }
};

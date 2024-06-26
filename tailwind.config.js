// tailwind.config.js

module.exports = {
  content: ["./portfolio/templates/*.html", "./projects/templates/*.html"],
  theme: {
    extend: {
      colors: {
        background: {
          DEFAULT: "#f7f7f2",
          light: "#f2f7f5",
        },
        mustard: { DEFAULT: "#faae2b", dark: "##e09005" },
        primary: "#899878",
        secondary: "#222725",
        tertiary: "#00473e",
        lightgreen: "#e4e6c3",
        myblack: "#121113",
        notblack: "#1a1a1a",
      },
      height: {
        content: "calc(100vh - 100px)",
      },
      fontFamily: {
        nunito: ["Nunito", "sans-serif"],
        montserrat: ["Montserrat", "sans-serif"],
      },
    },
  },
};

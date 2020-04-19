import { css } from "styled-components";

const sizes = {
  xs: 360,
  s: 375,
  md: 768,
  lg: 1366,
  xl: 1920,
};

export default Object.keys(sizes).reduce((acc, label) => {
  acc[label] = (...args) => css`
    @media (max-width: ${sizes[label]}px) {
      ${css(...args)};
    }
  `;
  return acc;
}, {});

import React from "react";
import { ThemeProvider, createGlobalStyle } from "styled-components";
import { BrowserRouter as Router} from "react-router-dom";
import Store from "./hooks/Store";
import theme from "./utils/theme";
import Wrapper from './containers/Wrapper';

import { render } from "react-dom";

const Sonar = ( ) => {
  const GlobalStyle = createGlobalStyle`
  body {
    padding: 0;
    margin: 0;
    font-family: ${theme.font};
    color: ${theme.colors.black};
    * {
      font-family: ${theme.font};
      color: ${theme.colors.black};
    }
  } `;

  return (
    <Store>
      <Router>
        <ThemeProvider theme={theme}>
          <GlobalStyle />
          <Wrapper />
        </ThemeProvider>
      </Router>
    </Store>
  );
};

render(<Sonar crossorigin />, document.getElementById("app"));
import React from "react";
import ReactDOM from "react-dom";
import { ThemeProvider, createGlobalStyle } from "styled-components";
import { BrowserRouter } from "react-router-dom";
import Wrapper from "./containers/Wrapper";
import theme from "./utils/theme";

const Sonar = () => {
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
    <BrowserRouter>
      <ThemeProvider theme={theme}>
        <GlobalStyle />
        <Wrapper />
      </ThemeProvider>
    </BrowserRouter>
  );
};
ReactDOM.render(<Sonar />, document.getElementById("app"));

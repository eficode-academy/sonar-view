import React from "react";
import ReactDOM from "react-dom";
import { ThemeProvider, createGlobalStyle } from "styled-components";
import { BrowserRouter } from "react-router-dom";
import Store from "./hooks/Store";
import theme from "./utils/theme";

import Login from './components/login/Login';
import Logout from './components/login/Logout';


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
    <Store>
      <BrowserRouter>
        <ThemeProvider theme={theme}>
          <GlobalStyle />

          <Login />

        </ThemeProvider>
      </BrowserRouter>
    </Store>
  );
};

ReactDOM.render(<Sonar />, document.getElementById("app"));

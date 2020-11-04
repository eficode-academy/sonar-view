import React from 'react';
import { GoogleLogout } from 'react-google-login';
import Login from './Login';
import ReactDOM from "react-dom";
import { ThemeProvider, createGlobalStyle } from "styled-components";
import { BrowserRouter } from "react-router-dom";
import Store from "../../hooks/Store";
import theme from "../../utils/theme";


const clientId = process.env.GOOGLE_KEY;

function Logout() {
  const onSuccess = () => {
    console.log('Logout made successfully');
    alert('Logout made successfully ✌');

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

  };

  return (
    <div>
      <GoogleLogout
        clientId={clientId}
        buttonText="Logout"
        onLogoutSuccess={onSuccess}
      ></GoogleLogout>
    </div>
  );
}

export default Logout;
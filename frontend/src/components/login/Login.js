import React from 'react';
import ReactDOM from "react-dom";
import { ThemeProvider, createGlobalStyle } from "styled-components";
import { BrowserRouter } from "react-router-dom";
import Store from "../../hooks/Store";
import theme from "../../utils/theme";

import { GoogleLogin } from 'react-google-login';
// refresh token
import { refreshTokenSetup } from './utils/refreshToken';

import Wrapper from "../../containers/Wrapper";
import Logout from './Logout';

const clientId = process.env.GOOGLE_KEY;

function Login() {
    
  const onSuccess = (res) => {
    console.log('Login Success: currentUser:', res.profileObj);
    alert(
      `Logged in successfully welcome ${res.profileObj.name} 😍. \n See console for full profile object.`
    );
    refreshTokenSetup(res);

    if(res.profileObj.email.includes('@eficode.com')) {

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

              <Wrapper />

            </ThemeProvider>
          </BrowserRouter>
        </Store>
      );
      };
      ReactDOM.render(<Sonar />, document.getElementById("app"));
      
    } else {

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
  
                <p>Acess denied. Login with Eficode Google Login</p>
                <Logout />
  
              </ThemeProvider>
            </BrowserRouter>
          </Store>
        );
      };
      ReactDOM.render(<Sonar />, document.getElementById("app"));
    }

  };

  const onFailure = (res) => {
    console.log('Login failed: res:', res);
    alert(
      `Failed to login. 😢 Please ping this to repo owner ChristofferNissen`
    );
  };

  return (
    <div>
      <GoogleLogin
        clientId={clientId}
        buttonText="Login"
        onSuccess={onSuccess}
        onFailure={onFailure}
        cookiePolicy={'single_host_origin'}
        style={{ marginTop: '100px' }}
        isSignedIn={true}
      />
    </div>
  );
}

export default Login;
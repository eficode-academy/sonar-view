import { string } from "prop-types";
import { useEffect, useContext } from "react";
import { refreshPage } from './refreshPage';

export const refreshTokenSetup = (res) => {
    // Timing to renew access token

    // Extract information about user and save as State
    let mail = res.profileObj.email;
    let name = res.profileObj.name;
    let eficodean = mail.includes("@eficode.com");
    let role = "unauthorized";
    if (eficodean)
      role = "eficodean";

    localStorage.setItem('authToken', res.tokenObj.id_token.toString('base64'))
    localStorage.setItem('user_email', mail);
    localStorage.setItem('user_name', name);
    localStorage.setItem('user_role', role);

    let refreshTiming = (res.tokenObj.expires_in || 3600 - 5 * 60) * 1000;
  
    const refreshToken = async () => {
      const newAuthRes = await res.reloadAuthResponse();
      refreshTiming = (newAuthRes.expires_in || 3600 - 5 * 60) * 1000;
      console.log('newAuthRes:', newAuthRes);

      // saveUserToken(newAuthRes.access_token);  <-- save new token
      localStorage.setItem('authToken', newAuthRes.id_token);

      // Setup the other timer after the first one
      setTimeout(refreshToken, refreshTiming);

      // Query backend for signed token
      await SignToken(newAuthRes.id_token)

    };

    SignToken(res.tokenObj.id_token)

    // Setup first refresh timer
    setTimeout(refreshToken, refreshTiming);

  };

const SignToken = async (tokenObj) => {
  const authUrl = 'http://localhost:8080/google/auth';
  console.log(tokenObj)
  const responseObj = fetch(authUrl, { 
    method: 'post', 
    headers: new Headers({
      'Authorization': 'Bearer '+ tokenObj, 
    })
  });

  const response = await responseObj;
  const signedToken = (await response.json())['auth_token']
  localStorage.setItem('signedAuthToken', signedToken)
  refreshPage()
}

export const getUserInformation = () => {
  return {
    name: localStorage.getItem('user_name'),
    mail: localStorage.getItem('user_email'),
    roles: [localStorage.getItem('user_role')]
  };
};

export const clearToken = (res) => {
  localStorage.setItem('signedAuthToken', '[Token removed by logout]');
  localStorage.setItem('authToken', '[Token removed by logout]');
  localStorage.setItem('user_email', '');
  localStorage.setItem('user_name', '');
  localStorage.setItem('user_role', 'guest');
};
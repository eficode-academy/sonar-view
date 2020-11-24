import React from 'react';
import { useGoogleLogout } from 'react-google-login';

import { clearToken } from './utils/refreshToken';

const clientId = process.env.REACT_APP_GOOGLEKEY;

function LogoutHooks() {
  const onLogoutSuccess = () => {
    clearToken();
  };

  const onFailure = () => {
    console.log('Handle failure cases');
  };

  const { signOut } = useGoogleLogout({
    clientId,
    onLogoutSuccess,
    onFailure,
  });

  return (
    <button type="submit" onClick={signOut} className="button">
      {/* <img src="icons/google.svg" alt="google login" className="icon"/> */}
      <span className="buttonText">Sign out</span>
    </button>
  );
}

export default LogoutHooks;
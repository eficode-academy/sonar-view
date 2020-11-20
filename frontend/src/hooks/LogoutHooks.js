import React from 'react';
import { useGoogleLogout } from 'react-google-login';

import { clearToken } from './utils/refreshToken';
import { refreshPage } from './utils/refreshPage';

const clientId =
  '20840044614-h4k2pdffbgumpqvri0g1sv5mn4q61q71.apps.googleusercontent.com';

function LogoutHooks() {
  const onLogoutSuccess = () => {
    // console.log('Logged out Success');
    // alert('Logged out Successfully ✌');
    clearToken();
    refreshPage();
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
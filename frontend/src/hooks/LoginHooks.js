import React from 'react';
import { useGoogleLogin } from 'react-google-login';
import { refreshPage } from './utils/refreshPage';

// refresh token
import { refreshTokenSetup } from './utils/refreshToken';

const clientId =
  '20840044614-h4k2pdffbgumpqvri0g1sv5mn4q61q71.apps.googleusercontent.com';

function LoginHooks() {
  const onSuccess = (res) => {
    // console.log('Login Success: currentUser:', res.profileObj);
    // alert(
    //   `Logged in successfully welcome ${res.profileObj.name} 😍. \n See console for full profile object.`
    // );
    refreshTokenSetup(res);
  
    refreshPage();

  };

  const onFailure = (res) => {
    console.log('Login failed: res:', res);
    alert(
      `Failed to login. 😢 Please ping this to repo owner ChrstofferNissen`,
    );
  };

  const { signIn } = useGoogleLogin({
    onSuccess,
    onFailure,
    clientId,
    isSignedIn: true,
    accessType: 'offline',
    // responseType: 'code',
    // prompt: 'consent',
  });

  return (
    <button type="submit" onClick={signIn} className="button">
      {/* <img src="icons/google.svg" alt="google login" className="icon"></img> */}
      <span className="buttonText">Sign in with Google</span>
    </button>
  );
}

export default LoginHooks;
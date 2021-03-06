import React from 'react';
import { useGoogleLogin } from 'react-google-login';
import { refreshTokenSetup } from './utils/refreshToken';


const clientId = process.env.REACT_APP_GOOGLEKEY;

const onSuccess = (res) => {
  // console.log('Login Success: currentUser:', res.profileObj);
  // alert(
  //   `Logged in successfully welcome ${res.profileObj.name} 😍. \n See console for full profile object.`
  // );

  refreshTokenSetup(res);
};

const onFailure = (res) => {
  console.log('Login failed: res:', res);
  alert(
    `Failed to login. 😢 Please ping this to repo owner ChrstofferNissen`,
  );
};

export function Login() {
  try {
    return useGoogleLogin({
      onSuccess,
      onFailure,
      clientId,
      isSignedIn: true,
      accessType: 'offline',
      // hostedDomain: 'eficode.com',
      // responseType: 'code',
      // prompt: 'consent',
    });
  } catch (error) {
    console.log(error);
  }
}

export function LoginHooks() {

  const { signIn } = useGoogleLogin({
    onSuccess,
    onFailure,
    clientId,
    isSignedIn: true,
    accessType: 'offline',
    // hostedDomain: 'eficode.com', // auto selects eficode account instead of showing logged in accounts
    // responseType: 'code',
    // prompt: 'consent',
  });

  return (
    <>
      <button type="submit" onClick={signIn} className="button">
        {/* <img src="icons/google.svg" alt="google login" className="icon"></img> */}
        <span className="buttonText">Sign in with Google</span>
      </button>
    </>
  );
}

export default LoginHooks;
import { useEffect, useContext } from "react";
import { Context } from "./Store";
import { clearToken } from "./utils/refreshToken";

const useDataLoader = (query, type) => {
  const url = process.env.REACT_APP_URL;
  const baseUrl = `${url}/${query}`;

  const [state, dispatch] = useContext(Context);

  useEffect(() => {
    let didCancel = false;
    let tokenExpired = false;

    const fetchData = async () => {
      dispatch({ type: `FETCH_${type}_INIT` });

      try {
        const responseObj = fetch(baseUrl, { 
          headers: new Headers({
            'Access-Control-Allow-Origin': '*',
            'Authorization': `Bearer ${ localStorage.getItem('signedAuthToken')}`, 
          }),
        });
        const response = await responseObj;

        if(Number(response.status) === 422) {
          // refresh token
          tokenExpired = true;
          throw new Error("Token expired");

        } else {
          // Assume success
          const json = await response.json();
          if (!didCancel) {
            dispatch({
              type: `FETCH_${type}_SUCCESS`,
              payload: { ...json },
            });
          }
        }

      } catch (error) {
        if (tokenExpired) {
          console.log("Token expired..");
          clearToken();
        } else if (!didCancel) {
          console.log("Error", error);
          clearToken();
          dispatch({ type: `FETCH_${type}_FAILURE`, error });
        }
      }
    };

    fetchData();

    return () => {
      didCancel = true;
    };
  }, [query]);

  return { ...state };
};

export default useDataLoader;
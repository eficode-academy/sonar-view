import { useEffect, useContext } from "react";
import { Context } from "./Store";
import { clearToken } from "./utils/refreshToken";

const useDataLoader = (query, type) => {
  // const baseUrl = `https://sonar-survey-rioz6g7rrq-lz.a.run.app/sonar/${query}`;
  const baseUrl = `http://localhost:8080/google/${query}`;

  const [state, dispatch] = useContext(Context);

  useEffect(() => {
    let didCancel = false;

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
        const json = await response.json();

        if (!didCancel) {
          dispatch({
            type: `FETCH_${type}_SUCCESS`,
            payload: { ...json },
          });
        }
      } catch (error) {
        if (!didCancel) {
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
import React, { createContext, useReducer } from "react";
import reducer from "./reducer";

// TODO: implement proper state management
const initialState = {
  sidebarData: [],
  personDetails: [],
  isLoading: true,
  error: null,
};

const Store = ({ children }) => {
  const [state, dispatch] = useReducer(reducer, initialState);
  return (
    <Context.Provider value={[state, dispatch]}>{children}</Context.Provider>
  );
};
if (module.hot) {
  module.hot.accept("./reducer", () => {
    /* eslint-disable global-require */
    const nextReducer = require("./reducer").default;

    Store.replaceReducer(nextReducer);
  });
}

export const Context = createContext(initialState);
export default Store;

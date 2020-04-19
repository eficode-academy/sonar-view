const reducer = (state, action) => {
  switch (action.type) {
    case "FETCH_SURVEYS_INIT":
      return {
        ...state,
        isLoading: true,
        error: false,
      };
    case "FETCH_SURVEYS_SUCCESS":
      return {
        ...state,
        isLoading: false,
        error: false,
        sidebarData: action.payload,
      };
    case "FETCH_SURVEYS_FAILURE":
      return {
        ...state,
        isLoading: false,
        error: action.error,
      };

    case "FETCH_PERSONS_INIT":
      return {
        ...state,
        isLoading: true,
        error: false,
      };
    case "FETCH_PERSONS_SUCCESS":
      return {
        ...state,
        isLoading: false,
        error: false,
        sidebarData: action.payload,
      };
    case "FETCH_PERSONS_FAILURE":
      return {
        ...state,
        sidebarData: false,
        error: action.error,
      };

    case "FETCH_DETAILS_INIT":
      return {
        ...state,
        isLoading: true,
        error: false,
      };
    case "FETCH_DETAILS_SUCCESS":
      return {
        ...state,
        isLoading: false,
        error: false,
        personDetails: action.payload,
      };
    case "FETCH_DETAILS_FAILURE":
      return {
        ...state,
        personDetails: false,
        error: action.error,
      };
    default:
      throw new Error();
  }
};

export default reducer;

import React, { useEffect, useReducer } from "react";
import PropTypes from "prop-types";
import { Flex } from "rebass";
import { Switch, Route } from "react-router-dom";
import Home from "../components/Home";
import StudyDetails from "../components/StudyDetails";
import Person from "../components/Person";
import SidebarWrapper from "./SidebarWrapper";
import LoginHooks from '../hooks/LoginHooks';
import Unauthorized from "../components/Unauthorized";
import { hasRole } from '../auth/auth';
import { clearToken, getUserInformation } from "../hooks/utils/refreshToken";
import userSubject from "../components/UserSubject";

const SET_USER = 'SET_USER';
const userReducer = (user, action) => {
  if (action === SET_USER) {
    return action.user;
  }
  return user;
}; 

export const Layout = ({ component: Component, route }) => {
  return (
    <Flex width="100%" sx={{ height: "100vh" }}>
      <SidebarWrapper />
      <Flex alignItems="center" justifyContent="center" m="auto" width="100%">
        <Component route={route} />
      </Flex>
    </Flex>
  );
};

Layout.propTypes = {
  route: PropTypes.objectOf(PropTypes.any).isRequired,
  component: PropTypes.func.isRequired,
};

function Wrapper() {
  const layoutRender = (component) => (route) => (
    <Layout component={component} route={route} />
  );

  const [user, dispatch] = useReducer(userReducer, getUserInformation());
  const onUserUpdated = (newUser) => {
    dispatch({
      action: SET_USER,
      newUser,
    });
  };

  useEffect(() => {
    //  Fetch from State
    userSubject.attach(onUserUpdated);

    // detach when unmount
    return () => {
      userSubject.detach(onUserUpdated);
    };
  });

  userSubject.updateUser(); // enable observer pattern
  
  // default state
  if(user.role === null) {
    clearToken()
  }

  return (
    <Switch id='switch'> 
      {hasRole(user, ['eficodean']) && <Route path="/surveys/:date/:email" render={layoutRender(Person)} /> }
      {hasRole(user, ['eficodean']) && <Route path="/surveys/:date" render={layoutRender(StudyDetails)} exact /> }
      {hasRole(user, ['eficodean']) && <Route path="/" render={layoutRender(Home)} exact /> }

      {/* Add page for guest users (non eficodeans) */}
      {hasRole(user, ['guest']) && <Route path="/" render={() => <LoginHooks />} exact /> }
      {hasRole(user, ['unauthorized']) && <Route path="/" render={Unauthorized} exact /> }

      <Route render={() => <h1>404: page not found</h1>} />
      
    </Switch>
  );
}

export default Wrapper;
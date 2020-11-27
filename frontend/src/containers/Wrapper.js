import React, { useEffect, useState } from "react";
import PropTypes from "prop-types";
import { Flex } from "rebass";
import { Switch, Route } from "react-router-dom";
import Home from "../components/Home";
import StudyDetails from "../components/StudyDetails";
import Person from "../components/Person";
import SidebarWrapper from "./SidebarWrapper";
import { Login, LoginHooks } from '../hooks/LoginHooks';
import Unauthorized from "../components/Unauthorized";
import { hasRole } from '../auth/auth';
import { getUserInformation } from "../hooks/utils/refreshToken";
import userSubject from "../components/UserSubject";


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

function element(user, layoutRender) {
  const layoutRender = (component) => (route) => (
    <Layout component={component} route={route} />
  );

  return (
    <>
      <Switch id='switch'> 
        {hasRole(user, ['eficodean']) && <Route path="/surveys/:date/:email" render={layoutRender(Person)} /> }
        {hasRole(user, ['eficodean']) && <Route path="/surveys/:date" render={layoutRender(StudyDetails)} exact /> }
        {hasRole(user, ['eficodean']) && <Route path="/" render={layoutRender(Home)} exact /> }

        {/* Add page for guest users (non eficodeans) */}
        {hasRole(user, ['guest']) && <Route path="/" render={() => <LoginHooks />} exact /> }
        {hasRole(user, ['unauthorized']) && <Route path="/" render={Unauthorized} exact /> }
        
        <Route render={() => <h1>404: page not found</h1>} />
      </Switch>
    </>
  );
}

const Wrapper = () => {
  Login(); // hook call. Ensures token gets refreshed if the user accidentially refreshes the browser

  const [userState, setUser] = useState(getUserInformation(), "user");
  const onUserUpdated = (newUser) => {
    // avoid unneccessary renders of Wrapper element
    const equal = (newUser.role === userState.role && newUser.mail === userState.mail);
    if(!equal)
      setUser(newUser);
  };

  // Observer pattern
  useEffect(() => {
    //  Fetch from State
    userSubject.attach(onUserUpdated);

    // detach when unmount
    return () => {
      userSubject.detach(onUserUpdated);
    };
  });


  return element(userState);

};

export default Wrapper;
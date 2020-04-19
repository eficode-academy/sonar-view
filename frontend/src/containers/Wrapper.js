import React from "react";
import PropTypes from "prop-types";
import { Flex } from "rebass";
import { Switch, Route } from "react-router-dom";
import Home from "../components/Home";
import Main from "../components/Main";
import Person from "../components/Person";
import SidebarWrapper from "./SidebarWrapper";

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

  return (
    <Switch>
      <Route path="/" exact render={layoutRender(Home)} />
      <Route exact path="/surveys/:date" render={layoutRender(Main)} />
      <Route path="/surveys/:date/:email" render={layoutRender(Person)} />
      <Route render={() => <h1>404: page not found</h1>} />
    </Switch>
  );
}

export default Wrapper;

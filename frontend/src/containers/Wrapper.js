import React from "react";

import { Flex } from "rebass";
import { Switch, Route } from "react-router-dom";
import Home from "../components/Home";
import Main from "../components/Main";
import Sidebar from "../components/Sidebar";
import data from "../../testjson.json";

const Wrapper = () => {
  const dates = data.map((item) => {
    return {
      date: item.survey_date,
      id: item.id,
    };
  });

  const renderUsers = (router) => {
    const { id } = router.match.params;
    const day = data.filter((days) => days.id === id);
    return <Main data={day[0]} />;
  };

  return (
    <Flex width="100%">
      <Sidebar items={dates} />
      <Flex alignItems="center" justifyContent="center" width="100%">
        <Switch>
          <Route exact path="/" component={Home} />
          <Route exact path="/surveys/:id" render={renderUsers} />
        </Switch>
      </Flex>
    </Flex>
  );
};

export default Wrapper;

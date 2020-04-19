import React, { useState, useEffect } from "react";
import { withRouter } from "react-router-dom";
import PropTypes from "prop-types";
import Sidebar from "../components/Sidebar";
import useDataLoader from "../hooks/useDataLoader";

function SidebarWrapper({ match }) {
  const [query, setQuery] = useState(["surveys", "SURVEYS"]);
  const [response, setResponse] = useState({});

  const { sidebarData = [], isLoading } = useDataLoader(...query);

  useEffect(() => {
    if (!isLoading) {
      setResponse(sidebarData);
    }
  }, [isLoading]);

  useEffect(() => {
    if (match.path === "/") {
      setQuery(["surveys", "SURVEYS"]);
    } else {
      setQuery([`surveys/${match.params.date}/persons`, "PERSONS"]);
    }
  }, [match.path]);

  return <Sidebar data={response} isLoading={isLoading} />;
}

SidebarWrapper.propTypes = {
  match: PropTypes.shape({
    path: PropTypes.string,
    params: PropTypes.shape({
      email: PropTypes.string,
      date: PropTypes.string,
    }),
  }).isRequired,
};

export default withRouter(SidebarWrapper);

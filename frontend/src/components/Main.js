import React from "react";
import PropTypes from "prop-types";

function Main({ data }) {
  return <div>{data.survey_date}</div>;
}

Main.propTypes = {
  data: PropTypes.shape.isRequired,
};
export default Main;

import React from "react";
import ReactDOM from "react-dom";
import data from "../../test-data/large-test.json";

const Sonar = () => {
  const renderNames = data.filter((item) => console.log(item.Name));
  return <div>{renderNames}</div>;
};
ReactDOM.render(<Sonar />, document.getElementById("app"));

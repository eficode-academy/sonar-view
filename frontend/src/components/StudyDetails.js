import React from "react";

function StudyDetails() {
  const test = localStorage.getItem('authToken');
  return (
    <>
    <p>StudyDetails not implemented yet. Will contain info such as date, number of participants etc...</p>
    <p>{test.substring(0, 150)}</p>
    </>
  );

}

export default StudyDetails;

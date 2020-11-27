import React from "react";
import LogoutHooks from "../hooks/LogoutHooks";

const Unauthorized = () => (
  <>
    <div>
      <h1>Unauthorized</h1>
      <p>Please log in with you eficode email to access data</p>
      <LogoutHooks />
    </div>
  </>
);

export default Unauthorized;
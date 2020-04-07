import React from "react";
import styled from "styled-components";
import { Flex, Box } from "rebass";
import Link from "./Link";
import Logo from "./Logo";

const Wrapper = styled.div`
  padding: 20px 40px;
  width: 240px;
  border-right: 1px solid ${(props) => props.theme.colors.lightGrey};
  height: 100vh;
  position: sticky;
  overflow: scroll;
`;

function Sidebar({ items }) {
  return (
    <Wrapper>
      <Flex flexDirection="column">
        <Box width={["100px", "120px"]} mb="40px">
          <Logo />
        </Box>
        {items.map((item) => (
          <Link href={`/surveys/${item.id}`} title={item.date} />
        ))}
      </Flex>
    </Wrapper>
  );
}

Sidebar.propTypes = {};

export default Sidebar;
